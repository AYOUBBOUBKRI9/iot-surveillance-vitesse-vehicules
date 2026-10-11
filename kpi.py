import streamlit as st
def afficher_kpis(df):
    derniere = df.iloc[-1]
    col1, col2, col3, col4 = st.columns(4)
    # Dernière vitesse
    with col1:
        st.metric(
            "🚗 Dernière vitesse",
            f"{derniere['vitesse']:.1f} km/h"
        )
    # Vitesse moyenne
    with col2:
        st.metric(
            "📊 Vitesse moyenne",
            f"{df['vitesse'].mean():.1f} km/h"
        )
    # Vitesse maximale
    with col3:
        st.metric(
            "🚀 Vitesse maximale",
            f"{df['vitesse'].max():.1f} km/h"
        )
    # Etat actuel
    with col4:
        etat = derniere["etat"]
        if etat == "NORMAL":
            st.success("🟢 NORMAL")
        elif etat == "DEPASSEMENT":
            st.error("🚨 DEPASSEMENT")
        else:
            st.warning("⚠ ANOMALIE")