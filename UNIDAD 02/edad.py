# Pedir la edad al usuario
edad = int(input("Introduce tu edad: "))

# Verificar si está dentro del rango válido
if edad < 1 or edad > 120:
    print("Edad no válida")
else:
    # Clasificación por rango de edad
    if edad < 16:
        print("Eres niño/a")
    elif edad >= 16 and edad <= 21:
        print("Eres adolescente")
    elif edad >= 22 and edad <= 35:
        print("Eres joven")
    elif edad <= 50:
        print("Eres maduro/a")
    elif edad >= 51 and edad <= 60:
        print("Eres de mediana edad")
    elif edad >= 61 and edad <= 80:
        print("Eres mayor")
    elif edad >= 81 and edad <= 100:
        print("Eres viejo/a")
    else:
        print("Eres centenario/a")
