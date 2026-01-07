from array import array

# Crear array de enteros
nums = array('i', [1, 2, 3, 4])
print("Array original:", nums)

# Cambio del primer elemento
nums[0] = 10
print("Después del cambio:", nums)

# Asignar un valor de tipo incorrecto
nums[1] = "hola"