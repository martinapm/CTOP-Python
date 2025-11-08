#1.Crea un programa que pida al usuario un número decimal y muestre su valor convertido a entero y a cadena de texto 
#2.Ahora convierte una variable de tipo cadena a entero y realiza una operación aritmética con ella. Ejemplo: "5" -> 5 + 2 = 7.


numero_decimal = float(input("Ingresa un número decimal: "))

print("Convertido a entero:", int(numero_decimal))
print("Convertido a cadena:", str(numero_decimal))


cadena_numero = "5"
entero = int(cadena_numero)
resultado = entero + 2

print("Resultado", resultado)
