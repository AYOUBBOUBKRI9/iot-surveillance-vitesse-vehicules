import streamlit as st
import plotly.graph_objects as go

def courbe_vitesse(df):

    st.subheader("📈 Vitesse moyenne en fonction du temps")

    # Trier les données par date
    data = df.sort_values("date_heure").copy()

    # Calcul de la vitesse moyenne
    data["vitesse_moyenne"] = (
        data["capteur1"] +
        data["capteur2"] +
        data["capteur3"]
    ) / 3

    # Garder les 50 dernières mesures
    data = data.tail(50)

    # Création de la courbe
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=data["date_heure"],
            y=data["vitesse_moyenne"],
            mode="lines",
            name="Vitesse moyenne",
            line=dict(width=3)
        )
    )

    fig.update_layout(
        title="Évolution de la vitesse moyenne",
        xaxis_title="Temps",
        yaxis_title="Vitesse moyenne (km/h)",
        hovermode="x unified",
        template="plotly_white",
        height=450
    )

    st.plotly_chart(fig, use_container_width=True)