# 1. GESTIÓN DE ESTUDIANTES
estudiantes = ["Marta García", "Rafael López", "Thomas Rodríguez"]

print("Lista Inicial de Estudiantes:")
for i, estudiante in enumerate(estudiantes, 1):
    print(f"{i}. {estudiante}")

# añadir estudiante
nuevo = input("\nIntroduce el nombre del nuevo estudiante: ").strip()
if nuevo:
    estudiantes.append(nuevo)
    print(f"Estudiante '{nuevo}' añadido.")

print("\nLista después de añadir:")
for i, estudiante in enumerate(estudiantes, 1):
    print(f"{i}. {estudiante}")

# eliminar estudiante
print("\n Eliminar un estudiante")
print("Estudiantes disponibles:")
for i, estudiante in enumerate(estudiantes, 1):
    print(f"{i}. {estudiante}")

try:
    idx = int(input("\nNúmero del estudiante a eliminar: "))
    if 1 <= idx <= len(estudiantes):
        eliminado = estudiantes.pop(idx - 1)
        print(f"Estudiante '{eliminado}' eliminado.")
    else:
        print("Número no válido.")
except ValueError:
    print("Debes introducir un número.")

# ordenar
estudiantes.sort()
print("\nLista ordenada:")
for i, estudiante in enumerate(estudiantes, 1):
    print(f"{i}. {estudiante}")

# 2. CALIFICACIONES
print("\nCalificaciones")

calificaciones = {}

print("\nIntroduce calificaciones (0-10):")
for estudiante in estudiantes:
    while True:
        try:
            nota = float(input(f"Nota para {estudiante}: "))
            if 0 <= nota <= 10:
                calificaciones[estudiante] = nota
                break
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Introduce un número.")

print("\nTodas las calificaciones:")
for estudiante, nota in calificaciones.items():
    print(f"{estudiante}: {nota:.2f}")

# menú simple
while True:
    print("\n1. Añadir/actualizar nota")
    print("2. Ver nota de un alumno")
    print("3. Ver todas las notas")
    print("4. Calcular nota media")
    print("5. Continuar")
    
    op = input("Elige una opción (1-5): ").strip()
    
    if op == "1":
        nombre = input("Nombre completo del alumno: ").strip()
        
        if nombre not in estudiantes:
            respuesta = input("¿Añadir a la lista? (s/n): ").strip().lower()
            if respuesta == 's':
                estudiantes.append(nombre)
                estudiantes.sort()
                print(f"Alumno añadido.")
        
        while True:
            try:
                nota = float(input(f"Nota para {nombre}: "))
                if 0 <= nota <= 10:
                    calificaciones[nombre] = nota
                    print(f"Nota actualizada.")
                    break
                else:
                    print("La nota debe estar entre 0 y 10.")
            except ValueError:
                print("Introduce un número.")
    
    elif op == "2":
        nombre = input("Nombre del alumno: ").strip()
        if nombre in calificaciones:
            print(f"Nota: {calificaciones[nombre]:.2f}")
        else:
            print("No hay calificación registrada.")
    
    elif op == "3":
        print("\nCalificaciones:")
        for est, nota in calificaciones.items():
            print(f"{est}: {nota:.2f}")
    
    elif op == "4":
        if calificaciones:
            total = 0
            for nota in calificaciones.values():
                total += nota
            media = total / len(calificaciones)
            print(f"Nota media: {media:.2f}")
        else:
            print("No hay calificaciones.")
    
    elif op == "5":
        print("Continuando...")
        break
    
    else:
        print("Opción no válida.")

# 3. ARCHIVOS
print("Guardando datos en archivo")

# guardar
try:
    archivo = open("alumnos.txt", "w", encoding="utf-8")
    for estudiante, nota in calificaciones.items():
        archivo.write(f"{estudiante} - {nota:.2f}\n")
    archivo.close()
    print(f"Datos guardados en 'alumnos.txt'")
except:
    print("Error al guardar el archivo")

# leer
print("\nLEYENDO DATOS DEL ARCHIVO")
try:
    archivo = open("alumnos.txt", "r", encoding="utf-8")
    print("Contenido del archivo:")
    for linea in archivo:
        print(linea.strip())
    archivo.close()
except:
    print("Error al leer el archivo")

print("\nPrograma terminado")