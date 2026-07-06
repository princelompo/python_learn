# ==============================================
# JOUR 23 : DÉCORATEURS & FERMETURES (CLOSURES)
# ==============================================
# Thèmes du jour :
# 1. Fermetures (closures)
# 2. Décorateurs simples
# 3. Wrapper avec *args, **kwargs
# 4. Décorateurs avec paramètres
# 5. Préservation des métadonnées (functools.wraps)
# 6. Cas pratiques : log, cache, contrôle d'accès
# ==============================================

import time
from functools import wraps

print("=" * 60)
print("📘 LEÇON DU JOUR 23 - DÉCORATEURS & FERMETURES")
print("=" * 60)

# ----------------------------------------------
# 1. FERMETURES (CLOSURES)
# ----------------------------------------------
print("\n1️⃣ FERMETURES (CLOSURES)")
print("-" * 40)

def creer_multiplicateur(facteur):
    """Retourne une fonction qui multiplie par 'facteur'."""
    def multiplier(x):
        return x * facteur
    return multiplier

double = creer_multiplicateur(2)
triple = creer_multiplicateur(3);

print(f"Double de 5 = {double(5)}")
print(f"Triple de 5 = {triple(5)}")


# Exemple avec modification d'état (mot-clé nonlocal)
def creer_compteur():
    """Retourne une fonction qui incrémente un compteur interne."""
    compte = 0
    def incrementer():
        nonlocal compte
        compte += 1
        return compte
    return incrementer

mon_compteur = creer_compteur()
print(f"Compteur (appel 1) : {mon_compteur()}")
print(f"Compteur (appel 2) : {mon_compteur()}")
print(f"Compteur (appel 3) : {mon_compteur()}")

# ----------------------------------------------
# 2. DÉCORATEUR SIMPLE (SANS PARAMÈTRE)
# ----------------------------------------------
print("\n2️⃣ DÉCORATEUR SIMPLE")
print("-" * 40)

def souligner(fonction):
    """Décore une fonction en soulignant son résultat."""
    def wrapper(*args, **kwargs):
        resultat = fonction(*args, **kwargs)
        return f"{resultat}\n{'=' * len(str(resultat))}"
    return wrapper

@souligner
def saluer(nom):
    return f"Bonjour {nom}"

print(saluer("Alice"))

# Sans sucre syntaxique, c'est équivalent à :
# saluer = souligner(saluer)

# ----------------------------------------------
# 3. DÉCORATEUR AVEC *args, **kwargss
# ----------------------------------------------
print("\n3️⃣ DÉCORATEUR GÉNÉRIQUE (args, kwargs)")
print("-" * 40)

def journaliser(fonction):
    """Enregistre l'appel de la fonction avec ses arguments."""
    @wraps(fonction)  # Préserve __name__ et __doc__
    def wrapper(*args, **kwargs):
        print(f"🔍 Appel de {fonction.__name__} avec args={args}, kwargs={kwargs}")
        resultat = fonction(*args, **kwargs)
        print(f"✅ Résultat : {resultat}")
        return resultat
    return wrapper

@journaliser
def additionner(a, b):
    """Retourne la somme de deux nombres."""
    return a + b

print(additionner(3, 4))
print(f"Nom préservé : {additionner.__name__}")
print(f"Doc préservée : {additionner.__doc__}")

# ----------------------------------------------
# 4. DÉCORATEUR AVEC PARAMÈTRES
# ----------------------------------------------
print("\n4️⃣ DÉCORATEUR AVEC PARAMÈTRES")
print("-" * 40)

def repeter(n_fois):
    """Fabrique de décorateur : répète l'appel n fois."""
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            for i in range(n_fois):
                print(f"[{i+1}/{n_fois}]", end=" ")
                fonction(*args, **kwargs)
        return wrapper
    return decorateur

@repeter(3)
def dire_coucou():
    print("Coucou !")

dire_coucou()

