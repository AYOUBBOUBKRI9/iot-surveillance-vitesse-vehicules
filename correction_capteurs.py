"""
Correction et détection des anomalies
Projet IoT - Surveillance de la vitesse
"""
from config import LIMITE_VITESSE
def vitesse_moyenne(c1, c2, c3):
    """
    Calcule la vitesse moyenne
    """
    return round((c1 + c2 + c3) / 3, 2)
def detecter_anomalie(c1, c2, c3):
    """
    Vérifie si un capteur est incohérent.
    Retourne :
        True  -> anomalie
        False -> normal
    """
    valeurs = [c1, c2, c3]
    ecart = max(valeurs) - min(valeurs)
    return ecart > 25
def capteur_defectueux(c1, c2, c3):
    """
    Détermine quel capteur est probablement défectueux.
    """
    valeurs = [c1, c2, c3]
    moyenne = sum(valeurs) / 3
    distances = [
        abs(c1 - moyenne),
        abs(c2 - moyenne),
        abs(c3 - moyenne)
    ]
    indice = distances.index(max(distances))
    return indice + 1
def vitesse_corrigee(c1, c2, c3):
    ecart_max = 20   # seuil d'écart accepté
    capteurs = [c1, c2, c3]
    # Vérifier si capteur 1 est suspect
    if abs(c1-c2) > ecart_max and abs(c1-c3) > ecart_max:
        return round((c2+c3)/2, 2)
    # Vérifier si capteur 2 est suspect
    elif abs(c2-c1) > ecart_max and abs(c2-c3) > ecart_max:
        return round((c1+c3)/2, 2)
    # Vérifier si capteur 3 est suspect
    elif abs(c3-c1) > ecart_max and abs(c3-c2) > ecart_max:
        return round((c1+c2)/2, 2)
    # Aucun capteur défaillant
    else:
        return round(
            (c1+c2+c3)/3,
            2
        )
def etat(c1, c2, c3):
    """
    Détermine l'état de la mesure.
    """
    if detecter_anomalie(c1, c2, c3):
        return "ANOMALIE"
    vitesse = vitesse_moyenne(c1, c2, c3)
    if vitesse > LIMITE_VITESSE:
        return "DEPASSEMENT"
    return "NORMAL"