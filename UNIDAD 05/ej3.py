class Cuenta:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo privado
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor
        else:
            print("El saldo no puede ser negativa")
    
c = Cuenta(100)
print(c.saldo)  # Acceso normal
c.saldo = -1  # Setter validado