# ----------------------------------------------
# 5. CAS PRATIQUE N°1 : CHRONOMÈTRE
# ----------------------------------------------
print("\n5️⃣ CAS PRATIQUE - CHRONOMÈTRE")
print("-" * 40)

def chronometrer(fonction):
    """Mesure et affiche le temps d'exécution d'une fonction."""
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        debut = time.perf_counter()
        resultat = fonction(*args, **kwargs)
        fin = time.perf_counter()
        print(f"⏱️ {fonction.__name__} exécutée en {fin - debut:.6f} secondes")
        return resultat
    return wrapper

@chronometrer
def calcul_long(n):
    """Simule un calcul long."""
    time.sleep(n)
    return n * 2

resultat = calcul_long(0.5)
print(f"Résultat = {resultat}")

# ----------------------------------------------
# 6. CAS PRATIQUE N°2 : MÉMOÏSATION (CACHE)
# ----------------------------------------------
print("\n6️⃣ CAS PRATIQUE - MÉMOÏSATION (CACHE)")
print("-" * 40)

def memoizer(fonction):
    """Cache les résultats de la fonction pour éviter les recalculs."""
    cache = {}
    @wraps(fonction)
    def wrapper(*args):
        if args not in cache:
            print(f"  Calcul pour {args}...")
            cache[args] = fonction(*args)
        else:
            print(f"  Résultat trouvé dans le cache pour {args}")
        return cache[args]
    return wrapper

@memoizer
def fib(n):
    """Calcule le n-ième nombre de Fibonacci (récursif)."""
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("Fibonacci(5) :")
print(f"Résultat = {fib(5)}")

print("\nFibonacci(10) (bénéficie du cache précédent) :")
print(f"Résultat = {fib(10)}")

# ----------------------------------------------
# 7. CAS PRATIQUE N°3 : CONTRÔLE D'ACCÈS
# ----------------------------------------------
print("\n7️⃣ CAS PRATIQUE - CONTRÔLE D'ACCÈS")
print("-" * 40)

# Simulation d'un utilisateur connecté ou non
utilisateur_connecte = True

def necessite_authentification(fonction):
    """Vérifie que l'utilisateur est connecté avant d'exécuter la fonction."""
    @wraps(fonction)
    def wrapper(*args, **kwargs):
        if not utilisateur_connecte:
            print("⛔ Accès refusé : utilisateur non connecté.")
            return None
        return fonction(*args, **kwargs)
    return wrapper

@necessite_authentification
def voir_secret():
    return "Le secret est : Python c'est génial !"

print(voir_secret())

# Test avec utilisateur déconnecté
utilisateur_connecte = False
print(voir_secret())

# ----------------------------------------------
# 8. EXERCICE INTÉGRÉ : VALIDATION DE PARAMÈTRES
# ----------------------------------------------
print("\n8️⃣ EXERCICE - DÉCORATEUR DE VALIDATION")
print("-" * 40)

def valider_types(*types_attendus):
    """
    Décorateur avec paramètres qui vérifie que les arguments
    positionnels sont du bon type.
    """
    def decorateur(fonction):
        @wraps(fonction)
        def wrapper(*args, **kwargs):
            if len(args) != len(types_attendus):
                raise TypeError(f"Nombre d'arguments incorrect (attendu {len(types_attendus)}, reçu {len(args)})")
            for i, (arg, type_attendu) in enumerate(zip(args, types_attendus)):
                if not isinstance(arg, type_attendu):
                    raise TypeError(f"Argument {i+1} : attendu {type_attendu.__name__}, reçu {type(arg).__name__}")
            return fonction(*args, **kwargs)
        return wrapper
    return decorateur

@valider_types(int, int)
def diviser(a, b):
    """Division sécurisée (a et b doivent être des entiers)."""
    if b == 0:
        raise ZeroDivisionError("Division par zéro")
    return a / b

# Tests
print(f"10 / 3 = {diviser(10, 3):.2f}")
try:
    diviser("dix", 3)
except TypeError as e:
    print(f"Erreur de type : {e}")

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 23")
print("=" * 60)

