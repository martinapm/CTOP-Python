#Crea una función que calcule la media aritmética de dos valores numéricos introducidos por el usuario. Asegúrate de que los tipos de datos introducidos son correctos (validación de datos de entrada).
def media_dos_valores():
    while True:
        try:
            a = float(input("Introduce el primer número: "))
            b = float(input("Introduce el segundo número: "))
            break
        except ValueError:
            print("Error: Debes introducir solo números.")
    
    media = (a + b) / 2
    print(f"La media es: {media}")
