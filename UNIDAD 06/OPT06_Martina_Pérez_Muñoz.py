# U06 - Generadores, iteradores y cierres
# Generador de números de la suerte


def numeros_suerte(limite):
    """Generador que produce números del 1 al límite indicado."""
    for numero in range(1, limite + 1):
        yield numero


def numeros_suerte_pares(limite):
    """Generador que produce solo los números pares del 1 al límite."""
    for numero in range(1, limite + 1):
        if numero % 2 == 0:
            yield numero


# Programa principal
# Cambia este valor por tu número de lista en clase

MI_NUMERO_LISTA = 12

print("=" * 40)
print(f" GENERADOR DE NÚMEROS DE LA SUERTE ")
print("=" * 40)

# Todos los números del 1 al límite
print(f"\n Números del 1 al {MI_NUMERO_LISTA}:")
generador = numeros_suerte(MI_NUMERO_LISTA)
for num in generador:
    print(num, end=" ")
print()

# Solo los números pares
print(f"\n Números PARES del 1 al {MI_NUMERO_LISTA}:")
generador_pares = numeros_suerte_pares(MI_NUMERO_LISTA)
for num in generador_pares:
    print(num, end=" ")
print()

print("\n" + "=" * 40)