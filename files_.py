# ==============================================
# JOUR 18 : GESTION DE FICHIERS (READ, WRITE, APPEND)
# ==============================================
# Thèmes du jour :
# 1. Ouverture avec open() et fermeture automatique (with)
# 2. Modes de fichier (r, w, a)
# 3. Lecture (read, readline, readlines, itération)
# 4. Écriture et ajout
# 5. Manipulation de chemins avec pathlib
# 6. Introduction au module CSV
# ==============================================

import csv
from pathlib import Path
import os
import shutil

print("=" * 60)
print("📘 LEÇON DU JOUR 18 - GESTION DE FICHIERS")
print("=" * 60)

# ----------------------------------------------
# 1. CRÉATION D'UN DOSSIER DE TRAVAIL TEMPORAIRE
# ----------------------------------------------
print("\n1️⃣ PRÉPARATION DU DOSSIER DE TRAVAIL")
print("-" * 40)

# On utilise pathlib pour créer un dossier "temp_jour18" proprement
dossier = Path.cwd() /'LEARNPY/dossier_temp'
dossier.mkdir(exist_ok=True)  # crée le dossier s'il n'existe pas déjà
print(f"Dossier de travail : {dossier.absolute()}")

# ----------------------------------------------
# 2. ÉCRITURE DANS UN FICHIER (mode 'w')
# ----------------------------------------------    
print("\n2️⃣ ÉCRITURE DE FICHIER (mode 'w')")
print("-" * 40)

fichier_notes = dossier / "notes.txt"
contenu_initial = """Journal de bord
Jour 1 : Setup terminé
Jour 2 : Variables maîtrisées
"""

with open(fichier_notes, "w", encoding="utf-8") as f:
    f.write(contenu_initial)

print(f"Fichier créé : {fichier_notes}")
print("Contenu écrit. Le fichier précédent (s'il existait) a été écrasé.")

# ----------------------------------------------
# 3. LECTURE COMPLÈTE (read, readlines)
# ----------------------------------------------
print("\n3️⃣ LECTURE DE FICHIER")
print("-" * 40)

with open(fichier_notes, "r", encoding="utf-8") as f:
    tout = f.read()  # Lit tout le fichier en une seule chaîne
print("Contenu complet (read) :")
print(tout)

# On peut aussi lire ligne par ligne avec readlines()
with open(fichier_notes, "r", encoding="utf-8") as f:
    lignes = f.readlines()  # Liste de lignes (avec le \n)
print(f"Nombre de lignes lues : {len(lignes)}")
for i, ligne in enumerate(lignes, start=1):
    print(f"  Ligne {i}: {ligne.strip()}")

# Itération directe (recommandée pour les gros fichiers)
print("\nItération ligne par ligne :")
with open(fichier_notes, "r", encoding="utf-8") as f:
    for ligne in f:
        # Traitement sans charger tout le fichier
        print(f"  -> {ligne.strip()}")

# ----------------------------------------------
# 4. AJOUT EN FIN DE FICHIER (mode 'a')
# ----------------------------------------------
print("\n4️⃣ AJOUT À LA FIN (mode 'a')")
print("-" * 40)

with open(fichier_notes, "a", encoding="utf-8") as f:
    f.write("Jour 3 : Listes et slicing\n")

# Vérification
with open(fichier_notes, "r", encoding="utf-8") as f:
    print("Contenu après ajout :")
    print(f.read())

# ----------------------------------------------
# 5. ÉCRITURE DE PLUSIEURS LIGNES AVEC writelines
# ----------------------------------------------
print("\n5️⃣ ÉCRITURE AVEC writelines()")
print("-" * 40)

nouvelles_lignes = ["Ligne A\n", "Ligne B\n", "Ligne C\n"]
fichier_lignes = dossier / "lignes.txt"

with open(fichier_lignes, "w", encoding="utf-8") as f:
    f.writelines(nouvelles_lignes)

print(f"Fichier {fichier_lignes} créé avec writelines.")
with open(fichier_lignes, "r", encoding="utf-8") as f:
    print("Contenu :")
    print(f.read())

