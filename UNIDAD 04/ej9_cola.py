from collections import deque

cola = deque()

# Añadir 3 elementos
cola.append("a")
cola.append("b")
cola.append("c")

# Eliminar el primero
cola.popleft()

# Mostrar la cola resultante
print(cola)