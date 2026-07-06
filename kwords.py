# ==============================================
# JOUR 12 : ARGUMENTS AVANCÉS EN PYTHON
# ==============================================
# Thèmes du jour :
# 1. Valeurs par défaut
# 2. *args (nombre variable d'arguments positionnels)
# 3. **kwargs (nombre variable d'arguments nommés)
# ==============================================

print("=" * 50)
print("📘 LEÇON DU JOUR 12")
print("=" * 50)

# ----------------------------------------------
# 1. VALEURS PAR DÉFAUT
# ----------------------------------------------
print("\n1️⃣ VALEURS PAR DÉFAUT")
print("-" * 30)

def presenter_personne(nom, age, ville="Non précisée"):
    """
    Affiche les informations d'une personne.
    Si la ville n'est pas fournie, elle prend la valeur 'Non précisée'.
    """
    print(f"Nom : {nom}")
    print(f"Age : {age} ans")
    print(f"Ville : {ville}")
    print()  # Ligne vide pour aérer

# Test avec et sans valeur par défaut
print(">>> Test 1 : Ville fournie")
presenter_personne("Sophie", 28, "Lyon")

print(">>> Test 2 : Ville omise (valeur par défaut utilisée)")
presenter_personne("Marc", 35)

# ----------------------------------------------
# 2. *ARGS (Arguments Positionnels Variables)
# ----------------------------------------------
print("\n2️⃣ *ARGS - Nombre variable d'arguments")
print("-" * 30)

def calculer_moyenne(*notes):
    """
    Calcule la moyenne d'un nombre quelconque de notes.
    *notes devient un tuple contenant tous les arguments fournis.
    """
    if len(notes) == 0:
        return 0  # Évite la division par zéro
    
    print(f"Notes reçues : {notes} (type : {type(notes).__name__})")
    somme = sum(notes)       # sum() est une fonction native qui additionne un iterable
    nombre = len(notes)      # len() donne le nombre d'éléments
    moyenne = somme / nombre
    return moyenne

# Tests avec différents nombres d'arguments
print(f">>> Moyenne (3 notes) : {calculer_moyenne(12, 15, 18):.2f}")
print(f">>> Moyenne (5 notes) : {calculer_moyenne(10, 11, 9, 14, 16):.2f}")
print(f">>> Moyenne (0 note)  : {calculer_moyenne()}")

# Autre exemple classique : concaténer des chaînes
def assembler_mots(*mots, separateur=" "):
    """Assemble un nombre variable de mots avec un séparateur."""
    return separateur.join(mots)

print(f">>> Phrase assemblée : '{assembler_mots('Python', 'est', 'puissant')}'")

# ----------------------------------------------
# 3. **KWARGS (Arguments Nommés Variables)
# ----------------------------------------------
print("\n3️⃣ **KWARGS - Arguments nommés variables")
print("-" * 30)

def creer_fiche_produit(nom_produit, **caracteristiques):
    """
    Crée une fiche produit avec des caractéristiques flexibles.
    **caracteristiques devient un dictionnaire.
    """
    print(f"📦 Produit : {nom_produit}")
    print(f"   Type de l'objet reçu : {type(caracteristiques).__name__}")
    
    if caracteristiques:
        print("   Caractéristiques :")
        for cle, valeur in caracteristiques.items():
            print(f"      • {cle} : {valeur}")
    else:
        print("   (Aucune caractéristique fournie)")
    print()

# Tests
print(">>> Test 1 : Plusieurs caractéristiques")
creer_fiche_produit("Ordinateur Portable", 
                    marque="Dell", 
                    RAM="16 Go", 
                    Stockage="512 Go SSD", 
                    Prix="899€")

print(">>> Test 2 : Aucune caractéristique")
creer_fiche_produit("Stylo")

# ----------------------------------------------
# 4. COMBINAISON DES TROIS CONCEPTS
# ----------------------------------------------
print("\n4️⃣ COMBINAISON COMPLÈTE")
print("-" * 30)

def fonction_demo_complete(nom, age=18, *competences, **details):
    """
    Démonstration de l'ordre des paramètres :
    1. Paramètres normaux obligatoires
    2. Paramètres avec valeurs par défaut
    3. *args
    4. **kwargs
    """
    print(f"👤 Nom : {nom}")
    print(f"🎂 Âge : {age}")
    
    if competences:
        print(f"🛠️ Compétences : {', '.join(competences)}")
    
    if details:
        print("📋 Détails supplémentaires :")
        for cle, valeur in details.items():
            print(f"   {cle} : {valeur}")
    print()

# Test
fonction_demo_complete("Alice",           # Paramètre obligatoire
                       25,                # Écrase la valeur par défaut 'age'
                       "Python", "SQL", "Git",  # *args
                       ville="Paris",     # Début de **kwargs
                       poste="Développeuse",
                       teletravail=True)

# Ici on utilise la valeur par défaut pour 'age' (18)
fonction_demo_complete("Bob", 
                       "JavaScript", "React",  # *args
                       ville="Bordeaux",       # **kwargs
                       niveau="Junior")

# ----------------------------------------------
# 5. EXERCICE PRATIQUE INTÉGRÉ
# ----------------------------------------------
print("\n5️⃣ EXERCICE : Gestionnaire de Commandes Flexible")
print("-" * 30)

def passer_commande(client, *articles, **options):
    """
    Simule une commande dans un restaurant.
    - client : nom du client (obligatoire)
    - *articles : liste des plats commandés
    - **options : options spéciales (sur place/emporter, remarques...)
    """
    print(f"🧾 Commande pour : {client}")
    
    if articles:
        print("   🍽️ Articles commandés :")
        for i, article in enumerate(articles, start=1):
            print(f"      {i}. {article}")
    else:
        print("   ⚠️ Aucun article commandé !")
    
    if options:
        print("   ⚙️ Options :")
        for option, valeur in options.items():
            print(f"      • {option} : {valeur}")
    
    total_estime = len(articles) * 12  # Prix fictif
    print(f"   💶 Total estimé : {total_estime}€")
    print()

# Simulations de commandes
passer_commande("Marie", 
                "Pizza Margherita", "Salade César", "Tiramisu",
                type_service="Sur place",
                remarque="Sans gluten pour la salade")

passer_commande("Pierre",
                "Burger", "Frites",
                type_service="À emporter",
                paiement="Carte bancaire")

passer_commande("Lucie",
                type_service="Sur place",
                remarque="Juste un café, svp")

print("=" * 50)
print("✅ FIN DE LA LEÇON DU JOUR 12")
print("=" * 50)