
import time as t

while True:
    try:
        n = int(input("Introduce un número entre 5 y 50: "))
        if 5 <= n <= 50:
            for i in range(n, 0, -1):
                print(i)
                t.sleep(0.5)
            print("OUT")
        else:
            print("Número fuera de rango.")
    except ValueError:
        print("Por favor, introduce un número válido.")
