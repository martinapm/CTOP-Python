#Ejemplo 1
#El siguiente ejemplo combina POO y bases de datos, objetivo central de esta unidad:


class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

#Crear objeto
u = Usuario("Ana", 30)

#Guardar el objeto en una base de datos SQLite
import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, edad INTEGER)")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (u.nombre, u.edad))

conexion.commit()
print("OK. Base de datos guardada.")

conexion.close()