import streamlit as st

def afficher_sidebar():

    st.sidebar.title("🚗 Paramètres du Dashboard")

    st.sidebar.markdown("---")

    # Nombre de mesures à afficher
    nb_mesures = st.sidebar.selectbox(
        "📋 Nombre de mesures",
        options=[10, 20, 30, 50, 100],
        index=3
    )

    # Limite de vitesse
    limite = st.sidebar.slider(
        "🚦 Limite de vitesse (km/h)",
        min_value=50,
        max_value=150,
        value=100,
        step=10
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown("### ℹ️ Informations")

    st.sidebar.write("• Surveillance des vitesses")
    st.sidebar.write("• 3 capteurs de mesure")
    st.sidebar.write("• Détection des anomalies")
    st.sidebar.write("• Alertes de dépassement")

    return nb_mesures, limite