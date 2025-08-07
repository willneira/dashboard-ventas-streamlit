# ejercicio_4.py
import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame con datos de categorías y valores
data = {
    'Categoría': ['A', 'B', 'C', 'D', 'E'],
    'Valor': [80, 150, 200, 95, 130]
}
df = pd.DataFrame(data)

# Filtrar valores mayores a 100
df_filtrado = df[df['Valor'] > 100]

# Crear gráfico de barras con los datos filtrados
plt.bar(df_filtrado['Categoría'], df_filtrado['Valor'], color='green')

# Añadir etiquetas a los ejes y título
plt.xlabel('Categoría')
plt.ylabel('Valor')
plt.title('Valores Mayores a 100')

# Ajuste del layout y visualización
plt.tight_layout()
plt.show()
