# ==============================================
# JOUR 17 : MODULES, PACKAGES & IMPORTS
# ==============================================
# Thèmes du jour :
# 1. Importer des modules (bibliothèque standard)
# 2. Créer son propre module
# 3. Comprendre les packages
# 4. Utiliser __name__ == "__main__"
# 5. Bonnes pratiques d'organisation
# ==============================================

print("=" * 60)
print("📘 LEÇON DU JOUR 17 - MODULES ET IMPORTS")
print("=" * 60)

# ----------------------------------------------
# 1. IMPORTS DE BASE : MODULES STANDARD
# ----------------------------------------------
print("\n1️⃣ MODULES DE LA BIBLIOTHÈQUE STANDARD")
print("-" * 40)

import math
import random
from datetime import datetime, timedelta
import os
import sys

# Utilisation de math
rayon = 5
aire = math.pi * math.pow(rayon, 2)
print(f"Aire d'un cercle de rayon {rayon} : {aire:.2f}")

# Utilisation de random
print(f"Nombre aléatoire entre 1 et 100 : {random.randint(1, 100)}")
couleurs = ["rouge", "vert", "bleu"]
print(f"Couleur aléatoire : {random.choice(couleurs)}")

# Utilisation de datetime
maintenant = datetime.now()
print(f"Date et heure actuelles : {maintenant.strftime('%Y-%m-%d %H:%M:%S')}")
demain = maintenant + timedelta(days=1)
print(f"Demain même heure : {demain.strftime('%Y-%m-%d %H:%M:%S')}")

# Utilisation de os
print(f"Répertoire courant : {os.getcwd()}")
print(f"Contenu du répertoire (premiers 5) : {os.listdir('.')[:5]}")

# Utilisation de sys
print(f"Version de Python : {sys.version}")
print(f"Plateforme : {sys.platform}")

# ----------------------------------------------
# 2. CRÉATION D'UN MODULE PERSONNEL
# ----------------------------------------------
print("\n2️⃣ CRÉER SON PROPRE MODULE")
print("-" * 40)

# On va simuler la création d'un module séparé en écrivant son contenu
# dans une chaîne, puis en l'exécutant. Normalement tu aurais un fichier .py.
# Ici pour la démonstration on définit directement une "bibliothèque".

# Imaginons que ce code soit dans un fichier 'geometrie.py'
def perimetre_rectangle(longueur, largeur):
    return 2 * (longueur + largeur)

def perimetre_cercle(rayon):
    return 2 * math.pi * rayon

# Utilisation (comme si on importait le module)
print(f"Périmètre d'un rectangle 5x3 : {perimetre_rectangle(5, 3)}")
print(f"Périmètre d'un cercle de rayon 5 : {perimetre_cercle(5):.2f}")

# En réalité, dans un autre fichier on ferait :
# from geometrie import perimetre_rectangle

# ----------------------------------------------
# 3. PACKAGES (STRUCTURE AVEC __init__.py)
# ----------------------------------------------
print("\n3️⃣ ORGANISATION EN PACKAGES")
print("-" * 40)

# Un package est un dossier avec un fichier __init__.py (même vide).
# Ici on ne peut pas créer de dossier, mais on explique le principe.

print("Exemple de structure :")
print("""
mon_projet/
├── main.py
└── utils/
    ├── __init__.py
    ├── calculs.py
    └── affichage.py
""")
print("Pour importer : from utils import calculs")
print("Ou : from utils.calculs import ma_fonction")

# ----------------------------------------------
# 4. LA VARIABLE __name__ == "__main__"
# ----------------------------------------------
print("\n4️⃣ UTILISATION DE __name__ == '__main__'")
print("-" * 40)

def fonction_principale():
    print("Ceci est la fonction principale du script.")

# Ce bloc ne s'exécute que si ce fichier est lancé directement.
if __name__ == "__main__":
    print("Le script est exécuté directement (pas importé).")
    fonction_principale()
else:
    print("Le module a été importé, la fonction principale n'est pas exécutée.")

# Pour tester l'import, tu peux lancer ce script directement.
# Si tu l'importes depuis un autre, le message du else s'affichera.

# ----------------------------------------------
# 5. BONNES PRATIQUES
# ----------------------------------------------
print("\n5️⃣ BONNES PRATIQUES")
print("-" * 40)

print("• Regrouper les imports en haut du fichier.")
print("• Importer d'abord les modules standard, puis les modules tiers, puis les modules locaux.")
print("• Éviter 'from module import *'.")
print("• Utiliser des alias pour les noms longs (ex: import numpy as np).")
print("• Protéger le code exécutable avec if __name__ == '__main__'.")

# ----------------------------------------------
# 6. EXERCICE INTÉGRÉ : MODULE DE CONVERSION
# ----------------------------------------------
print("\n6️⃣ EXERCICE - CRÉATION D'UN MODULE DE CONVERSION")
print("-" * 40)

# On définit un pseudo-module de conversion directement
def celsius_vers_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_vers_celsius(f):
    return (f - 32) * 5/9

def km_vers_miles(km):
    return km * 0.621371

def miles_vers_km(miles):
    return miles / 0.621371

# Utilisation
temp_c = 25
print(f"{temp_c}°C = {celsius_vers_fahrenheit(temp_c)}°F")
dist_km = 10
print(f"{dist_km} km = {km_vers_miles(dist_km):.2f} miles")

# Si on avait un fichier conversions.py, on ferait :
# from conversions import celsius_vers_fahrenheit

# ----------------------------------------------
# 7. GESTION DU PATH ET IMPORTS DYNAMIQUES (BONUS)
# ----------------------------------------------
print("\n7️⃣ BONUS - AJOUTER UN CHEMIN D'IMPORT")
print("-" * 40)

# Parfois ton module n'est pas dans le même dossier. Tu peux ajouter son chemin :
nouveau_chemin = "/chemin/vers/mon/module"
if os.path.exists(nouveau_chemin):
    sys.path.insert(0, nouveau_chemin)
    print(f"Le chemin {nouveau_chemin} a été ajouté à sys.path")
else:
    print("Chemin non trouvé, démonstration seulement.")

print(f"Chemins d'import actuels (premiers 5) : {sys.path[:5]}")

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 17")
print("=" * 60)