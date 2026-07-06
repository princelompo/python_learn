n = int(input("entrer la valeur de n : "))

for i in range(n):
    for j in range (i+1):
        x = 65 + i
        print(chr(x), end="")
    print()


print(ord('A')) #65
print(ord('Z')) #90
print(ord('a'))
print(abs(-5))
print(ascii('A'))
print(ascii('é'))
print(bin(10))
print(oct(10))
print(hex(10))
print(bool(0))
print(bool(1))
print(bool(""))
print(all([True, True, False]))
print(any([True, True, False]))
print(chr(65))
print(chr(90))


print(" Toutes les methodes des caracteres \n")

phrase = "Bonjour le monde"
print(phrase.upper()) # met en majuscules
print(phrase.lower()) # met en minuscules
print(phrase.capitalize()) # met la première lettre en majuscule
print(phrase.title()) # met la première lettre de chaque mot en majuscule
print(phrase.swapcase()) # inverse les majuscules et minuscules
print(phrase.strip()) # supprime les espaces au début et à la fin
print(phrase.replace("o", "0")) # remplace les 'o' par des '0'
print(phrase[0:5:3]) # extrait une partie de la phrase (de l'index 0 à 5 avec un pas de 3)
print(phrase.split()) # découpe la phrase en mots
print(phrase.find("le")) # trouve la position de "le"
print(phrase.count("o")) # compte le nombre d'occurrences de "o"
print(phrase.index("le")) # trouve la position de "le"
print(phrase.startswith("Bon")) # vérifie si la phrase commence par "Bon"
print(phrase.endswith("de")) # vérifie si la phrase se termine par "de"
print(phrase.isalpha()) # vérifie si la phrase est composée uniquement de lettres
print(phrase.isdigit()) # vérifie si la phrase est composée uniquement de chiffres
print(phrase.isalnum()) # vérifie si la phrase est composée uniquement de lettres et de chiffres
print(phrase.islower()) # vérifie si la phrase est en minuscules
print(phrase.isupper()) # vérifie si la phrase est en majuscules
print(phrase.isspace()) # vérifie si la phrase est composée uniquement d'espaces
print(phrase.center(30)) # centre la phrase dans une largeur de 30 caractères
print(phrase.ljust(30)) # aligne la phrase à gauche dans une largeur de 30 caractères
print(phrase.rjust(30)) # aligne la phrase à droite dans une largeur de 30 caractères
print(phrase.zfill(30)) # complète la phrase avec des zéros à gauche pour atteindre une largeur de 30 caractères    
print(phrase.partition("le")) # partitionne la phrase en trois parties autour de "le"
print(phrase.rpartition("le")) # partitionne la phrase en trois parties autour de "le" en partant de la fin
print(phrase.splitlines()) # découpe la phrase en lignes
print(phrase.expandtabs()) # remplace les tabulations par des espaces
print(phrase.encode()) # encode la phrase en bytes
print(phrase.decode()) # decode la phrase en bytes
print(phrase.format()) # formate la phrase (utile pour les chaînes avec des placeholders)
print(phrase.format_map({})) # formate la phrase avec un mapping (dictionnaire)

