from functools import wraps


print("\t\n===== ✨✨DÉCORATEURS AVEC PARAMÈTRES =======\n")

def repeter (n):
    def decorer(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for k in range (0,n):
                print(f"{k+1} fois /{n} :", end=" ")
                func(*args, **kwargs)
        return wrapper
    return decorer

@repeter(3)
def saluer():
    print("Bonjour tout le monde !")

saluer()

def validation_arg(*types):
    """Fabrique de décorateur qui valide les types des arguments d'une fonction."""
    def decorer(func):
        """Décorateur qui valide les types des arguments d'une fonction."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Valide les types des arguments avant d'appeler la fonction et retourne une erreur si les types ne correspondent pas."""
            if len(args) != len(types):
                raise TypeError(f"Nombre d'arguments incorrect : attendu {len(types)}, reçu {len(args)}")
            for i, (arg, typ) in enumerate(zip(args, types)):
                if not isinstance(arg, typ):
                    raise TypeError(f"ARgument {i+1} : attendu {typ.__name__}, reçu {type(arg).__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorer

@validation_arg(str, str, int)
def afficher_info(nom, prenom, age):
    print(f"Nom : {nom}, Prénom : {prenom}, Age : {age} ans")

afficher_info("Alice", "Dupont", 30)

try:
    afficher_info("Alice", "Dupont", "trente")
except TypeError as e:
    print(f"Erreur de validation : {e}")
