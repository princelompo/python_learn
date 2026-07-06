print("=" * 60)
print("📘 LEÇON DU JOUR 20 - FONCTIONS AVANCÉES")
print("=" * 60)


# ----------------------------------------------
# Fonctions avec types indiqués

# Indication de types pour les arguments et le retour
def ajouter(a: int, b: int) -> int:
    return a + b

# ----------------------------------------------
# Décorateurs pour mesurer le temps d'exécution
from functools import wraps
import time
def mesurer_temps(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        debut = time.perf_counter()
        resultat = func(*args, **kwargs)
        fin = time.perf_counter()
        print(f"Temps d'exécution de {func.__name__} : {fin - debut:.4f} secondes")
        return resultat
    return wrapper

@mesurer_temps
def calculer_somme(n: int) -> int:
    return sum(range(n))

# fonction qui retourne une list 
def generer_carres(n: int) -> list:
    return [i**2 for i in range(n)]

# ----------------------------------------------

# Fonctionc qui retourne un dictionnaire

def compter_lettres(phrase: str) -> dict:
    compte = {}
    for lettre in phrase:
        if lettre.isalpha():
            lettre = lettre.lower()
            compte[lettre] = compte.get(lettre, 0) + 1
    return compte

# ----------------------------------------------

if __name__ == "__main__":
    print(f"3 + 5 = {ajouter(3, 5)}")
    print(f"Somme des nombres de 0 à 999999 : {calculer_somme(1000000)}")
    print(f"Carrés de 0 à 9 : {generer_carres(10)}")
    print(f"Compte des lettres dans 'Hello World!' : {compter_lettres('Hello World!')}")

