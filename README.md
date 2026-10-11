# 🚗 IoT Vehicle Speed Monitoring System

**Simulation IoT · Python · MySQL · Streamlit · Data Visualization**

Un système intelligent de surveillance de la vitesse des véhicules, conçu pour simuler une architecture IoT complète, de la génération des mesures à leur visualisation dans un tableau de bord interactif.

## 📌 Présentation du projet

Comment surveiller la vitesse des véhicules, détecter les mesures incohérentes et identifier les excès de vitesse sans disposer de capteurs physiques ?

Ce projet propose une solution basée sur la **simulation de trois capteurs virtuels**, l'enregistrement des données dans une base MySQL et leur exploitation à travers une application interactive développée avec Streamlit.

Le système automatise la collecte des mesures, leur traitement, la détection des anomalies et la génération d'alertes, tout en permettant de suivre l'évolution des vitesses à travers des indicateurs et des graphiques.

> **Objectif :** reproduire le fonctionnement d'une solution IoT de surveillance routière dans un environnement entièrement simulé, sans nécessiter de carte Arduino ou ESP32.

## 🎯 Objectifs

- Simuler la collecte de données issues de trois capteurs de vitesse.
- Enregistrer et centraliser les mesures dans une base de données MySQL.
- Calculer les indicateurs statistiques liés à la vitesse.
- Identifier les mesures aberrantes et les incohérences entre capteurs.
- Détecter automatiquement les dépassements de la limite de vitesse.
- Visualiser les données historiques et les dernières mesures.
- Développer un tableau de bord interactif facilitant le suivi du système.

## 🛠️ Technologies utilisées

| Technologie | Utilisation |
|---|---|
| **Python** | Simulation, traitement et logique métier |
| **MySQL** | Stockage et gestion des mesures |
| **Pandas** | Manipulation et analyse des données |
| **Streamlit** | Développement du tableau de bord interactif |
| **Plotly** | Visualisation graphique des mesures |
| **mysql-connector-python** | Connexion à la base de données |
| **streamlit-autorefresh** | Actualisation périodique du dashboard |

## 🏗️ Architecture du système

Le système suit un flux de traitement simple :

```text
┌──────────────────────────────┐
│    Capteurs virtuels (x3)    │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│     Simulation des mesures   │
│     simulateur_capteurs.py   │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│         Base MySQL           │
│        iot_vitesse           │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│   Traitement et détection    │
│      correction_capteurs.py  │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│  Dashboard interactif        │
│  Streamlit + Plotly          │
└──────────────────────────────┘
```

## ⚙️ Fonctionnalités principales

### 1. Simulation des capteurs

Le module `simulateur_capteurs.py` génère des mesures de vitesse à partir de trois capteurs virtuels. Les données sont produites périodiquement puis enregistrées dans MySQL.

Cette approche permet de tester le système sans matériel physique et de reproduire différents scénarios de surveillance.

### 2. Traitement et contrôle de cohérence

Le module `correction_capteurs.py` exploite les mesures disponibles afin de :

- Calculer la vitesse moyenne.
- Comparer les valeurs fournies par les différents capteurs.
- Repérer les mesures incohérentes.
- Appliquer les mécanismes de correction prévus dans le système.

### 3. Surveillance des dépassements de vitesse

Le système compare la vitesse calculée à une limite configurable, fixée à **100 km/h par défaut**.

Lorsqu'un dépassement est détecté, le tableau de bord affiche une alerte permettant d'identifier rapidement les situations nécessitant une attention particulière.

### 4. Détection des anomalies

Le système recherche les écarts importants entre les mesures des trois capteurs.

Exemple de mesure incohérente :

| Capteur 1 | Capteur 2 | Capteur 3 |
|---:|---:|---:|
| 35 km/h | 36 km/h | 7 km/h |

Dans cet exemple, la troisième mesure est nettement différente des deux autres et peut être signalée comme anomalie.

### 5. Dashboard interactif

L'application Streamlit centralise les informations utiles au suivi du système :

