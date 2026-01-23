import sqlite3

conexion = sqlite3.connect("empresa.db")
cursor = conexion.cursor()

#CREAR TABLA empleado
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    salario REAL
)   
""")    

#INSERTAR DATOS EN LA TABLA empleado
cursor.execute("INSERT INTO empleados (nombre, salario) VALUES (?, ?)", ("Paco", 50000.0))
conexion.commit()
print("Empleado insertado correctamente.")

#LEER empleado(s)
cursor.execute("SELECT * FROM empleados")

print("Lista de empleados:")
for fila in cursor.fetchall():
    print(f"ID: {fila[0]}, Nombre: {fila[1]}, Salario: {fila[2]}")

#Cerrar cursor y conexión
cursor.close()
conexion.close()