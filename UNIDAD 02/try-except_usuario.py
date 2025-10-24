
try:
    numero = int(input("Introduce un número: "))
    print("Has introducido el número:", numero)
except ValueError:
    print("Error, no has introducido un número válido.")
