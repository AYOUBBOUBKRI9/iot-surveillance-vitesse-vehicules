
# Configuration générale du projet IoT
# Base de données
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "DMAI2002"   # Mets ton mot de passe MySQL ici si tu en as un
DB_NAME = "iot_vitesse"

# Paramètres IoT
LIMITE_VITESSE = 100       # km/h
INTERVALLE_MESURE = 3      # secondes entre deux mesures

# Paramètres Dashboard
NB_DERNIERES_MESURES = 50

# Couleurs
COULEUR_NORMAL = "#2ECC71"
COULEUR_ALERTE = "#E74C3C"
COULEUR_ANOMALIE = "#F39C12"
COULEUR_COURBE = "#3498DB"

# Titre
APP_TITLE = "🚗 Dashboard IoT - Surveillance de la vitesse"