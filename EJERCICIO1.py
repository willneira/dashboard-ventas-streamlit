# ejercicio_1.py
import matplotlib.pyplot as plt

# Listas de datos
x = [1, 2, 3, 4, 5]
y = [3, 7, 9, 6, 12]

# Crear gráfico de línea
plt.plot(x, y)

# Añadir título
plt.title('Gráfico de Línea Básico: Relación X vs Y')

# Ajuste del layout y visualización
plt.tight_layout()
plt.show()
