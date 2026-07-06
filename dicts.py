# ==============================================
# JOUR 15 : DICTIONNAIRES & UTILISATION RÉELLE
# ==============================================
# Thèmes du jour :
# 1. Création et manipulation de base
# 2. Méthodes essentielles (get, items, keys, values, update)
# 3. Parcours et compréhensions
# 4. Cas pratiques : comptage, cache, configuration
# ==============================================

print("=" * 50)
print("📘 LEÇON DU JOUR 15 - DICTIONNAIRES")
print("=" * 50)

# ----------------------------------------------
# 1. CRÉATION ET ACCÈS
# ----------------------------------------------
print("\n1️⃣ CRÉATION ET ACCÈS DE BASE")
print("-" * 30)

# Création
personne = {
    "nom": "Martin",
    "prenom": "Sophie",
    "age": 28,
    "competences": ["Python", "SQL", "Git"],
    "adresse": {
        "rue": "15 Avenue des Champs",
        "code_postal": "75008"
    }
}

print(f"Dictionnaire personne : {personne}")
print(f"Nom complet : {personne['prenom']} {personne['nom']}")
print(f"Première compétence : {personne['competences'][0]}")
print(f"Ville : {personne['adresse']['code_postal']}")

# Ajout / Modification
personne["age"] = 29                     # Modification
personne["email"] = "sophie@email.com"   # Ajout
print(f"\nAprès modifications : {personne}")

# ----------------------------------------------
# 2. MÉTHODES DE SÉCURITÉ ET DE MANIPULATION
# ----------------------------------------------
print("\n2️⃣ MÉTHODES ESSENTIELLES")
print("-" * 30)

# .get() avec valeur par défaut
print(f"Téléphone (clé absente) : {personne.get('telephone', 'Non renseigné')}")
print(f"Email (clé présente) : {personne.get('email', 'Non renseigné')}")

# .pop() pour retirer et récupérer
age_supprime = personne.pop("age")
print(f"Âge supprimé : {age_supprime}")
print(f"Dictionnaire après pop : {personne}")

# Vérification d'appartenance
print(f"'nom' est-il dans le dictionnaire ? {'nom' in personne}")
print(f"'age' est-il dans le dictionnaire ? {'age' in personne}")

# ----------------------------------------------
# 3. PARCOURS DE DICTIONNAIRES
# ----------------------------------------------
print("\n3️⃣ PARCOURS ET ITÉRATION")
print("-" * 30)

print("Parcours des clés :")
for cle in personne:
    print(f"  {cle}")

print("\nParcours des valeurs :")
for valeur in personne.values():
    print(f"  {valeur}")

print("\nParcours clé + valeur (avec .items()) :")
for cle, valeur in personne.items():
    print(f"  {cle} -> {valeur}")

# ----------------------------------------------
# 4. FUSION DE DICTIONNAIRES
# ----------------------------------------------
print("\n4️⃣ FUSION ET MISE À JOUR")
print("-" * 30)

config_par_defaut = {"theme": "clair", "langue": "fr", "notifications": True}
config_utilisateur = {"theme": "sombre", "langue": "en"}

# Méthode 1 : .update()
config_finale = config_par_defaut.copy()  # On copie pour ne pas modifier l'original
config_finale.update(config_utilisateur)
print(f"Fusion avec .update() : {config_finale}")

# Méthode 2 : opérateur ** (Python 3.5+)
config_finale2 = {**config_par_defaut, **config_utilisateur}
print(f"Fusion avec ** : {config_finale2}")

# ----------------------------------------------
# 5. DICTIONNAIRES EN COMPRÉHENSION
# ----------------------------------------------
print("\n5️⃣ COMPRÉHENSIONS DE DICTIONNAIRES")
print("-" * 30)

# Carrés des 5 premiers entiers
carres = {x: x**2 for x in range(1, 6)}
print(f"Carrés : {carres}")

# Filtrer un dictionnaire
notes = {"Alice": 15, "Bob": 8, "Charlie": 12, "Diane": 19}
admis = {nom: note for nom, note in notes.items() if note >= 10}
print(f"Étudiants admis : {admis}")

# Inverser clés et valeurs (si valeurs uniques)
couleurs = {"rouge": "#FF0000", "vert": "#16A016", "bleu": "#0000FF"}
code_vers_couleur = {code: nom for nom, code in couleurs.items()}
print(f"Inversion : {code_vers_couleur}")

