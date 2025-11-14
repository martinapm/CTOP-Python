# Autor: Martina Pérez Muñoz
# Fecha: 15/11/2025
# Descripción: Pide dos números y una operación (+, -, *, /) y muestra el resultado.
# Entrada esperada: 8, 2, *
# Salida esperada: Resultado: 16

n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))
op = input("Introduce la operación (+, -, *, /): ")

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "Error: división entre cero"
else:
    resultado = "Operación no válida"

print("Resultado:", resultado)
