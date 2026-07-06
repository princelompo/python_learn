print("=" * 70)
print("=============📘 LEÇON DU JOUR 16 - TRIER MES FICHIERS ================")
print("=" * 70)

# ----------------------------------------------
# 1. LISTE DES FICHIERS DANS UN DOSSIER
# ----------------------------------------------
import os
import shutil
from pathlib import Path
import time
from datetime import datetime
from functools import wraps

dossier = Path.cwd()

# ----------------------------------------------
def measure_time(func):
    """Décorateur qui mesure et affiche le temps d'exécution d'une fonction."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        resultat = func(*args, **kwargs)
        end = time.time()
        print(f"\nTemps d'exécution de '{func.__name__}' : {end - start:.4f} s \n")
        return resultat
    return wrapper

@measure_time
def trier_choisir():
    print("\n ENTRER LE CRITÈRE DE TRI \n")
    print("1. Par nom (ordre alphabétique)")
    print("2. Par taille (du plus petit au plus grand)")
    print("3. Par date de modification (du plus ancien au plus récent)")
    print("4. Par extension (ordre alphabétique)")
    print("5. Par nom (ordre alphabétique inversé)")
    print("6. Par taille (du plus grand au plus petit)")
    print("7. Par date de modification (du plus récent au plus ancien)")
    print("8. Par extension (ordre alphabétique inversé)")

    choix = input("Votre choix (1-8) : ")

    fichiers =  [f for f in dossier.iterdir() if f.is_file()]
    dossiers = [d for d in dossier.iterdir() if d.is_dir()]

    if choix == "1":
        fichiers_tries = sorted(fichiers, key=lambda f: f.name.lower())
        dossiers_tries = sorted(dossiers, key=lambda d: d.name.lower())
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR NOM :")
            print("-" * 70)
            for f in fichiers_tries:
                print(f.name)
        if dossiers_tries:
            print("\n📁 DOSSIERS TRIES PAR NOM :")
            print("-" * 70)
            for d in dossiers_tries:
                print(d.name)
    
    elif choix == "2":
        fichiers_tries = sorted(fichiers, key=lambda f: f.stat().st_size)
        dossiers_tries = sorted(dossiers, key=lambda d: d.stat().st_size)
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR TAILLE (du plus petit au plus grand) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'TAILLE (KILOOCTETS)':15}")
            print("-" * 70)
            for f in fichiers_tries:
                print(f"{f.name:50} | {f.stat().st_size/(1024):10.2f} Ko ")
        if dossiers_tries:
            print("\n📁 DOSSIERS TRIES PAR TAILLE (du plus petit au plus grand) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'TAILLE (KILOOCTETS)':15}")
            print("-" * 70)
            for d in dossiers_tries:
                print(f"{d.name:50} | {d.stat().st_size/(1024):10.2f} Ko ")
        
    elif choix == "3":
        fichiers_tries = sorted(fichiers, key=lambda f: f.stat().st_mtime)
        dossiers_tries = sorted(dossiers, key=lambda d: d.stat().st_mtime)
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR DATE DE MODIFICATION (du plus ancien au plus récent) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'DERNIÈRE MODIFICATION':15}")
            print("-" * 70)
            for f in fichiers_tries:
                date_modif = f.stat().st_mtime
                redable_time = datetime.fromtimestamp(date_modif).strftime('%Y-%M-%D %H:%M:%S')
                print(f"{f.name:50} | {redable_time:15}")
        if dossiers_tries:
            print("\n📁 DOSSIERS TRIES PAR DATE DE MODIFICATION (du plus ancien au plus récent) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'DERNIÈRE MODIFICATION':15}")
            print("-" * 70)
            for d in dossiers_tries:
                date_modif = d.stat().st_mtime
                redable_time = datetime.fromtimestamp(date_modif).strftime('%Y-%M-%D %H:%M:%S')
                print(f"{d.name:50} | {redable_time:15}")
        
    elif choix == "4":
        fichiers_tries = sorted(fichiers, key=lambda f: f.suffix.lower())
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR EXTENSION :")
            print("-" * 70)
            for f in fichiers_tries:
                print(f.name)
        
    elif choix == "5":
        dossiers_tries = sorted(dossiers, key=lambda d: d.name.lower(), reverse=True)
        fichiers_tries = sorted(fichiers, key=lambda f: f.name.lower(), reverse=True)
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR NOM (ordre alphabétique inversé) :")
            print("-" * 70)
            for f in fichiers_tries:
                print(f.name)
        if dossiers_tries:
            print("\n📁 DOSSIERS TRIES PAR NOM (ordre alphabétique inversé) :")
            print("-" * 70)
            for d in dossiers_tries:
                print(d.name)
        
    elif choix == "6":
        fichiers_tries = sorted(fichiers, key=lambda f: f.stat().st_size, reverse=True)
        dossiers_tries = sorted(dossiers, key=lambda d: d.stat().st_size, reverse=True)
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR TAILLE (du plus grand au plus petit) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'TAILLE (KILOOCTETS)':15}")
            print("-" * 70)
            for f in fichiers_tries:
                print(f"{f.name:50} | {f.stat().st_size/(1024):10.2f} Ko")
        if dossiers_tries:
            print("\n📁 DOSSIERS TRIES PAR TAILLE (du plus grand au plus petit) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'TAILLE (KILOOCTETS)':15}")
            print("-" * 70)
            for d in dossiers_tries:
                print(f"{d.name:50} | {d.stat().st_size/(1024):10.2f} Ko")
        
    elif choix == "7":
        fichiers_tries = sorted(fichiers, key=lambda f: f.stat().st_mtime, reverse=True)
        dossiers_tries = sorted(dossiers, key=lambda d: d.stat().st_mtime, reverse=True)
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR DATE DE MODIFICATION (du plus récent au plus ancien) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'DERNIÈRE MODIFICATION':15}")
            print("-" * 70)
            for f in fichiers_tries:
                date_modif = f.stat().st_mtime
                redable_time = datetime.fromtimestamp(date_modif).strftime('%Y-%M-%D %H:%M:%S')
                print(f"{f.name:50} | {redable_time:15}")
        if dossiers_tries:
            print("\n📁 DOSSIERS TRIES PAR DATE DE MODIFICATION (du plus récent au plus ancien) :")
            print("-" * 70)
            print(f"{'NOM':50} |{'DERNIÈRE MODIFICATION':15}")
            print("-" * 70)
            for d in dossiers_tries:
                date_modif = d.stat().st_mtime
                redable_time = datetime.fromtimestamp(date_modif).strftime('%Y-%M-%D %H:%M:%S')
                print(f"{d.name:50} | {redable_time:15}")
        
    elif choix == "8":
        fichiers =  [f for f in dossier.iterdir() if f.is_file()]
        fichiers_tries = sorted(fichiers, key=lambda f: f.suffix.lower(), reverse=True)
        if fichiers_tries:
            print("\n📁 FICHIERS TRIES PAR EXTENSION (ordre alphabétique inversé) :")
            print("-" * 70)
            for f in fichiers_tries:
                print(f.name)
        
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 8.")

trier_choisir()