# ----------------------------------------------
# 6. MANIPULATION DE CHEMINS AVEC pathlib
# ----------------------------------------------
print("\n6️⃣ MANIPULATION DE CHEMINS (pathlib)")
print("-" * 40)

fichier = dossier / "exemple.txt"
print(f"Chemin : {fichier}")
print(f"Nom du fichier : {fichier.name}")
print(f"Dossier parent : {fichier.parent}")
print(f"Suffixe : {fichier.suffix}")

# Créer un fichier et tester son existence
fichier.write_text("Test de pathlib", encoding="utf-8")
if fichier.exists():
    print(f"Le fichier {fichier} existe.")
    print(f"Taille : {fichier.stat().st_size} octets")

# Lister les fichiers du dossier
print(f"\nContenu du dossier {dossier} :")
for element in dossier.iterdir():
    if element.is_file():
        print(f"  📄 {element.name}")
    elif element.is_dir():
        print(f"  📁 {element.name}")

# ----------------------------------------------
# 7. MODULE CSV (LECTURE ET ÉCRITURE)
# ----------------------------------------------
print("\n7️⃣ TRAVAILLER AVEC DES FICHIERS CSV")
print("-" * 40)

fichier_csv = dossier / "contacts.csv"

# Écriture d'un fichier CSV
with open(fichier_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Nom", "Email", "Âge"])  # En-tête
    writer.writerow(["Alice", "alice@mail.com", 30])
    writer.writerow(["Bob", "bob@mail.com", 25])
    writer.writerow(["Charlie", "charlie@mail.com", 35])

print(f"Fichier CSV créé : {fichier_csv}")

# Lecture du CSV
with open(fichier_csv, "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    print("Contenu du CSV :")
    for ligne in reader:
        print(f"  {ligne}")

# Accès par dictionnaire (DictReader)
with open(fichier_csv, "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    print("\nAvec DictReader (clés = en-têtes) :")
    for ligne in reader:
        print(f"  {ligne['Nom']} a {ligne['Âge']} ans (email: {ligne['Email']})")

# ----------------------------------------------
# 8. EXERCICE INTÉGRÉ : JOURNAL DE BORD
# ----------------------------------------------
print("\n8️⃣ EXERCICE - JOURNAL DE BORD PERSONNALISÉ")
print("-" * 40)

def ajouter_entree_journal(chemin_fichier, date, contenu):
    """Ajoute une entrée datée dans un fichier journal."""
    with open(chemin_fichier, "a", encoding="utf-8") as f:
        f.write(f"[{date}] {contenu}\n")
    print(f"Entrée ajoutée : [{date}] {contenu}")

def afficher_journal(chemin_fichier):
    """Affiche le contenu complet du journal."""
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            print(f"=== Journal : {chemin_fichier} ===")
            for ligne in f:
                print(ligne.rstrip())
    except FileNotFoundError:
        print("Le journal n'existe pas encore.")

# Test du journal
journal_path = dossier / "mon_journal.txt"
ajouter_entree_journal(journal_path, "2024-01-01", "Début de l'apprentissage Python")
ajouter_entree_journal(journal_path, "2024-01-02", "J'ai compris les listes")
ajouter_entree_journal(journal_path, "2024-01-03", "Je manipule des fichiers")

afficher_journal(journal_path)

# ----------------------------------------------
# 9. BONUS : NETTOYAGE DU DOSSIER TEMPORAIRE
# ----------------------------------------------
print("\n9️⃣ NETTOYAGE (optionnel)")
print("-" * 40)

# Pour supprimer le dossier et son contenu, décommentez la ligne suivante :
# import shutil
# shutil.rmtree(dossier)

reponse = input("Voulez-vous supprimer le dossier temporaire et son contenu ? (o/n) : ").strip().lower()
if reponse == 'o':
    shutil.rmtree(dossier)
    print(f"Le dossier {dossier} et son contenu ont été supprimés.")
else:
    print("Le dossier n'a pas été supprimé.")


print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 18")
print("=" * 60)