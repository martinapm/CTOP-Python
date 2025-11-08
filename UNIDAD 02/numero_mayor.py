
numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))


if numero1 > numero2:
    print(f"El número {numero1} es mayor que {numero2}")
elif numero2 > numero1:
    print(f"El número {numero2} es mayor que {numero1}")
else:
    print("Los números son iguales")
