#Escribe un programa que pida la edad del usuario y muestre uno de estos mensajes según su valor: 1."Eres menor de edad"si tienes menos de 18. 2."Eres adulto" si tiene entre 18 y 64. 3. "Eres mayor" si tienes 65 o más


edad = int(input("Introduce tu edad: "))


if edad < 18:
    print("Eres menor de edad")
elif 18 <= edad <= 64:
    print("Eres adulto")
else:
    print("Eres mayor")
