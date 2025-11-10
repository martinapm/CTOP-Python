#Escribe un programa que calcule la suma de los números pares del 1 al 20 utilizando un bucle while

numero = 1
suma = 0

while numero <= 20:
    if numero % 2 == 0:
        suma += numero
    numero += 1

print("La suma de los números pares del 1 al 20 es:", suma)
