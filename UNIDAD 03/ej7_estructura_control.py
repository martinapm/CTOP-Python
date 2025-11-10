#Escribe un programa que recorra una lista de 5 nombres e imprima solo los que tengan más de 4 letras

nombres = ["Martina", "Arianna", "Sol", "Ana", "Samuel"]

for nombre in nombres: 
    if len (nombre) > 4:
        print (nombre)
