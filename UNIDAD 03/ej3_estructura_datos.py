#1. Declara una lista con 5 nombres de frutas y muestra: .El primer y el ultimo elemento de la lista. .EL numero total de elementos (usando len())  .El resultado de añadir una nueva fruta con append().

frutas = ["naranja", "pera", "uva", "fresa", "manzana"]


print("Primer elemento:", frutas[0])
print("Último elemento:", frutas[-1])


print("Número total de frutas:", len(frutas))


frutas.append("plátano")


print("Lista de frutas actualizada:", frutas)
