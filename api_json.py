# ==============================================
# JOUR 27 : APIS, REQUESTS & JSON
# ==============================================
# Thèmes du jour :
# 1. Requête GET et récupération de JSON
# 2. Codes de statut et gestion d'erreurs
# 3. Paramètres d'URL (params) et Headers
# 4. Requête POST avec envoi de données JSON
# 5. Manipulation de fichiers JSON locaux
# ==============================================

import requests
import json
import os

print("=" * 60)
print("📘 LEÇON DU JOUR 27 - APIS, REQUESTS & JSON")
print("=" * 60)

# ----------------------------------------------
# 1. REQUÊTE GET SIMPLE
# ----------------------------------------------
print("\n1️⃣ REQUÊTE GET (API CHUCK NORRIS)")
print("-" * 40)

try:
    reponse = requests.get("https://api.chucknorris.io/jokes/random", timeout=5)
    reponse.raise_for_status()
    blague = reponse.json()
    print(f"😄 Blague du jour : {blague['value']}")
except requests.exceptions.RequestException as e:
    print(f"Erreur : {e}")

# ----------------------------------------------
# 2. CODES DE STATUT ET EN-TÊTES
# ----------------------------------------------
print("\n2️⃣ CODES DE STATUT")
print("-" * 40)

reponse = requests.get("https://httpbin.org/status/404")
print(f"Statut d'une 404 : {reponse.status_code}")
print(f"Est-ce un succès ? {reponse.ok}")  # False

reponse_ok = requests.get("https://httpbin.org/get")
print(f"Statut d'un GET : {reponse_ok.status_code}")

# ----------------------------------------------
# 3. PARAMÈTRES D'URL ET HEADERS
# ----------------------------------------------
print("\n3️⃣ PARAMÈTRES D'URL")
print("-" * 40)

# Requête avec paramètres
reponse = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "python", "sort": "stars", "per_page": 3},
    timeout=10
)
if reponse.ok:
    donnees = reponse.json()
    print("Top 3 dépôts Python sur GitHub :")
    for repo in donnees["items"]:
        print(f"  ⭐ {repo['stargazers_count']} - {repo['full_name']}")
else:
    print("Impossible de contacter GitHub (peut-être rate limit).")

# ----------------------------------------------
# 4. REQUÊTE POST
# ----------------------------------------------
print("\n4️⃣ REQUÊTE POST (HTTPBIN)")
print("-" * 40)

donnees_a_envoyer = {"nom": "Alice", "langage": "Python", "niveau": "Intermédiaire"}
reponse = requests.post("https://httpbin.org/post", json=donnees_a_envoyer)
if reponse.ok:
    echo = reponse.json()
    print("Données renvoyées par le serveur :")
    print(json.dumps(echo["json"], indent=2, ensure_ascii=False))

# ----------------------------------------------
# 5. GESTION DES ERREURS
# ----------------------------------------------
print("\n5️⃣ GESTION ROBUSTE DES ERREURS")
print("-" * 40)

def recuperer_api(url, timeout=5):
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError:
        print("❌ Impossible de se connecter au serveur.")
    except requests.exceptions.Timeout:
        print("❌ La requête a expiré.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ Erreur HTTP : {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur inconnue : {e}")
    return None

# Test avec une URL invalide
print("Test avec une URL invalide :")
resultat = recuperer_api("https://api.inexistante12345.com")

# ----------------------------------------------
# 6. MANIPULATION DE FICHIERS JSON
# ----------------------------------------------
print("\n6️⃣ FICHIERS JSON LOCAUX")
print("-" * 40)

# Écriture
donnees_locales = [
    {"id": 1, "tache": "Apprendre Python", "faite": True},
    {"id": 2, "tache": "Apprendre les APIs", "faite": False},               
    {"id": 3, "tache": "Créer un projet", "faite": False}
]

chemin_fichier = "taches.json"
with open(chemin_fichier, "w", encoding="utf-8") as f:
    json.dump(donnees_locales, f, indent=2, ensure_ascii=False)
print(f"Fichier '{chemin_fichier}' créé.")

# Lecture
with open(chemin_fichier, "r", encoding="utf-8") as f:
    taches_chargees = json.load(f)

print("Tâches chargées :")
for t in taches_chargees:
    statut = "✅" if t["faite"] else "⬜"
    print(f"  {statut} [{t['id']}] {t['tache']}")

# Nettoyage du fichier
os.remove(chemin_fichier)

# ----------------------------------------------
# 7. CONVERSION DICT <-> CHAÎNE JSON
# ----------------------------------------------
print("\n7️⃣ CONVERSION DICT <-> JSON (dumps / loads)")
print("-" * 40)

produit = {"nom": "Ordinateur", "prix": 899.99, "stock": True}
chaine_json = json.dumps(produit, indent=2, ensure_ascii=False)
print("Dict -> chaîne JSON :")
print(chaine_json)

dict_reconverti = json.loads(chaine_json)
print(f"Chaîne JSON -> dict : {dict_reconverti}")

# ----------------------------------------------
# 8. EXERCICE INTÉGRÉ : MÉTÉO AVEC UNE API GRATUITE
# ----------------------------------------------
print("\n8️⃣ EXERCICE - API MÉTÉO (Open-Meteo, sans clé)")
print("-" * 40)

try:
    reponse = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": 48.8566,    # Paris
            "longitude": 2.3522,
            "current_weather": True
        },
        timeout=10
    )
    reponse.raise_for_status()
    meteo = reponse.json()
    courant = meteo["current_weather"]
    print(f"📍 Météo actuelle à Paris :")
    print(f"   🌡️ Température : {courant['temperature']}°C")
    print(f"   💨 Vent : {courant['windspeed']} km/h")
    print(f"   🔎 Code météo : {courant['weathercode']}")
except requests.exceptions.RequestException as e:
    print(f"Erreur météo : {e}")

print("=" * 60)
print("✅ FIN DE LA LEÇON DU JOUR 27")
print("=" * 60)

