# 🚗 IoT Speed Monitoring System

## 📌 Description

Ce projet a été réalisé dans le cadre du module **Internet of Things (IoT)**.

L'objectif est de développer un système intelligent de **surveillance de la vitesse des véhicules** capable de simuler le fonctionnement d'une solution IoT réelle en l'absence de matériel (Arduino/ESP32).

Le système utilise **trois capteurs virtuels** pour mesurer la vitesse des véhicules, enregistre les données dans une base de données **MySQL**, détecte les anomalies et les dépassements de vitesse, puis affiche les résultats dans un **dashboard interactif développé avec Streamlit**.

---

## 🎯 Objectifs

- Simuler un système IoT de surveillance de la vitesse.
- Générer automatiquement les mesures de trois capteurs.
- Stocker les données dans une base MySQL.
- Calculer la vitesse moyenne.
- Détecter les anomalies des capteurs.
- Détecter les dépassements de vitesse.
- Visualiser les données en temps réel.
- Fournir un tableau de bord interactif.

---

## 🛠 Technologies utilisées

- Python
- Streamlit
- MySQL
- Pandas
- Plotly
- mysql-connector-python
- streamlit-autorefresh

---

## 📂 Structure du projet

```text
IOT_VITESSE/
│
├── dashboard.py
├── simulateur_capteurs.py
├── correction_capteurs.py
├── prediction.py
├── db.py
├── config.py
├── requirements.txt
│
├── components/
│   ├── alerts.py
│   ├── charts.py
│   ├── kpi.py
│   ├── sidebar.py
│   └── styles.py
│
├── assets/
│   ├── logo.png
│   └── police.png
│
└── README.md
```

---

## 🗄 Base de données

Nom de la base :

```text
iot_vitesse
```

Table principale :

```text
mesures_vitesse
```

| Champ | Type |
|--------|------|
| id | INT |
| date_heure | DATETIME |
| capteur1 | FLOAT |
| capteur2 | FLOAT |
| capteur3 | FLOAT |

Les trois colonnes des capteurs représentent directement les vitesses mesurées en **km/h**.

---

## ⚙ Fonctionnement du système

### 1. Simulation

En l'absence d'une carte Arduino ou ESP32, les mesures sont générées automatiquement par le fichier :

```text
simulateur_capteurs.py
```

Toutes les quelques secondes, une nouvelle mesure est créée et enregistrée dans MySQL.

---

### 2. Traitement

Le module :

```text
correction_capteurs.py
```

effectue :

- le calcul de la vitesse moyenne ;
- la détection des anomalies entre les capteurs ;
- la correction des mesures si nécessaire.

---

### 3. Dashboard

Le tableau de bord affiche :

- la dernière vitesse mesurée ;
- la vitesse moyenne ;
- la vitesse maximale ;
- la vitesse minimale ;
- les alertes de dépassement de vitesse ;
- les anomalies détectées ;
- une courbe représentant l'évolution de la vitesse moyenne en fonction du temps ;
- les dernières mesures enregistrées.

---

## 🚨 Détection des anomalies

Une anomalie est détectée lorsqu'un des trois capteurs fournit une valeur très différente des deux autres.

Exemple :

| Capteur 1 | Capteur 2 | Capteur 3 |
|-----------:|-----------:|-----------:|
| 35 | 36 | 7 |

Le système identifie automatiquement le troisième capteur comme incohérent.

---

## 🚦 Détection des dépassements

Lorsque la vitesse moyenne dépasse la limite définie (100 km/h par défaut), une alerte est affichée dans le tableau de bord.

---

## ▶ Installation

Cloner le dépôt :

```bash
git clone https://github.com/VOTRE_USERNAME/IOT_VITESSE.git
```

Entrer dans le projet :

```bash
cd IOT_VITESSE
```

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activer l'environnement :

Windows :

```bash
.venv\Scripts\activate
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuration MySQL

Créer un fichier `.env` :

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=iot_vitesse
```

Créer ensuite la base de données :

```sql
CREATE DATABASE iot_vitesse;
```

Importer les données dans la table :

```text
mesures_vitesse
```

---

## ▶ Lancer le projet

Démarrer le simulateur :

```bash
python simulateur_capteurs.py
```

Puis lancer le dashboard :

```bash
streamlit run dashboard.py
```

---

## 📈 Résultats

Le système permet :

- ✔ Simulation complète d'un système IoT
- ✔ Génération automatique des mesures
- ✔ Stockage des données dans MySQL
- ✔ Calcul de la vitesse moyenne
- ✔ Détection des anomalies
- ✔ Détection des dépassements de vitesse
- ✔ Tableau de bord interactif
- ✔ Visualisation en temps réel

---

## 🚀 Perspectives

Dans une version future, le système pourra être connecté à une carte **ESP32** ou **Arduino** afin de remplacer les données simulées par des mesures réelles provenant de capteurs de vitesse.

---

## 👩‍💻 Auteur

**Dalal Machehoul**

Master en Informatique – Gouvernance et Transformation Digitale

Université Mohammed V – Rabat

Projet réalisé dans le cadre du module **Internet of Things (IoT)**.

