#Crea un módulo llamado operaciones.py que contenga las funciones sumar(), restar(), multiplicar() y dividir(). Asegúrate de que el módulo no pueda ser ejecutado como un programa independiente.
def media_varios(*numeros):
    if len(numeros) < 2:
        return "Error: se necesitan al menos dos números."
    
    for n in numeros:
        if not isinstance(n, (int, float)):
            return "Error: todos los valores deben ser numéricos."
    
    return sum(numeros) / len(numeros)


print(media_varios(2, 4, 6, 8))
