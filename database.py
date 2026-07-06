# ==============================================
# JOUR 28 : BASES DE DONNÉES (SQLite / MySQL)
# ==============================================
# Thèmes du jour :
# 1. Création d'une base SQLite et d'une table
# 2. Insertion de données (INSERT)
# 3. Lecture de données (SELECT)
# 4. Mise à jour (UPDATE) et suppression (DELETE)
# 5. Requêtes paramétrées (sécurité)
# 6. Context manager (with) pour connexion
# ==============================================

import sqlite3
from pathlib import Path

print("=" * 60)
print("📘 LEÇON DU JOUR 28 - BASES DE DONNÉES")
print("=" * 60)

# Préparation : dossier temporaire pour la base
tmp = Path("temp_jour28")
tmp.mkdir(exist_ok=True)
chemin_bd = tmp / "demo.db"

# ----------------------------------------------
# 1. CRÉATION DE LA BASE ET DE LA TABLE
# ----------------------------------------------
print("\n1️⃣ CRÉATION DE LA BASE ET DE LA TABLE")
print("-" * 40)

with sqlite3.connect(chemin_bd) as connexion:
    curseur = connexion.cursor()
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS produits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            prix REAL NOT NULL,
            stock INTEGER DEFAULT 0,
            categorie TEXT
        )
    """)
    print(f"Base '{chemin_bd}' créée. Table 'produits' prête.")

# ----------------------------------------------
# 2. INSERTION DE DONNÉES
# ----------------------------------------------
print("\n2️⃣ INSERTION DE DONNÉES")
print("-" * 40)

with sqlite3.connect(chemin_bd) as connexion:
    curseur = connexion.cursor()
    
    # Insertion simple
    curseur.execute(
        "INSERT INTO produits (nom, prix, stock, categorie) VALUES (?, ?, ?, ?)",
        ("Ordinateur Portable", 899.99, 10, "Informatique")
    )
    
    # Insertion multiple avec executemany
    nouveaux_produits = [
        ("Souris", 19.99, 50, "Informatique"),
        ("Clavier", 49.99, 30, "Informatique"),
        ("Livre Python", 39.99, 20, "Livres"),
        ("Cahier", 4.99, 100, "Papeterie"),
        ("Stylo", 2.49, 200, "Papeterie")
    ]
    curseur.executemany(
        "INSERT INTO produits (nom, prix, stock, categorie) VALUES (?, ?, ?, ?)",
        nouveaux_produits
    )
    print(f"{len(nouveaux_produits)} produits ajoutés.")

# ----------------------------------------------
# 3. LECTURE (SELECT)
# ----------------------------------------------
print("\n3️⃣ LECTURE DE DONNÉES (SELECT)")
print("-" * 40)

with sqlite3.connect(chemin_bd) as connexion:
    curseur = connexion.cursor()
    
    # Tout lire
    curseur.execute("SELECT * FROM produits")
    tous = curseur.fetchall() # Récupère tous les résultats dans une liste de tuples
    print("Tous les produits :")
    for p in tous:
        print(f"  [{p[0]}] {p[1]} - {p[2]:.2f}€ (stock: {p[3]})")
    
    # Filtrage avec WHERE
    print("\nProduits en rupture de stock (stock = 0) :")
    curseur.execute("SELECT nom FROM produits WHERE stock = 0")
    ruptures = curseur.fetchall()
    if ruptures:
        for r in ruptures:
            print(f"  - {r[0]}")
    else:
        print("  Aucun.")
    
    # Tri avec ORDER BY
    print("\nProduits triés par prix décroissant :")
    curseur.execute("SELECT nom, prix FROM produits ORDER BY prix DESC")
    tries = curseur.fetchall()
    for nom, prix in tries:
        print(f"  {nom} : {prix:.2f}€")

# ----------------------------------------------
# 4. MISE À JOUR (UPDATE)
# ----------------------------------------------
print("\n4️⃣ MISE À JOUR (UPDATE)")
print("-" * 40)

with sqlite3.connect(chemin_bd) as connexion:
    curseur = connexion.cursor()
    
    # Augmenter le stock des produits Informatique de 5
    curseur.execute(
        "UPDATE produits SET stock = stock + 5 WHERE categorie = ?",
        ("Informatique",)
    )
    print(f"{curseur.rowcount} produit(s) mis à jour.")
    
    # Vérification
    curseur.execute("SELECT nom, stock FROM produits WHERE categorie = ?", ("Informatique",))
    for nom, stock in curseur.fetchall():
        print(f"  {nom} : nouveau stock = {stock}")

# ----------------------------------------------
# 5. SUPPRESSION (DELETE)
# ----------------------------------------------
print("\n5️⃣ SUPPRESSION (DELETE)")
print("-" * 40)

with sqlite3.connect(chemin_bd) as connexion:
    curseur = connexion.cursor()
    
    # Supprimer les produits dont le prix est < 5€
    curseur.execute("DELETE FROM produits WHERE prix < 5")
    print(f"{curseur.rowcount} produit(s) supprimé(s).")
    
    # Vérification
    curseur.execute("SELECT nom, prix FROM produits ORDER BY prix")
    for nom, prix in curseur.fetchall():
        print(f"  {nom} : {prix:.2f}€")

# ----------------------------------------------
# 6. EXERCICE INTÉGRÉ : GESTION DE BIBLIOTHÈQUE
# ----------------------------------------------
print("\n6️⃣ EXERCICE - MINI BIBLIOTHÈQUE AVEC SQLITE")
print("-" * 40)

# Création de la table
with sqlite3.connect(chemin_bd) as connexion:
    curseur = connexion.cursor()
    curseur.execute("""
        CREATE TABLE IF NOT EXISTS livres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            annee INTEGER,
            lu INTEGER DEFAULT 0
        )
    """)
    # Nettoyage des tests précédents si on relance
    curseur.execute("DELETE FROM livres")

# Fonctions de gestion
def ajouter_livre(titre, auteur, annee=None):
    with sqlite3.connect(chemin_bd) as conn:
        conn.execute(
            "INSERT INTO livres (titre, auteur, annee) VALUES (?, ?, ?)",
            (titre, auteur, annee)
        )

def marquer_lu(id_livre):
    with sqlite3.connect(chemin_bd) as conn:
        conn.execute("UPDATE livres SET lu = 1 WHERE id = ?", (id_livre,))

def lister_livres(filtre_lu=None):
    with sqlite3.connect(chemin_bd) as conn:
        if filtre_lu is None:
            return conn.execute("SELECT * FROM livres ORDER BY titre").fetchall()
        else:
            return conn.execute(
                "SELECT * FROM livres WHERE lu = ? ORDER BY titre",
                (filtre_lu,)
            ).fetchall()

# Utilisation
ajouter_livre("1984", "George Orwell", 1949)
ajouter_livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943)
ajouter_livre("Dune", "Frank Herbert", 1965)

marquer_lu(2)  # Marque "Le Petit Prince" comme lu

print("Tous les livres :")
for livre in lister_livres():
    statut = "✅" if livre[4] else "⬜"
    print(f"  {statut} [{livre[0]}] {livre[1]} par {livre[2]} ({livre[3]})")

print("\nLivres lus :")
for livre in lister_livres(filtre_lu=1):
    print(f"  ✅ [{livre[0]}] {livre[1]}")

print("\nLivres non lus :")
for livre in lister_livres(filtre_lu=0):
    print(f"  ⬜ [{livre[0]}] {livre[1]}")

# ----------------------------------------------
# 7. BONUS : NETTOYAGE
# ----------------------------------------------
import shutil
shutil.rmtree(tmp)
print(f"\nDossier temporaire '{tmp}' supprimé.")

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 28")
print("=" * 60)