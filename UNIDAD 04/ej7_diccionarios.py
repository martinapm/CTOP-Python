#ejercicio 6: Diccionarios para que se pueda recorrer e imprimir claves y valores
persona = {
    "nombre": "Carlos",
    "edad": 30
}

# Añadir la clave "ciudad"
persona["ciudad"] = "Madrid"

# Eliminar la clave "edad"
del persona["edad"]

print(persona)

# Recorrer el diccionario e imprimir claves y valores
for clave, valor in persona.items():
    print(clave, ":", valor)