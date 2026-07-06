# NOTION DE CLASSES EN PYTHON

print()
print("="*50)
print("========== NOTION DE CLASSES EN PYTHON ===========")
print("="*50)

class Etudiant:
    def __init__(self, nom, age, filiere, notes):
        self.nom = nom
        self.age = age
        self.filiere = filiere
        self.notes = list(notes) 

    def moyenne(self):
        try:
            for note in self.notes:
                if not isinstance(note, (int, float)):
                    raise ValueError(f"Note non numérique détectée : {note}")
                if note < 0 or note > 20:
                    raise ValueError(f"Note hors intervalle [0-20] : {note}")
            return sum(self.notes) / len(self.notes)
        except ZeroDivisionError:
            return 0

    def Admis(self):
        return self.moyenne() >= 10
    
    def __str__(self):
        return f""" ===AFFICHAGE DE L'ÉTUDIANT {self.nom}===
                    Nom : {self.nom}
                    Age : {self.age} ans
                    Filière : {self.filiere}
                    Notes : {', '.join(map(str, self.notes))}
                    Moyenne : {self.moyenne():.2f}
                    Admis : {'Oui' if self.Admis() else 'Non'} \n """


class Compte_bancaire:
    def __init__(self, proprietaire, solde = 0):
        self.proprietaire = proprietaire
        self.solde = solde
    
    def deposer(self, montant):
        self.solde += montant
        print(f"Dépôt de {montant}€ effectué pour {self.proprietaire} Nouveau solde : {self.solde}€")
    
    def retirer(self, montant):
        try:
            if montant > self.solde:
                raise ValueError("Solde insuffisant.")
            elif montant < 0:
                raise ValueError("Montant négatif.")
            elif not isinstance(montant, (int, float)):
                raise TypeError("Montant non numérique.")
            else:
                self.solde -= montant
                print(f"Retrait de {montant}€ effectué pour {self.proprietaire} Nouveau solde : {self.solde}€")
        except ValueError as e:
            print(f"Erreur de retrait : {e}")

    def __str__(self):
        return f""" ===AFFICHAGE DU COMPTE {self.proprietaire}===
                    Propriétaire : {self.proprietaire}
                    Solde : {self.solde}€  \n"""

# ----------------------------------------------

class Projet():
    def __init__(self, nom, description, membres, **langages):
        self.nom = nom
        self.description = description
        self.membres = membres
        self.langages = langages

    def ajouter_membre(self, membre):
        if membre not in self.membres:
            self.membres.append(membre)
            print(f"{membre} a été ajouté au projet {self.nom}.")
        else:
            print(f"{membre} est déjà dans le projet {self.nom}.")
    
    def supprimer_membre(self, membre):
        if membre in self.membres:
            self.membres.remove(membre)
            print(f"{membre} a été supprimé du projet {self.nom}.")
        else:
            print(f"{membre} n'est pas dans le projet {self.nom}.")

    def ajouter_langage(self, langage):
        for valeur in self.langages.values():
            if valeur == langage:
                print(f"{langage} est déjà associé au projet {self.nom}.")
                return
        if not isinstance(langage,str):
            print(f"{langage} n'est pas une chaîne de caractères.")
            return
        else:
            self.langages[f"langage{len(self.langages) + 1}"] = langage
            print(f"{langage} a été ajouté au projet {self.nom} comme langage de programmation.")
        
    def __str__(self):
        return f""" ===AFFICHAGE DU PROJET {self.nom}===
                    Nom : {self.nom}
                    Description : {self.description}
                    Membres : {', '.join(self.membres)}
                    Langages : {', '.join(self.langages.values())} \n"""  

    
print("\n✨INFORMATIONS SUR LA CLASSE ÉTUDIANT✨\n")
etudiant1 = Etudiant("Alice", 20, "Informatique", (15, 18, 12))
etudiant2 = Etudiant("Bob", 18, "Mathematiques", (11, 9, 8, 6))
print(etudiant1)
print(etudiant2)

print("\n✨INFORMATIONS SUR LA CLASSE COMPTE_BANCAIRE✨\n")
compte1 = Compte_bancaire("Alice")
compte2 = Compte_bancaire("Bob", 500)
print(compte1)
print(compte2)
compte1.deposer(1000)
compte2.retirer(200)
print()
print(compte1)
print(compte2)

print("\n✨INFORMATIONS SUR LA CLASSE PROJET✨\n")
projet1 = Projet("Application", "Creation d'une application web pour l'entreprise", ["Alice", "Bob", "Charlie"], langage1="Python", langage2="JavaScript")
print(projet1)
projet1.ajouter_membre("David")
projet1.supprimer_membre("Bob")
projet1.ajouter_langage("Java")
projet1.ajouter_langage("C++")
projet1.ajouter_langage("Python")
print()
print(projet1)




 



            