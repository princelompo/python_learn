import csv
from pathlib import Path
import os
import pandas as pd

print("=" * 60)
print(" MANIPULATION DE FICHIERS CSV AVEC PYTHON")
print("=" * 60)

# ----------------------------------------------

dossier = Path.cwd() /'LEARNPY'



with open(dossier / "data.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f) # Crée un objet lecteur pour parcourir les lignes du CSV
    print("Contenu du CSV :")
    for ligne in lecteur:
        print(ligne) # Affiche chaque ligne du CSV en supprimant les espaces superflus

with open(dossier / "data.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f) # Crée un objet écrivain pour ajouter des lignes au CSV
    writer.writerow(["David", "Bonhomme", 28, "bonhomme@mail.com", "Alger", "Policier",50000]) # Ajoute une nouvelle ligne au CSV
print("Nouvelle ligne ajoutée au CSV.")

with open(dossier / "data.csv", "r", encoding="utf-8") as f:
    lecteur = csv.DictReader(f) # Crée un objet DictReader pour lire le CSV avec des clés d'en-tête
    print("\nContenu du CSV avec DictReader :")
    for ligne in lecteur:
        print(f"{ligne['Nom']} {ligne['Prenom']} a {ligne['Age']} ans et travaille comme {ligne['Profession']} à {ligne['Ville']} (email: {ligne['Email']}, salaire: {ligne['Salaire']})")

# Acces au nieme element du CSV
reponse = int(input("\nEntrez le numéro de la ligne à afficher (1 pour la première ligne, etc.) : "))
with open(dossier / "data.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    for i, ligne in enumerate(lecteur, start=1):
        if i == reponse:
            print(f"Ligne {reponse} : {ligne}")
            break
    else:
        print(f"Le fichier ne contient pas {reponse} lignes.")

# Acces au dernier element du CSV
with open(dossier / "data.csv", "r", encoding="utf-8") as f:
    lecteur = csv.reader(f)
    dernier_ligne = None    
    for ligne in lecteur:
        dernier_ligne = ligne
    if dernier_ligne:
        print(f"\nDernière ligne du CSV : {dernier_ligne}")
    else:
        print("Le fichier CSV est vide.")


with open(dossier / "data.csv", "r", newline="", encoding="utf-8") as f:
    data = pd.read_csv(f)

print(data)