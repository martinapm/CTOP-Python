#Define una función presentar(nombre, edad=18) que muestre un mensaje con ambos datos. Llama a la función con y sin el argumento edad para ver cómo funciona el valor por defecto.

def presentar(nombre, edad=23):
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")


presentar("Alejandro", 21)


presentar("Martina")
