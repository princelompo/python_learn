# ==============================================
# JOUR 22 : ITÉRATEURS VS GÉNÉRATEURS (DEEP DIVE)
# ==============================================
# Thèmes du jour :
# 1. Protocole itérateur (__iter__, __next__)
# 2. Création d'un itérateur personnalisé
# 3. Fonctions génératrices avec yield
# 4. Comparaison itérateur vs générateur
# 5. Utilisation manuelle de iter() et next()
# ==============================================

print("=" * 60)
print("📘 LEÇON DU JOUR 22 - ITÉRATEURS & GÉNÉRATEURS (DEEP DIVE)")
print("=" * 60)

# ----------------------------------------------
# 1. PROTOCOLE ITÉRATEUR : THÉORIE ET EXEMPLE SIMPLE
# ----------------------------------------------
print("\n1️⃣ PROTOCOLE ITÉRATEUR")
print("-" * 40)

class Compteur:
    """Itérateur personnalisé : compte de 'debut' à 'fin' (exclu)."""
    def __init__(self, debut, fin):
        self.valeur = debut
        self.fin = fin
        self.tours = 0
    
    def __iter__(self):
        """Retourne l'itérateur (l'objet lui-même)."""
        print("  -> __iter__ appelé")
        return self
    
    def __next__(self):
        """Retourne la valeur suivante ou lève StopIteration."""
        if self.valeur >= self.fin:
            print(f"  -> StopIteration levée après {self.tours} tours")
            raise StopIteration
        actuel = self.valeur
        self.valeur += 1
        self.tours += 1
        return actuel

print("Parcours avec for :")
for n in Compteur(10, 13):
    print(f"  Valeur : {n}")

# L'objet ne peut pas être réutilisé
print("\nUn itérateur ne peut être parcouru qu'une fois :")
c = Compteur(1, 3)
print(list(c))  # [1, 2]
print(list(c))  # [] (déjà épuisé)

# ----------------------------------------------
# 2. GÉNÉRATEUR : FONCTION AVEC yield
# ----------------------------------------------
print("\n2️⃣ FONCTION GÉNÉRATRICE (yield)")
print("-" * 40)

def compteur_gen(debut, fin):
    """Générateur équivalent au Compteur précédent."""
    while debut < fin:
        yield debut
        debut += 1

print("Parcours du générateur :")
for n in compteur_gen(10, 13):
    print(f"  Valeur : {n}")

# Usage manuel
gen = compteur_gen(100, 103)
print(f"Type du générateur : {type(gen)}")
print(f"next() -> {next(gen)}")
print(f"next() -> {next(gen)}")
print(f"next() -> {next(gen)}")
# print(next(gen))  # StopIteration

# ----------------------------------------------
# 3. COMPARAISON DÉTAILLÉE
# ----------------------------------------------
print("\n3️⃣ ITÉRATEUR vs GÉNÉRATEUR : COMPARAISON")
print("-" * 40)

# Itérateur avec état complexe
class FibonacciIterator:
    """Itérateur de la suite de Fibonacci jusqu'à une limite max."""
    def __init__(self, max_terme):
        self.a, self.b = 0, 1
        self.max = max_terme
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.a > self.max:
            raise StopIteration
        valeur = self.a
        self.a, self.b = self.b, self.a + self.b
        return valeur

print("Fibonacci (itérateur) jusqu'à 50 :")
print(list(FibonacciIterator(50)))

# Générateur équivalent (beaucoup plus simple)
def fibonacci_gen(max_terme):
    a, b = 0, 1
    while a <= max_terme:
        yield a
        a, b = b, a + b

print("Fibonacci (générateur) jusqu'à 50 :")
print(list(fibonacci_gen(50)))

# ----------------------------------------------
# 4. INSPECTION MANUELLE AVEC iter() ET next()
# ----------------------------------------------
print("\n4️⃣ UTILISATION MANUELLE DE iter() ET next()")
print("-" * 40)

