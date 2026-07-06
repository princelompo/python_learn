# ==============================================
# JOUR 16 : COMPRÉHENSIONS DE LISTES & GÉNÉRATEURS
# ==============================================
# Thèmes du jour :
# 1. Compréhensions de listes (avec/sans condition)
# 2. Compréhensions de dictionnaires et d'ensembles
# 3. Expressions génératrices (mémoire optimisée)
# 4. Fonctions génératrices avec yield
# ==============================================

import sys

print("=" * 60)
print("📘 LEÇON DU JOUR 16 - COMPRÉHENSIONS ET GÉNÉRATEURS")
print("=" * 60)

# ----------------------------------------------
# 1. COMPRÉHENSIONS DE LISTES - BASES
# ----------------------------------------------
print("\n1️⃣ COMPRÉHENSIONS DE LISTES")
print("-" * 40)

# Sans condition
carres = [x**2 for x in range(10)]
print(f"Carrés de 0 à 9 : {carres}")

# Avec condition (filtrage)
pairs = [x for x in range(20) if x % 2 == 0]
print(f"Nombres pairs < 20 : {pairs}")

# Transformation avec condition
mots = ["python", "java", "c++", "javascript", "ruby"]
mots_longs_maj = [mot.upper() for mot in mots if len(mot) > 4]
print(f"Mots longs en majuscules : {mots_longs_maj}")

# Compréhension imbriquée (équivalent de deux boucles for)
couples = [(x, y) for x in range(3) for y in range(2)]
print(f"Produit cartésien [0,1,2] x [0,1] : {couples}")

# Aplatir une matrice
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
aplatie = [nb for ligne in matrice for nb in ligne]
print(f"Matrice aplatie : {aplatie}")

# ----------------------------------------------
# 2. COMPRÉHENSIONS DE DICTIONNAIRES
# ----------------------------------------------
print("\n2️⃣ COMPRÉHENSIONS DE DICTIONNAIRES")
print("-" * 40)

# Création directe
carres_dict = {x: x**2 for x in range(5)}
print(f"Carrés en dictionnaire : {carres_dict}")

# Inversion clé/valeur (si valeurs uniques)
original = {"a": 1, "b": 2, "c": 3}
inverse = {v: k for k, v in original.items()}
print(f"Dictionnaire inversé : {inverse}")

# Filtrage de dictionnaire
notes = {"Alice": 15, "Bob": 8, "Charlie": 12, "Diane": 19}
admis = {nom: note for nom, note in notes.items() if note >= 10}
print(f"Étudiants admis (note >= 10) : {admis}")

# ----------------------------------------------
# 3. COMPRÉHENSIONS D'ENSEMBLES (SETS)
# ----------------------------------------------
print("\n3️⃣ COMPRÉHENSIONS D'ENSEMBLES")
print("-" * 40)

# Ensemble des premières lettres
mots = ["pomme", "poire", "banane", "fraise", "framboise"]
initiales = {mot[0] for mot in mots}
print(f"Initiales uniques : {initiales}")

# Élimination des doublons et transformation
nombres = [1, 2, 2, 3, 3, 3, 4]
carres_uniques = {x**2 for x in nombres}
print(f"Carrés uniques : {carres_uniques}")

# ----------------------------------------------
# 4. EXPRESSIONS GÉNÉRATRICES (LAZY EVALUATION)
# ----------------------------------------------
print("\n4️⃣ EXPRESSIONS GÉNÉRATRICES")
print("-" * 40)

# Création d'un générateur avec parenthèses
gen_carres = (x**2 for x in range(5))
print(f"Type de gen_carres : {type(gen_carres)}")  # generator

# Consommation manuelle
print("Consommation avec next() :")
print(f"  next(gen) -> {next(gen_carres)}")
print(f"  next(gen) -> {next(gen_carres)}")
print(f"  Reste converti en liste : {list(gen_carres)}")

# Comparaison mémoire : liste vs générateur
n = 1_000_000
liste_grande = [i for i in range(n)]
gen_grand = (i for i in range(n))

taille_liste = sys.getsizeof(liste_grande)
taille_gen = sys.getsizeof(gen_grand)

print(f"\nComparaison mémoire pour {n:,} éléments :")
print(f"  Liste : {taille_liste / (1024*1024):.2f} Mo")
print(f"  Générateur : {taille_gen} octets (négligeable)")

