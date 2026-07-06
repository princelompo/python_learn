# ==============================================
# JOUR 19 : GESTION DES ERREURS (TRY, EXCEPT, FINALLY)
# ==============================================
# Thèmes du jour :
# 1. Structure try/except de base
# 2. Capturer plusieurs exceptions spécifiques
# 3. Utilisation de else et finally
# 4. Lever des exceptions avec raise
# 5. Créer ses propres exceptions personnalisées
# 6. Bonnes pratiques de robustesse
# ==============================================

import sys

print("=" * 60)
print("📘 LEÇON DU JOUR 19 - GESTION DES ERREURS")
print("=" * 60)

# ----------------------------------------------
# 1. CAPTURE D'EXCEPTION SIMPLE
# ----------------------------------------------
print("\n1️⃣ TRY/EXCEPT DE BASE")
print("-" * 40)

try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : Division par zéro interceptée.")

print("Le programme continue normalement après l'erreur.\n")

# ----------------------------------------------
# 2. CAPTURE DE PLUSIEURS EXCEPTIONS
# ----------------------------------------------
print("2️⃣ CAPTURE MULTIPLE")
print("-" * 40)

def division_securisee(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Impossible de diviser par zéro.")
        return None
    except TypeError:
        print("Type de données incompatible pour la division.")
        return None

print(division_securisee(10, 2))
print(division_securisee(10, 0))
print(division_securisee(10, "deux"))

# ----------------------------------------------
# 3. BLOCS ELSE ET FINALLY
# ----------------------------------------------
print("\n3️⃣ ELSE ET FINALLY")
print("-" * 40)

def ouvrir_et_lire(chemin):
    fichier = None
    try:
        fichier = open(chemin, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"Le fichier '{chemin}' est introuvable.")
    else:
        print(f"Fichier ouvert avec succès. Première ligne : {fichier.readline().strip()}")
    finally:
        if fichier and not fichier.closed:
            fichier.close()
            print("Fichier fermé dans finally.\n")

# Test avec un fichier qui n'existe pas
ouvrir_et_lire("inexistant.txt")

# Test avec un fichier qui existe (on crée un fichier temporaire)
from pathlib import Path
dossier = Path("temp_jour19")
dossier.mkdir(exist_ok=True)
f_temp = dossier / "demo.txt"
f_temp.write_text("Ligne 1\nLigne 2\n", encoding="utf-8")
ouvrir_et_lire(f_temp)

# ----------------------------------------------
# 4. LEVER UNE EXCEPTION AVEC RAISE
# ----------------------------------------------
print("4️⃣ RAISE (LEVER UNE EXCEPTION)")
print("-" * 40)

def verifier_age(age):
    if not isinstance(age, int):
        raise TypeError("L'âge doit être un entier.")
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif.")
    if age > 150:
        raise ValueError("L'âge est trop élevé (>150).")
    print(f"Âge valide : {age} ans.")

tests = [25, -5, 200, "trente"]
for t in tests:
    try:
        verifier_age(t)
    except (TypeError, ValueError) as e:
        print(f"Validation échouée pour {t!r} -> {e}")

# ----------------------------------------------
# 5. EXCEPTIONS PERSONNALISÉES
# ----------------------------------------------
print("\n5️⃣ CRÉER SES PROPRES EXCEPTIONS")
print("-" * 40)

class SoldeInsuffisantError(Exception):
    """Exception levée quand un retrait dépasse le solde."""
    def __init__(self, solde, montant):
        self.solde = solde
        self.montant = montant
        super().__init__(f"Solde {solde}€ insuffisant pour retirer {montant}€.")

def retirer_solde(solde, montant):
    if montant > solde:
        raise SoldeInsuffisantError(solde, montant)
    return solde - montant

compte = 100
try:
    nouveau = retirer_solde(compte, 150)
except SoldeInsuffisantError as e:
    print(f"Opération refusée : {e}")
else:
    print(f"Nouveau solde : {nouveau}€")

# ----------------------------------------------
# 6. GESTION GLOBALE DES EXCEPTIONS (DÉMONSTRATION)
# ----------------------------------------------
print("\n6️⃣ ATTRA-TOUT (AVEC PRÉCAUTION)")
print("-" * 40)

# Parfois, on veut éviter qu'un programme plante en production, mais il faut
# au moins journaliser l'erreur. On peut utiliser `except Exception as e:`
import traceback

try:
    # Code risqué
    eval("print(1 + )")  # SyntaxError volontaire
except Exception as e:
    print(f"Une erreur générique a été interceptée : {e}")
    # traceback.print_exc()  # Décommente pour voir la pile d'appels

# Note: éviter de capturer BaseException ou KeyboardInterrupt sans bonne raison.

# ----------------------------------------------
# 7. EXERCICE INTÉGRÉ : SAISIE UTILISATEUR ROBUSTE
# ----------------------------------------------
print("\n7️⃣ EXERCICE - SAISIE D'UN NOMBRE POSITIF")
print("-" * 40)

def demander_nombre_positif(message="Entrez un nombre positif : "):
    """
    Demande à l'utilisateur un nombre positif jusqu'à ce qu'il soit valide.
    Utilise try/except pour gérer les erreurs de conversion.
    """
    while True:
        reponse = input(message)
        try:
            valeur = float(reponse)
            if valeur <= 0:
                raise ValueError("Le nombre doit être strictement positif.")
            return valeur
        except ValueError as e:
            print(f"Saisie invalide : {e}. Réessayez.")

# Pour tester, décommentez la ligne suivante (nécessite une interaction)
# prix = demander_nombre_positif("Prix HT (>0) : ")
# print(f"Prix saisi : {prix}")

# Simulation d'une saisie valide
import io
import sys

# On simule l'entrée utilisateur avec un faux flux (sans interaction)
entrees_simulees = ["-10\n", "0\n", "abc\n", "42.5\n"]
original_stdin = sys.stdin
sys.stdin = io.StringIO("".join(entrees_simulees))

print("Simulation de saisie :")
try:
    prix = demander_nombre_positif("Prix HT (>0) : ")
    print(f"Prix validé : {prix}")
finally:
    sys.stdin = original_stdin  # Rétablir stdin

# ----------------------------------------------
# 8. BONUS : CONTEXTE DE FICHIER AVEC EXCEPTION
# ----------------------------------------------
print("\n8️⃣ BONUS - WITH ET GESTION D'ERREUR")
print("-" * 40)

# L'instruction `with` gère automatiquement la fermeture, même en cas d'erreur.
# On peut y ajouter un try/except pour les erreurs métier.
try:
    with open(dossier / "demo.txt", "r", encoding="utf-8") as f:
        contenu = f.read()
        # Simulation d'une erreur de traitement
        if "Ligne" not in contenu:
            raise ValueError("Le fichier ne contient pas le mot 'Ligne'.")
        print("Traitement du fichier OK.")
except FileNotFoundError:
    print("Fichier non trouvé.")
except ValueError as e:
    print(f"Erreur de contenu : {e}")
# Pas besoin de finally pour fermer le fichier, `with` l'a déjà fait.

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 19")
print("=" * 60)