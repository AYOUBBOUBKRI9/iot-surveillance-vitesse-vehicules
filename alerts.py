import streamlit as st


def afficher_alerte(derniere_mesure, limite=100):
    """
    Affiche une alerte selon la dernière mesure.
    """

    vitesse = derniere_mesure["vitesse"]
    etat = derniere_mesure["etat"]
    heure = derniere_mesure["date_heure"]

    st.subheader("🚨 État du système")

    if etat == "ANOMALIE":

        st.warning(f"""
⚠️ **Anomalie détectée**

🕒 Heure : {heure}

Un des capteurs semble incohérent.

Vérifiez le système de mesure.
""")

    elif vitesse > limite:

        st.error(f"""
🚨 **Dépassement de vitesse**

🕒 Heure : {heure}

🚗 Vitesse mesurée : **{vitesse:.1f} km/h**

Limite autorisée : **{limite} km/h**
""")

    else:

        st.success(f"""
✅ **Circulation normale**

🕒 Heure : {heure}

🚗 Dernière vitesse : **{vitesse:.1f} km/h**
""")