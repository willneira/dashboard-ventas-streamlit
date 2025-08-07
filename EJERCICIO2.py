# ejercicio_2.py
import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de ventas
data = {
    'Producto': ['A', 'B', 'C', 'D'],
    'Ventas': [120, 340, 230, 150]
}
df = pd.DataFrame(data)

# Crear gráfico de barras
plt.bar(df['Producto'], df['Ventas'])

# Añadir etiquetas a los ejes
plt.xlabel('Producto')
plt.ylabel('Ventas')

# Añadir título
plt.title('Ventas por Producto')

# Ajuste del layout y visualización
plt.tight_layout()
plt.show()
