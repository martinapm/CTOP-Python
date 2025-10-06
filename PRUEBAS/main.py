import sys, saludos, calculos

total = 10

#Muestra tu nombre y apellidos

nombre = 'Martina Pérez Muñoz'

print(saludos.saludar(nombre))
print(saludos.despedir(nombre))


#Calculos


a = 5
b = 3

print(calculos.suma(a, b))
print(calculos.resta(a, b))








#Modifica el valor de 'total' usando una operación del módulo

if __name__ != '__main__':
    print('Ejecútame, que no soy un módulo.')
    print(__name__)
    sys.exit(1)

