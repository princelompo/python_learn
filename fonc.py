from functools import wraps
import time

print("===== JOUR SUIVANT =======")


def prncipal(func):
    @wraps(func)
    def wrapper(*arg, **kwargs):
        now = time.perf_counter()
        result = func(*arg, **kwargs)
        end = time.perf_counter()
        print(f" temps d'execution : {end-now}.4f s")
        return result
    return wrapper

@prncipal
def saluer():
    print("Bonjour tout le monde !")

saluer()

# ----------------------------------------------
#simple closure

def multiplier(n):
    def inner(x):
        return x * n
    return inner

double = multiplier(2)
triple = multiplier(3)
print(f"Double de 5 = {double(5)}")
print(f"Triple de 5 = {triple(5)}")
