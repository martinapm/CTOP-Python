import sys

lista = [1, 2, 3, 4]

try:
    for n in range(5):
        print(lista[n])
except IndexError as e:
    print("Error :", e)
else:
    print("Finalizó sin errores.")
finally:
    sys.exit()
    