# ----------------------------------------------
# 6. CAS PRATIQUE N°1 : COMPTEUR D'OCCURRENCES
# ----------------------------------------------
print("\n6️⃣ CAS PRATIQUE - COMPTAGE D'ÉLÉMENTS")
print("-" * 30)

texte = "le python est un serpent le python est aussi un langage"
mots = texte.split()
frequences = {}

for mot in mots:
    # .get(mot, 0) retourne la valeur actuelle ou 0 si le mot n'existe pas encore
    frequences[mot] = frequences.get(mot, 0) + 1

print(f"Texte : '{texte}'")
print("Fréquence des mots :")
for mot, nb in sorted(frequences.items()):
    print(f"  '{mot}' : {nb} fois")

# ----------------------------------------------
# 7. CAS PRATIQUE N°2 : CACHE DE FONCTION (MÉMOÏSATION)
# ----------------------------------------------
print("\n7️⃣ CAS PRATIQUE - CACHE POUR OPTIMISATION")
print("-" * 30)

# Calcul de Fibonacci avec cache
cache_fibonacci = {}

def fibonacci(n):
    """Retourne le n-ième nombre de Fibonacci avec cache."""
    # Vérifier si déjà calculé
    if n in cache_fibonacci:
        print(f"  (valeur de F({n}) récupérée du cache)")
        return cache_fibonacci[n]
    
    # Cas de base
    if n <= 1:
        resultat = n
    else:
        resultat = fibonacci(n-1) + fibonacci(n-2)
    
    # Stocker dans le cache avant de retourner
    cache_fibonacci[n] = resultat
    return resultat

print("Calcul de F(6) :")
print(f"Résultat F(6) = {fibonacci(6)}")
print(f"Cache après calcul : {cache_fibonacci}")

# ----------------------------------------------
# 8. CAS PRATIQUE N°3 : DISPATCHER (REMPLACER IF/ELIF)
# ----------------------------------------------
print("\n8️⃣ CAS PRATIQUE - CONFIGURATION PAR DICTIONNAIRE")
print("-" * 30)

def action_demarrer():
    return "Système démarré"

def action_arreter():
    return "Système arrêté"

def action_redemarrer():
    return "Système redémarré"

# Dictionnaire d'actions
menu_actions = {
    "start": action_demarrer,
    "stop": action_arreter,
    "restart": action_redemarrer
}

# Simulation de commandes utilisateur
commandes_test = ["start", "restart", "stop", "help"]

for cmd in commandes_test:
    action = menu_actions.get(cmd)
    if action:
        resultat = action()
        print(f"Commande '{cmd}' : {resultat}")
    else:
        print(f"Commande '{cmd}' : Inconnue")

# ----------------------------------------------
# 9. EXERCICE INTÉGRÉ : GESTION DE STOCK
# ----------------------------------------------
print("\n9️⃣ EXERCICE - GESTION DE STOCK AVEC DICTIONNAIRE")
print("-" * 30)

stock = {
    "pommes": 10,
    "bananes": 5,
    "oranges": 8
}

def afficher_stock(stock_dict):
    print("État du stock :")
    for produit, quantite in stock_dict.items():
        print(f"  {produit} : {quantite} unités")

def ajouter_produit(stock_dict, produit, quantite):
    stock_dict[produit] = stock_dict.get(produit, 0) + quantite
    print(f"Ajout de {quantite} {produit}(s)")

def retirer_produit(stock_dict, produit, quantite):
    if produit not in stock_dict:
        print(f"Erreur : {produit} n'existe pas dans le stock")
        return
    if stock_dict[produit] < quantite:
        print(f"Erreur : stock insuffisant de {produit} (disponible : {stock_dict[produit]})")
        return
    stock_dict[produit] -= quantite
    if stock_dict[produit] == 0:
        del stock_dict[produit]  # Supprimer l'entrée si plus de stock
    print(f"Retrait de {quantite} {produit}(s)")

# Test du gestionnaire de stock
afficher_stock(stock)

print("\n--- Opérations ---")
ajouter_produit(stock, "pommes", 5)
ajouter_produit(stock, "kiwis", 12)
retirer_produit(stock, "bananes", 2)
retirer_produit(stock, "oranges", 10)  # Stock insuffisant
retirer_produit(stock, "oranges", 8)   # Retrait complet

print("\n--- Stock final ---")
afficher_stock(stock)

print("=" * 50)
print("✅ FIN DE LA LEÇON DU JOUR 15")
print("=" * 50)