import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from prediction import predire_vitesse
from streamlit_autorefresh import st_autorefresh
from db import get_connection
from correction_capteurs import vitesse_corrigee, vitesse_moyenne, etat
from components.kpi import afficher_kpis
from components.sidebar import afficher_sidebar
from simulateur_capteurs import LIMITE_VITESSE
from components.charts import courbe_vitesse
from components.alerts import afficher_alerte
from components.styles import appliquer_style
# Configuration
st.set_page_config(
    page_title="Dashboard IoT - Surveillance de la vitesse",
    page_icon="🚗",
    layout="wide"
)
appliquer_style()
# Actualisation automatique toutes les 3 secondes
st_autorefresh(interval=3000, key="refresh")
st.title("🚗 Dashboard IoT - Surveillance de la vitesse")
# Lecture de la base de données MySQL
conn = get_connection()
query = """
SELECT *
FROM mesures_vitesse
ORDER BY date_heure ASC
"""
df = pd.read_sql(query, conn)
conn.close()
if df.empty:
    st.warning("Aucune donnée disponible.")
    st.stop()
# Calcul de la vitesse moyenne
df["vitesse"] = df.apply(
    lambda x: vitesse_moyenne(
        x.capteur1,
        x.capteur2,
        x.capteur3
    ),
    axis=1
)
df["vitesse_corrigee"] = df.apply(
    lambda x: vitesse_corrigee(
        x.capteur1,
        x.capteur2,
        x.capteur3
    ),
    axis=1
)
df["correction"] = df.apply(
    lambda x:
    "Oui" 
    if (
        abs(x.capteur1 - x.capteur2) > 20
        or abs(x.capteur1 - x.capteur3) > 20
        or abs(x.capteur2 - x.capteur3) > 20
    )
    else "Non",
    axis=1
)
# Etat
df["etat"] = df.apply(
    lambda x: etat(
        x.capteur1,
        x.capteur2,
        x.capteur3
    ),
    axis=1
)
last = df.iloc[-1]
# KPI
afficher_kpis(df)
# Alerte dynamique
afficher_alerte(last, LIMITE_VITESSE)
# COURBE VITESSE MOYENNE / TEMPS
courbe_vitesse(df)
col1, col2 = st.columns(2)
# Dernières alertes
st.subheader("🚨 Dernières alertes")
alertes = df[df["etat"] != "Normal"]
st.dataframe(
    df[
        [
            "date_heure",
            "capteur1",
            "capteur2",
            "capteur3",
            "vitesse",
            "vitesse_corrigee",
            "correction",
            "etat"
        ]
    ].tail(20),
    use_container_width=True
)
nb_mesures, LIMITE = afficher_sidebar()
df = df.tail(nb_mesures)
last = df.iloc[-1]
# Tableau général
st.subheader("📋 Dernières mesures")
st.dataframe(
    df.tail(20),
    use_container_width=True
)
st.divider()
# Prédiction des prochaines vitesses
st.subheader("🤖 Prédiction des prochaines vitesses")
if len(df)>10:
    predictions = predire_vitesse(df)
    futur = pd.DataFrame({

        "Temps futur":
        [
        "+3s",
        "+6s",
        "+9s",
        "+12s",
        "+15s",
        "+18s",
        "+21s",
        "+24s",
        "+27s",
        "+30s"
        ],

        "Vitesse prévue":
        predictions
    })
    st.dataframe(
        futur,
        use_container_width=True
    )
    fig = go.Figure()
    fig.add_scatter(
        y=df["vitesse_corrigee"],
        name="Historique"
    )
    fig.add_scatter(
        y=predictions,
        name="Prédiction"
    )
    st.plotly_chart(
        fig,
        use_container_width=True
    )