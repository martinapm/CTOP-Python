palabras = []
contador = 0

while True:
    try:
        palabra = input("Introduce una palabra (introduzca la palabra 'Basta' para que termine): ")
        if palabra == "" or palabra == "Basta":
            break
        palabras.append(palabra)
        contador += 1
        print("Palabras introducidas hasta ahora:")
        for p in palabras:
            print(p)
    except Exception as e:
        print(f"Error: {e}")

print(f"Has soportado estoicamente {contador} preguntas.")
