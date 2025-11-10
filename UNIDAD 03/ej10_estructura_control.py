#Crea un programa que pida al usuario una palabra y cuente cuántas letras tiene (sin usar la función len())

palabra = input("Escriba una palabra: ")

contador = 0
for letra in palabra:
    contador += 1

print("La palabra tiene", contador, "letras")
