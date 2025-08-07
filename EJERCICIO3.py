# ejercicio_3.py
import matplotlib.pyplot as plt

# Listas de datos
x = [10, 20, 30, 40, 50]
y = [100, 85, 70, 60, 45]

# Crear gráfico de dispersión personalizado
plt.scatter(x, y, color='red')  # Cambiar color de los puntos a rojo

# Añadir título y etiquetas
plt.title('Gráfico de Dispersión: X vs Y', fontsize=14)
plt.xlabel('Eje X', fontsize=12)
plt.ylabel('Eje Y', fontsize=12)

# Ajuste del layout y visualización
plt.tight_layout()
plt.show()
