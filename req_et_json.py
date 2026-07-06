import json
import requests
import os

# ----------------------------------------------
# 1. INTRODUCTION À JSON


print("1️⃣ INTRODUCTION À JSON")
print("-" * 40)
donnees_complexes = {
    "utilisateur": {
        "nom": "Bob",
        "age": 25,
        "adresse": {
            "rue": "123 Rue Principale",
            "ville": "Lyon",
            "code_postal": "69000"
        }
    },
    "hobbies": ["football", "cuisine", "voyage"], 
    "actif": True
}
chaine_json = json.dumps(donnees_complexes, indent=3, ensure_ascii=False)
print("Données Python :")
print(donnees_complexes)
print("Chaîne JSON :")
print(chaine_json)
json_reconverti = json.loads(chaine_json)
print("Données reconverties :")
print(json_reconverti)


# ----------------------------------------------
# 2. APPELS API ET JSON

print("\n2️⃣ APPELS API ET JSON")
print("-" * 40)
try:
    reponse = requests.get("https://jsonplaceholder.typicode.com/todos/1", timeout=10)
    reponse.raise_for_status()
    tache = reponse.json()
    print("Tâche récupérée depuis l'API :")
    print(tache)
except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}")
except json.JSONDecodeError as e:
    print(f"Erreur JSON : {e}")

# ----------------------------------------------
# 3. CRÉATION ET LECTURE DE FICHIERS JSON
print("\n3️⃣ CRÉATION ET LECTURE DE FICHIERS JSON")
print("-" * 40)
donnees_a_sauvegarder = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris"
}
with open("donnees.json", "w", encoding="utf-8") as f:
    json.dump(donnees_a_sauvegarder, f, indent=2, ensure_ascii=False)
print("Données sauvegardées dans 'donnees.json'.")
with open("donnees.json", "r", encoding="utf-8") as f:
    donnees_chargees = json.load(f)
print("Données chargées depuis 'donnees.json' :")
print(donnees_chargees)
os.remove("donnees.json")

# -----------------------------------------------
# 4. GESTION DES ERREURS DANS LES APPELS API
print("\n4️⃣ GESTION DES ERREURS DANS LES APPELS API")
print("-" * 40)

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"Erreur HTTP : {e}")
    except requests.exceptions.ConnectionError:
        print("Erreur de connexion.")
    except requests.exceptions.Timeout:
        print("La requête a expiré.")
    except requests.exceptions.RequestException as e:
        print(f"Erreur : {e}")
    return None


print("Test avec un utilisateur GitHub valide :")
utilisateur = get_github_user("princelompo")

if utilisateur:
    print(f"Nom d'utilisateur : {utilisateur['login']}")
    print(f"Nom complet : {utilisateur['name']}")
    print(f"Bio : {utilisateur['bio']}")
    print(f"Avatar : {utilisateur['avatar_url']}")
    print(f"Nombre de repos publics : {utilisateur['public_repos']}")
    print(f"Date de création : {utilisateur['created_at']}")
    print(f"Date de dernière mise à jour : {utilisateur['updated_at']}")
    print(f"URL du profil : {utilisateur['html_url']}")
    print(f"Site web : {utilisateur['blog']}")
    print(f"Nombre de followers : {utilisateur['followers']}")

else:
    print("Utilisateur non trouvé.")