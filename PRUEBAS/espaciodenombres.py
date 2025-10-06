from math import pi as PI
from math import sin as seno


#Nuestra propia función "sin() (seno)"
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14 #Definimos pi
 
print(sin(pi/2)) #0.999999
print(seno(PI/2)) #1.0


#Aunque se llama igual no hay conflicto de nombres, ¿porqué?
#Porque El código no tiene conflicto de nombres porque las funciones sin() y la constante pi están definidas en ámbitos diferentes