# Exemple pratique : somme de carrés avec générateur (économie mémoire)
somme_carres = sum(x**2 for x in range(1_000_000))
print(f"\nSomme des carrés de 0 à 999,999 (calculée avec générateur) : {somme_carres}")

# ----------------------------------------------
# 5. FONCTIONS GÉNÉRATRICES AVEC yield
# ----------------------------------------------
print("\n5️⃣ FONCTIONS GÉNÉRATRICES (yield)")
print("-" * 40)

def compte_a_rebours(n):
    """Générateur de compte à rebours de n à 0."""
    while n >= 0:
        yield n
        n -= 1

print("Compte à rebours depuis 5 :")
for valeur in compte_a_rebours(5):
    print(f"  {valeur}...", end=" ")
print("Go !")

def fibonacci(n):
    """Générateur des n premiers nombres de Fibonacci."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nPremiers nombres de Fibonacci :")
print(list(fibonacci(10)))

# Générateur infini (avec précaution)
def nombres_pairs_infini():
    n = 0
    while True:
        yield n
        n += 2

pairs = nombres_pairs_infini()
print("Premiers nombres pairs (infini) : ", end="")
for _ in range(6):
    print(next(pairs), end=" ")
print()

# ----------------------------------------------
# 6. PIPELINE DE TRAITEMENT AVEC GÉNÉRATEURS
# ----------------------------------------------
print("\n6️⃣ PIPELINE DE TRAITEMENT (COMPOSITION)")
print("-" * 40)

# Exemple : traiter un flux de données sans tout charger
def lire_fichier_simule():
    """Simule la lecture d'un gros fichier ligne par ligne."""
    lignes = [
        "INFO: Démarrage",
        "ERROR: Échec connexion",
        "INFO: Traitement",
        "WARNING: Mémoire élevée",
        "ERROR: Timeout"
    ]
    for ligne in lignes:
        yield ligne

def filtrer_erreurs(lignes):
    """Ne garde que les lignes contenant ERROR."""
    for ligne in lignes:
        if "ERROR" in ligne:
            yield ligne

def extraire_message(lignes):
    """Extrait le message après 'ERROR: '."""
    for ligne in lignes:
        yield ligne.split("ERROR: ")[1]

# Pipeline : chaque étape est un générateur
flux = lire_fichier_simule()
erreurs = filtrer_erreurs(flux)
messages = extraire_message(erreurs)

print("Messages d'erreur extraits :")
for msg in messages:
    print(f"  - {msg}")

# ----------------------------------------------
# 7. EXERCICE INTÉGRÉ : ANALYSE DE LOGS
# ----------------------------------------------
print("\n7️⃣ EXERCICE - ANALYSE DE LOGS AVEC GÉNÉRATEURS")
print("-" * 40)

# On simule un fichier de log volumineux
log_simule = [
    "2024-01-01 10:00:01 INFO User login",
    "2024-01-01 10:01:15 ERROR Database connection failed",
    "2024-01-01 10:02:30 INFO File processed",
    "2024-01-01 10:03:45 WARNING Disk space low",
    "2024-01-01 10:04:12 ERROR Authentication timeout",
    "2024-01-01 10:05:00 INFO User logout"
]

def lignes_erreur(logs):
    """Filtre les lignes contenant 'ERROR'."""
    for ligne in logs:
        if "ERROR" in ligne:
            yield ligne

def extraire_timestamp_et_message(logs_erreur):
    """Extrait le timestamp et le message d'erreur."""
    for ligne in logs_erreur:
        parts = ligne.split(" ERROR ")
        if len(parts) == 2:
            timestamp = parts[0][:19]  # Extrait "2024-01-01 10:01:15"
            message = parts[1]
            yield timestamp, message

# Pipeline
erreur_gen = lignes_erreur(log_simule)
details_gen = extraire_timestamp_et_message(erreur_gen)

print("Erreurs détectées avec timestamp :")
for ts, msg in details_gen:
    print(f"  [{ts}] {msg}")

# Avec une compréhension de liste si on veut stocker (pour petit volume)
erreurs_liste = [ligne for ligne in log_simule if "ERROR" in ligne]
print(f"\nListe des erreurs (stockée) : {erreurs_liste}")

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 16")
print("=" * 60)