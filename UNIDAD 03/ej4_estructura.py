#Define un diccionario llamado alumno con las claves: "nombre", "edad" y "curso". Imprime su contenido con un mensaje claro.

alumno = {
    "nombre": "Martina",
    "edad": 23,
    "curso": "Desarrollo de Aplicaciones Web"
}


for clave, valor in alumno.items():
    print(f"{clave}: {valor}")