- Dernière vitesse mesurée.
- Vitesse moyenne, minimale et maximale.
- Historique des mesures.
- Évolution temporelle de la vitesse.
- Alertes de dépassement.
- Anomalies détectées entre les capteurs.

Les graphiques interactifs facilitent l'exploration des données et la compréhension du comportement du système.

## 🗄️ Modèle de données

**Base de données :** `iot_vitesse`

**Table principale :** `mesures_vitesse`

| Champ | Type | Description |
|---|---|---|
| `id` | INT | Identifiant de la mesure |
| `date_heure` | DATETIME | Date et heure de collecte |
| `capteur1` | FLOAT | Vitesse mesurée par le capteur 1 |
| `capteur2` | FLOAT | Vitesse mesurée par le capteur 2 |
| `capteur3` | FLOAT | Vitesse mesurée par le capteur 3 |

Les vitesses sont exprimées en km/h.

## 📂 Structure du projet

```text
IOT_VITESSE/
├── components/
│   ├── alerts.py
│   ├── charts.py
│   ├── kpi.py
│   ├── sidebar.py
│   └── styles.py
├── assets/
│   ├── logo.png
│   └── police.png
├── config.py
├── correction_capteurs.py
├── dashboard.py
├── db.py
├── prediction.py
├── simulateur_capteurs.py
├── requirements.txt
└── README.md
```

*Remarque : cette arborescence présente l'organisation cible du projet. Les fichiers `assets/` ne sont à conserver dans la documentation que s'ils existent effectivement dans le dépôt.*

## 🚀 Installation et exécution

### Prérequis

- Python installé sur la machine.
- MySQL Server.
- Git, facultatif si le projet est téléchargé sous forme d'archive.

### 1. Récupérer le projet

```bash
git clone https://github.com/AYOUBBOUBKRI9/iot-surveillance-vitesse-vehicules.git
cd iot-surveillance-vitesse-vehicules
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

Activer l'environnement sous Windows :

```bash
.venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer MySQL

Créer la base de données :

```sql
CREATE DATABASE iot_vitesse;
```

Configurer ensuite les paramètres de connexion dans un fichier `.env` local, si le projet utilise cette méthode :

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=iot_vitesse
```

**Sécurité :** le fichier `.env` contenant les identifiants réels ne doit jamais être publié sur GitHub.

La table `mesures_vitesse` doit également être créée selon le schéma attendu par le projet, si elle n'est pas créée automatiquement par le code.

### 5. Lancer la simulation

Dans un premier terminal :

```bash
python simulateur_capteurs.py
```

### 6. Démarrer le tableau de bord

Dans un second terminal, avec le même environnement virtuel activé :

```bash
streamlit run dashboard.py
```

L'application s'ouvrira dans le navigateur. Vérifie que MySQL est démarré et que la configuration de connexion est correcte.

## 📊 Résultats attendus

Le projet met en œuvre une chaîne de traitement comprenant :

- La génération périodique de données simulées.
- Le stockage des mesures dans MySQL.
- Le calcul d'indicateurs statistiques.
- Le contrôle de cohérence entre capteurs.
- La détection des dépassements de vitesse.
- La visualisation des données dans une interface interactive.

## 🔮 Perspectives d'amélioration

Plusieurs évolutions sont envisageables :

- Remplacer les capteurs simulés par des capteurs physiques connectés à un ESP32 ou à une carte Arduino.
- Ajouter un système de notifications lors des dépassements.
- Développer des analyses prédictives à partir de l'historique des mesures.
- Renforcer la gestion des erreurs et la supervision de la collecte.
- Déployer le dashboard sur une plateforme accessible à distance.

## 👨‍💻 Auteur

**Mohamed Ayoub Boubkri**

Master en Informatique — Gouvernance et Transformation Digitale  
Université Mohammed V — Rabat

Projet réalisé dans le cadre du module *Internet of Things (IoT)*.

---

*Ce projet constitue une simulation pédagogique. Les mesures générées ne proviennent pas de véhicules réels et les résultats dépendent des règles de simulation et de traitement implémentées.*
