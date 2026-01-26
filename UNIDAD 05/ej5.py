#Ejemplo de código con Bajo Acoplamiento

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def obtener_precio(self):
        return self.precio

class Pedido:
    def __init__(self):
        self.productos = []

    def calcular_total(self):
        total = 0
        for p in self.productos:
            #Pedido solo depende de un método público,
            #no del detalle interno del producto
            total += p.obtener_precio()
        return total

# Crear 3 productos
producto1 = Producto("Laptop", 1200.00)
producto2 = Producto("Mouse", 25.50)
producto3 = Producto("Teclado", 75.99)


pedido = Pedido()
pedido.productos.append(producto1)
pedido.productos.append(producto2)
pedido.productos.append(producto3)


total = pedido.calcular_total()
print(f"Producto 1: {producto1.nombre} - ${producto1.obtener_precio()}")
print(f"Producto 2: {producto2.nombre} - ${producto2.obtener_precio()}")
print(f"Producto 3: {producto3.nombre} - ${producto3.obtener_precio()}")
print(f"\nPrecio total: ${total}")