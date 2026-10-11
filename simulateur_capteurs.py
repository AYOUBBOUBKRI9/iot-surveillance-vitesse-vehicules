import random
import time
from datetime import datetime
from db import get_connection
# Configuration
INTERVAL = 3
LIMITE_VITESSE = 100

def lancer_simulation():
    conn = get_connection()
    cursor = conn.cursor()
    print("===== Simulation IoT démarrée =====")
    while True:
        # Choix du scénario
        scenario = random.random()
        # ========= NORMAL ==========
        if scenario < 0.80:
            base = random.randint(40, 90)
            capteur1 = base + random.randint(-2,2)
            capteur2 = base + random.randint(-2,2)
            capteur3 = base + random.randint(-2,2)
        # ===== DEPASSEMENT =======
        elif scenario < 0.95:
            base = random.randint(105,130)
            capteur1 = base + random.randint(-2,2)
            capteur2 = base + random.randint(-2,2)
            capteur3 = base + random.randint(-2,2)
        # ===== ANOMALIE ======
        else:
            base = random.randint(40,80)
            capteur1 = base + random.randint(-2,2)
            capteur2 = base + random.randint(-2,2)
            if random.random() < 0.5:
                capteur3 = random.randint(0,10)
            else:
                capteur3 = random.randint(130,150)
        # Insertion MySQL
        sql = """
        INSERT INTO mesures_vitesse(date_heure, capteur1, capteur2, capteur3) VALUES
        (%s,%s,%s,%s)"""
        cursor.execute(
            sql,
            (
                datetime.now(),
                capteur1,
                capteur2,
                capteur3
            )
        )
        conn.commit()
        # Affichage terminal

        vitesse = round(
            (capteur1+capteur2+capteur3)/3,
            2
        )
        print("------------------------------------")
        print(datetime.now())

        print("Capteur 1 :", capteur1)
        print("Capteur 2 :", capteur2)
        print("Capteur 3 :", capteur3)
        print("Vitesse moyenne :", vitesse, "km/h")
        if vitesse > LIMITE_VITESSE:
            print("🚨 DEPASSEMENT DE VITESSE")
        if abs(capteur3-capteur1)>25 or abs(capteur3-capteur2)>25:
            print("⚠ CAPTEUR 3 DEFECTUEUX")
        time.sleep(INTERVAL)
# Lancer seulement si on exécute ce fichier directement
if __name__ == "__main__":

    lancer_simulation()