# Itérable standard
fruits = ["pomme", "poire", "cerise"]
it = iter(fruits)
print(f"Type de l'itérateur : {type(it)}")

try:
    while True:
        print(f"  fruit : {next(it)}")
except StopIteration:
    print("  Fin de la liste.")

# Avec un générateur (même comportement)
gen = (x**2 for x in range(3))
print("Carrés via next() :")
print(next(gen))
print(next(gen))
print(next(gen))

# ----------------------------------------------
# 5. CAS PRATIQUE : LECTURE PAR LOTS D'UN GROS FICHIER
# ----------------------------------------------
print("\n5️⃣ EXEMPLE CONCRET - ITÉRATEUR DE FICHIER PAR LOTS")
print("-" * 40)

class LignesParLots:
    """Itérateur qui lit un fichier par blocs de N lignes."""
    def __init__(self, chemin, taille_lot):
        self.chemin = chemin
        self.taille_lot = taille_lot
        self.fichier = None
    
    def __enter__(self):
        """Prépare la ressource lors de l'appel à 'with'."""
        self.fichier = open(self.chemin, "r", encoding="utf-8")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Assure la fermeture propre de la ressource."""
        if self.fichier:
            self.fichier.close()
            print(f"  -> Fichier {self.chemin.name} fermé proprement.")

    def __iter__(self):
        return self
    
    def __next__(self):
        lot = []
        for _ in range(self.taille_lot):
            ligne = self.fichier.readline()
            if not ligne:
                break
            lot.append(ligne.strip())
        if not lot:
            raise StopIteration
        return lot

# Création d'un fichier de test
from pathlib import Path
tmp = Path("temp_jour22")
tmp.mkdir(exist_ok=True)
fichier_test = tmp / "donnees.txt"
with open(fichier_test, "w", encoding="utf-8") as f:
    for i in range(1, 11):
        f.write(f"Ligne numéro {i}\n")

print(f"Fichier de test : {fichier_test}")
print("Lecture par lots avec Context Manager :")
with LignesParLots(fichier_test, 3) as lecteur:
    for lot in lecteur:
        print(f"  Lot : {lot}")

# Équivalent avec un générateur (plus pythonique)
def lire_par_lots(chemin, taille_lot):
    with open(chemin, "r", encoding="utf-8") as f:
        while True:
            lot = [f.readline().strip() for _ in range(taille_lot) if f.readline()]
            if not lot:
                break
            yield lot

print("Même chose avec le générateur :")
for lot in lire_par_lots(fichier_test, 3):
    print(f"  Lot : {lot}")

# Nettoyage
import shutil
shutil.rmtree(tmp)

# ----------------------------------------------
# 6. EXERCICE INTÉGRÉ : PARCOURS DE DICTIONNAIRE ORDONNÉ
# ----------------------------------------------
print("\n6️⃣ EXERCICE - ITÉRATEUR DE DICTIONNAIRE TRIÉ")
print("-" * 40)

class SortedDictIterator:
    """Itérateur qui parcourt un dictionnaire par clés triées."""
    def __init__(self, data):
        self.data = data
        self.cles = sorted(data.keys())
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.cles):
            raise StopIteration
        cle = self.cles[self.index]
        valeur = self.data[cle]
        self.index += 1
        return cle, valeur

donnees = {"zèbre": 3, "abeille": 5, "chat": 2, "baleine": 8}
print("Dictionnaire original :", donnees)
print("Parcours trié par clés :")
for cle, val in SortedDictIterator(donnees):
    print(f"  {cle} -> {val}")

# Équivalent générateur
def sorted_dict_gen(data):
    for cle in sorted(data.keys()):
        yield cle, data[cle]

print("Via générateur :")
for cle, val in sorted_dict_gen(donnees):
    print(f"  {cle} -> {val}")

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 22")
print("=" * 60) 