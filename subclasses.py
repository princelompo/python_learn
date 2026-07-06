print()
print("="*50)
print("==== SOUS-CLASSES, POLYMORPHISME ET HERITAGE =====")
print("="*50)

class Animal:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def Cri(self):
        print(f"{self.nom} fait un bruit.")
    
    def __str__(self):
        return f""" ===AFFICHAGE DE L'ANIMAL {self.nom}===
                    Nom : {self.nom}
                    Age : {self.age} ans \n"""

    
class Volant(Animal):
    def __init__(self, nom, age, envergure):
        super().__init__(nom, age)
        self.envergure = envergure

    def voler(self):
        print(f"{self.nom} s'envole avec une envergure de {self.envergure}m.")

    def Cri(self):
        print(f"{self.nom} siffle dans les airs.")

    def __str__(self):
        return f""" ===AFFICHAGE DU VOLANT {self.nom}===
                    Nom : {self.nom}
                    Age : {self.age} ans
                    Envergure : {self.envergure}m \n"""

class Chien(Animal):
    def __init__(self, nom, age, race):
        super().__init__(nom, age) #appel de la classe parente
        self.race = race
    
    def Cri(self):
        print(f"{self.nom} aboie OAUFF !.")
    
    def __str__(self):
        return f""" ===AFFICHAGE DU CHIEN {self.nom}===
                    Nom : {self.nom}
                    Age : {self.age} ans
                    Race : {self.race} \n"""

class Chat(Animal):
    def __init__(self, nom, age, couleur):
        super().__init__(nom, age)
        self.couleur = couleur
    
    def Cri(self):
        print(f"{self.nom} miaule MIAOU !.")
    
    def __str__(self):
        return f""" ===AFFICHAGE DU CHAT {self.nom}===
                    Nom : {self.nom}
                    Age : {self.age} ans
                    Couleur : {self.couleur} \n"""
                
class Canard(Volant):
    def __init__(self, nom, age, envergure, couleur):
        super().__init__(nom, age, envergure)
        self.couleur = couleur

    def __str__(self):
        return f""" ===AFFICHAGE DU CANARD {self.nom}===
                    Nom : {self.nom}
                    Age : {self.age} ans
                    Envergure : {self.envergure}m
                    Couleur : {self.couleur} \n"""






canard1 = Canard("Vivo", 2,"4km/h", "Noir")
print(canard1)
canard1.Cri()
canard1.voler()
print(isinstance(canard1, Animal))
print(isinstance(canard1, Volant))
print(isinstance(canard1, Chien))
print(isinstance(canard1, Chat))
print(isinstance(canard1, Canard))
print(issubclass(Canard, Animal))
print(issubclass(Canard, Volant))
print()

chien1, chat1 = Chien("Fido", 3, "Canis Familiaris"), Chat("Garfield", 2, "Orange")
print(chien1)
print(chat1)
chien1.Cri()
chat1.Cri()
print(isinstance(chien1, Animal))
print(isinstance(chat1, Animal))
print(isinstance(chien1, Volant))
print(isinstance(chat1, Volant))
print(isinstance(chien1, Chien))
print(isinstance(chat1, Chat))
print()

animaux = [chien1, chat1, canard1, Animal("Humain",35), Volant("Hugo", 22, "10km/h")]
numero = [i for i in range(1, len(animaux)+1)]

tout = { x:y for x,y in zip(numero, animaux)}
for a, b in tout.items():
    print(f"animal {a} : {b}")

