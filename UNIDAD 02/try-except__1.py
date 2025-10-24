
texto = " " 

try:
    f = open("archivo.txt", "r")
    texto = f.read()
except IOError as e:
    print("Ocurrió un error:", e)
