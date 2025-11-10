#Escribe un programa que pida al usuario un número y muestre su tabla de multiplicar (del 1 al 10) usando un bucle for

numero = int(input("Ingresa un número: "))

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")
