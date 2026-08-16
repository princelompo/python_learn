import random
import time


print("Bienvenue dans le générateur de mots de passe !" \
      "nCe programme vous aidera à créer un mot de passe sécurisé en fonction de vos préférences.\n ")

chiffres = "0123456789"
majuscules = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minuscules = "abcdefghijklmnopqrstuvwxyz"
symboles = "!@#$%^&*()-_=+[]{}|;:,.<>?/"

print("Entrer votre mot de passe : ")
mot_de_passe = input("Mot de passe : ")

print("\nVérification de la sécurité du mot de passe...\n")
time.sleep(1)  # Pause pour simuler le traitement   
if len(mot_de_passe) < 8:
    print("Le mot de passe doit contenir au moins 8 caractères.")
elif not any(char in chiffres for char in mot_de_passe):
    print("Le mot de passe doit contenir au moins un chiffre.")
elif not any(char in majuscules for char in mot_de_passe):
    print("Le mot de passe doit contenir au moins une lettre majuscule.")
elif not any(char in minuscules for char in mot_de_passe):
    print("Le mot de passe doit contenir au moins une lettre minuscule.")
elif not any(char in symboles for char in mot_de_passe):
    print("Le mot de passe doit contenir au moins un symbole.")
else:
    print("Mot de passe valide !")
