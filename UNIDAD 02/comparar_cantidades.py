
def comparar_cantidades(cantidad1, cantidad2):
    if cantidad1 > cantidad2:
        return "La primera cantidad es mayor."
    elif cantidad1 < cantidad2:
        return "La segunda cantidad es mayor."
    else:
        return "Ambas cantidades son iguales."

while True:
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = comparar_cantidades(num1, num2)
        print(resultado)
        break
    except ValueError:
        print("Error: No has introducido un valor de tipo numérico.")
