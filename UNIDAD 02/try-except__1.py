
texto = " " 

try:
    f = open("archivo.txt", "w")
    #texto = f.read()
    f.write("Hola, ke hase")
except IOError as e:
    print("Ocurrió un error:", e)
else:
    print("Fichero escrito correctamente")
finally:
    f.close()
    