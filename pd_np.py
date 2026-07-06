# ==============================================
# JOUR 26 : NUMPY & PANDAS – BASES
# ==============================================
# Thèmes du jour :
# 1. Tableaux NumPy (création, shape, dtype, slicing)
# 2. Opérations vectorisées
# 3. Masques booléens et reshaping
# 4. Pandas : Series et DataFrame
# 5. Sélection, filtrage, loc/iloc
# 6. Nettoyage (NaN) et groupby
# ==============================================

import numpy as np
import pandas as pd

print("=" * 60)
print("📘 LEÇON DU JOUR 26 - NUMPY & PANDAS")
print("=" * 60)

# ----------------------------------------------
# 1. CRÉATION DE TABLEAUX NUMPY
# ----------------------------------------------
print("\n1️⃣ CRÉATION DE TABLEAUX")
print("-" * 40)

a = np.array([1, 2, 3, 4, 5])
print(f"Liste -> array : {a}")

zeros = np.zeros((2, 3))
print(f"Zéros 2x3 :\n{zeros}")

ones = np.ones((2, 2))
print(f"Uns 2x2 :\n{ones}")

arange = np.arange(0, 10, 2)
print(f"arange(0,10,2) : {arange}")

linspace = np.linspace(0, 1, 5)
print(f"linspace(0,1,5) : {linspace}")

aleatoire = np.random.rand(2, 3)
print(f"Aléatoire 2x3 :\n{aleatoire}")

# ----------------------------------------------
# 2. PROPRIÉTÉS DES TABLEAUX
# ----------------------------------------------
print("\n2️⃣ PROPRIÉTÉS (shape, ndim, dtype, size)")
print("-" * 40)

mat = np.arange(12).reshape(3, 4)
print(f"Matrice 3x4 :\n{mat}")
print(f"Shape : {mat.shape}")
print(f"Dimensions : {mat.ndim}")
print(f"Type : {mat.dtype}")
print(f"Taille : {mat.size}")

# ----------------------------------------------
# 3. OPÉRATIONS VECTORISÉES
# ----------------------------------------------
print("\n3️⃣ OPÉRATIONS VECTORISÉES")
print("-" * 40)

x = np.array([1, 2, 3])
y = np.array([10, 20, 30])

print(f"x = {x}")
print(f"y = {y}")
print(f"x + y = {x + y}")
print(f"x * y = {x * y}")
print(f"x ** 2 = {x ** 2}")
print(f"sqrt(x) = {np.sqrt(x)}")
print(f"sum(x) = {np.sum(x)}")
print(f"mean(x) = {np.mean(x)}")

# ----------------------------------------------
# 4. MASQUES BOOLÉENS ET FILTRAGE
# ----------------------------------------------
print("\n4️⃣ MASQUES BOOLÉENS")
print("-" * 40)

valeurs = np.array([5, 12, 8, 21, 3, 15])
print(f"Tableau : {valeurs}")
print(f"valeurs > 10 : {valeurs > 10}")
print(f"Éléments > 10 : {valeurs[valeurs > 10]}")

# ----------------------------------------------
# 5. PANDAS – SERIES
# ----------------------------------------------
print("\n5️⃣ PANDAS SERIES")
print("-" * 40)

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(f"Series :\n{s}")
print(f"Élément 'b' : {s['b']}")
print(f"Opérations : {s * 2}")

# ----------------------------------------------
# 6. PANDAS – DATAFRAME
# ----------------------------------------------
print("\n6️⃣ DATAFRAME")
print("-" * 40)

df = pd.DataFrame({
    'Nom': ['Alice', 'Bob', 'Charlie', 'Diane'],
    'Âge': [25, 30, 35, 28],
    'Ville': ['Paris', 'Lyon', 'Marseille', 'Paris'],
    'Score': [88, 92, 79, 95]
})
print(df)

# Inspection
print(f"\nShape : {df.shape}")
print(f"Colonnes : {list(df.columns)}")
print("\nStatistiques :")
print(df.describe())

# ----------------------------------------------
# 7. SÉLECTION ET FILTRAGE
# ----------------------------------------------
print("\n7️⃣ SÉLECTION ET FILTRAGE")
print("-" * 40)

print(f"Colonne 'Nom' :\n{df['Nom']}")
print(f"\nColonnes 'Nom' et 'Score' :\n{df[['Nom', 'Score']]}")

# Filtrage
majeurs = df[df['Âge'] >= 30]
print(f"\nPersonnes >= 30 ans :\n{majeurs}")

parisiens = df[df['Ville'] == 'Paris']
print(f"\nParisiens :\n{parisiens}")

# loc et iloc
print(f"\nloc[2] (ligne index 2) :\n{df.loc[2]}")
print(f"iloc[0, 1] (ligne0 col1) : {df.iloc[0, 1]}")

# ----------------------------------------------
# 8. MODIFICATIONS ET COLONNES CALCULÉES
# ----------------------------------------------
print("\n8️⃣ COLONNES CALCULÉES")
print("-" * 40)

df['Double_Score'] = df['Score'] * 2
df['Excellent'] = df['Score'] >= 90
print(df)

# ----------------------------------------------
# 9. VALEURS MANQUANTES
# ----------------------------------------------
print("\n9️⃣ GESTION DES NaN")
print("-" * 40)

df2 = df.copy()
df2.loc[1, 'Score'] = None
df2.loc[3, 'Ville'] = None
print("DataFrame avec NaN :")
print(df2)
print("\nNaN détectés :")
print(df2.isna())
print("\nAprès fillna :")
print(df2.fillna({'Score': 0, 'Ville': 'Inconnue'}))

# ----------------------------------------------
# 10. GROUPBY
# ----------------------------------------------
print("\n🔟 GROUPBY")
print("-" * 40)

print("Moyenne des scores par ville :")
print(df.groupby('Ville')['Score'].mean())

print("\nÂge max par ville :")
print(df.groupby('Ville')['Âge'].max())

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 26")
print("=" * 60)  