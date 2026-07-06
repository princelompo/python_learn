from functools import reduce

print("="*60)
print("LECON DU JOUR : FONCTIONS LAMBDAS, REDUCE, FILTER ET MAP")  
print("="*60)

# ----------------------------------------------
# 1. FONCTIONS LAMBDAS
print("\n1️⃣ FONCTIONS LAMBDAS")
print("-"*30)

def carre(x):
    return x * x
# Version lambda de la fonction carre
carre_lambda = lambda x: x * x

def ajouter(a, b):
    return a + b
# Version lambda de la fonction ajouter
ajouter_lambda = lambda a, b: a + b

def est_pair(n):
    return n % 2 == 0
# Version lambda de la fonction est_pair
est_pair_lambda = lambda n: n % 2 == 0

# ----------------------------------------------

print(f"Carre de 5 (fonction normale) : {carre(5)}")
print(f"Carre de 5 (fonction lambda) : {carre_lambda(5)}")
print(f"Addition de 3 et 4 (fonction normale) : {ajouter(3, 4)}")
print(f"Addition de 3 et 4 (fonction lambda) : {ajouter_lambda(3, 4)}")
print(f"Est-ce que 10 est pair ? (fonction normale) : {est_pair(10)}")
print(f"Est-ce que 10 est pair ? (fonction lambda) : {est_pair_lambda(10)}")

# ----------------------------------------------

print("\n2️⃣ FONCTION REDUCE, FILTER ET MAP")
print("-"*30)

malist = [n for n in range(60) if n%4 == 0]
print(f"Liste de départ : {malist}")

# Utilisation de reduce pour calculer le produit de tous les éléments de la liste
produit = reduce(lambda x, y: x * y, malist[1:])  # On commence à partir du deuxième élément pour éviter de multiplier par 0
print(f"Produit des éléments de la liste : {produit}")

# Utilisation de filter pour ne garder que les éléments divisibles par 3
div3 = list(filter(lambda x: x % 3 == 0, malist))
print(f"Elements divisibles par 3 : {div3}")
  
# Utilisation de map pour doubler chaque élément de la liste
double = list(map(lambda x: x * 2, malist))
print(f"Elements doublés : {double}")

#combinaison de filter et map : doubler les éléments divisibles par 3
double_div3 = list(map(lambda x: x * 2, filter(lambda x: x % 3 == 0, malist)))
print(f"Elements divisibles par 3 et doublés : {double_div3}")

# ----------------------------------------------

print("FIN DE LA LEÇON DU JOUR ")