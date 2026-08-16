# ==============================================
# JOUR 24 : GESTIONNAIRES DE CONTEXTE & WITH
# ==============================================
# Thèmes du jour :
# 1. Fonctionnement du with (__enter__, __exit__)
# 2. Gestionnaire de contexte personnalisé (classe)
# 3. Gestion des exceptions dans __exit__
# 4. Utilisation de contextlib.contextmanager
# 5. Cas pratiques : chronomètre, changement de répertoire
# ==============================================

import time
import os
from contextlib import contextmanager
from pathlib import Path

print("=" * 60)
print("📘 LEÇON DU JOUR 24 - GESTIONNAIRES DE CONTEXTE")
print("=" * 60)

# ----------------------------------------------
# 1. RAPPEL : WITH SUR UN FICHIER
# ----------------------------------------------
print("\n1️⃣ RAPPEL - WITH SUR UN FICHIER")
print("-" * 40)

tmp = Path("temp_jour24")
tmp.mkdir(exist_ok=True)

# ou temp = Path.m

# Écriture
with open(tmp / "demo.txt", "w", encoding="utf-8") as f:
    f.write("Ligne 1\nLigne 2\n")

# Lecture
with open(tmp / "demo.txt", "r", encoding="utf-8") as f:
    print("Contenu :\n", f.read())

# ----------------------------------------------
# 2. GESTIONNAIRE DE CONTEXTE AVEC UNE CLASSE
# ----------------------------------------------
print("\n2️⃣ GESTIONNAIRE DE CONTEXTE (CLASSE)")
print("-" * 40)

class Chrono:
    """Mesure le temps passé dans le bloc with."""
    
    def __enter__(self):
        print("⏱️ Chronomètre lancé")
        self.debut = time.perf_counter()
        return self  # L'objet retourné est assigné à la variable après 'as'
    
    def __exit__(self, _, __, ___):
        self.fin = time.perf_counter()
        duree = self.fin - self.debut
        print(f"⏱️ Temps écoulé : {duree:.4f} secondes")
        # Retourner False : les exceptions sont propagées normalement
        return False

with Chrono() as ch:
    time.sleep(1.2)
    print("Travail en cours...")

# ----------------------------------------------
# 3. GESTION DES EXCEPTIONS DANS __exit__
# ----------------------------------------------
print("\n3️⃣ GESTION DES EXCEPTIONS")
print("-" * 40)

class IgnorerZeroDivision:
    """Intercepte et supprime les ZeroDivisionError."""
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, _exc_val, _exc_tb):
        if exc_type is ZeroDivisionError:
            print(f"⚠️ Erreur interceptée : {exc_type.__name__}")
            return True  # Empêche la propagation
        return False  # Les autres erreurs se propagent

print("Test avec division par zéro :")
with IgnorerZeroDivision():
    resultat = 1 / 0
    print("Ceci ne s'affiche pas")  # Car l'exception est levée avant
print("✅ Le programme continue après le with.\n")

print("Test avec une autre erreur (TypeError) :")
try:
    with IgnorerZeroDivision():
        "2" + 2  # type: ignore[operator]  # TypeError, pas intercepté
except TypeError as e:
    print(f"❌ TypeError bien propagée : {e}")

# ----------------------------------------------
# 4. UTILISATION DE @contextmanager
# ----------------------------------------------
print("\n4️⃣ UTILISATION DE CONTEXTMANAGER (DÉCORATEUR)")
print("-" * 40)

@contextmanager
def chronometrer(etiquette="Action"):
    """Version générateur du chronomètre."""
    print(f"🟢 Début : {etiquette}")
    debut = time.perf_counter()
    try:
        yield  # Le contrôle passe au bloc with
    finally:
        fin = time.perf_counter()
        print(f"🔴 Fin : {etiquette} a duré {fin - debut:.4f} s")

with chronometrer("calcul complexe"):
    time.sleep(0.7)

# ----------------------------------------------
# 5. CAS PRATIQUE : CHANGEMENT TEMPORAIRE DE RÉPERTOIRE
# ----------------------------------------------
print("\n5️⃣ CAS PRATIQUE - CHANGEMENT DE RÉPERTOIRE")
print("-" * 40)

@contextmanager
def changer_repertoire(chemin):
    """Entre temporairement dans un répertoire, puis revient."""
    ancien = os.getcwd()
    os.chdir(chemin)
    try:
        yield
    finally:
        os.chdir(ancien)

dossier_temp = tmp.absolute()
print(f"Avant : {os.getcwd()}")
with changer_repertoire(dossier_temp):
    print(f"Pendant : {os.getcwd()}")
print(f"Après : {os.getcwd()}")

# ----------------------------------------------
# 6. CAS PRATIQUE : CONNEXION SIMULÉE À UNE BASE
# ----------------------------------------------
print("\n6️⃣ CAS PRATIQUE - CONNEXION SIMULÉE")
print("-" * 40)

class ConnexionBD:
    """Simule une connexion à une base de données."""
    def __init__(self, nom_bd):
        self.nom_bd = nom_bd
        self.connectee = False
    
    def connecter(self):
        print(f"🔌 Connexion à la base {self.nom_bd}...")
        self.connectee = True
    
    def fermer(self):
        print(f"🔌 Fermeture de la connexion à {self.nom_bd}")
        self.connectee = False
    
    def executer(self, requete):
        if not self.connectee:
            raise RuntimeError("Pas de connexion")
        print(f"  📋 Exécution : {requete}")
        return "résultat"

class SessionBD:
    """Gestionnaire de contexte pour une session de base de données."""
    def __init__(self, nom_bd):
        self.connexion = ConnexionBD(nom_bd)
    
    def __enter__(self):
        self.connexion.connecter()
        return self.connexion
    
    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self.connexion.fermer()
        return False

with SessionBD("ma_base") as db:
    db.executer("SELECT * FROM utilisateurs")
    db.executer("UPDATE compteurs SET valeur = 42")

# ----------------------------------------------
# 7. EXERCICE INTÉGRÉ : SAUVEGARDE ET RESTAURATION
# ----------------------------------------------
print("\n7️⃣ EXERCICE - SAUVEGARDE/RESTAURATION D'ATTRIBUT")
print("-" * 40)

class Mutable:
    """Un objet avec un attribut modifiable."""
    def __init__(self, valeur):
        self.valeur = valeur

@contextmanager
def sauver_restaurer(obj, attribut):
    """Sauvegarde la valeur d'un attribut et la restaure après le bloc."""
    original = getattr(obj, attribut)
    print(f"  Sauvegarde de {attribut}={original}")
    try:
        yield
    finally:
        setattr(obj, attribut, original)
        print(f"  Restauration de {attribut}={original}")

objet = Mutable(10)
print(f"Valeur initiale : {objet.valeur}")

with sauver_restaurer(objet, "valeur"):
    objet.valeur = 999
    print(f"  Pendant le bloc : {objet.valeur}")

print(f"Après le bloc : {objet.valeur}")

# ----------------------------------------------
# 8. NETTOYAGE
# ----------------------------------------------
import shutil
shutil.rmtree(tmp)

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 24")
print("=" * 60)
