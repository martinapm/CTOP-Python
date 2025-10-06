import sys

def saludar(nombre):
    return f'¡Hola, {nombre}!'

def despedir(nombre):
    return f'Hasta luego, {nombre}'

if __name__ == '__main__':
    print('No me ejecutes, ¡solo soy un módulo!')
    print(__name__)
    sys.exit(1)
else:

    print(__name__)