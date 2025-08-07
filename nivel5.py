import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#---Crear arrays con numpy
#--Crear un array de numeros del 1 al 10
array_simple = np.arange(1, 11)
print("array_simple:", array_simple)
#Crear un array de 10 numeros aleatorios entre 0 y 100
array_aleatorio = np.random.randint(0, 100, size=10)
print("Array Aleatorio:", array_aleatorio)
#--Crear array de números decimales de 0 a 1(con 5 elementos)
array_decimales = np.linspace(0,1,5)
print("Decimales impresos:", array_decimales)

#---Operaciones Vectoriales
#Multiplicar todos los elementos por 2
array_multiplicado = array_simple * 2
print("Multiplicaciones arrays:", array_multiplicado)

# === INTEGRACIÓN NUMPY + PANDAS ===
# Crear un DataFrame desde un array aleatorio
df = pd.DataFrame({
    'ID': array_simple,
    'Valor': array_aleatorio
})
print("\nDataframe generado desde Numpy:")
print(df)

# === VISUALIZACIÓN DEL ARRAY EN GRÁFICO DE BARRAS ===
plt.figure(figsize=(10,5))
plt.bar(df['ID'], df['Valor'])
plt.title('Valores Aleatorios Generados con NumPy')
plt.xlabel('ID')
plt.ylabel('Valor')
plt.show()

# === CREAR UNA MATRIZ 2D CON NUMPY ===
# Simular ventas de 5 vendedores durante 7 días (valores aleatorios entre 100 y 1000)
matriz_ventas = np.random.randint(100, 1000, size=(5, 7))
print("\nMatriz Venta simulada (5 vendedores x 7 dias):")
print(matriz_ventas)
# === CREAR DATAFRAME DESDE LA MATRIZ ===
vendedores = ['Juan','Ana','pedro','Laura','Carlos']
dias = [f'Día {i+1}' for i in range(7)]

df_ventas = pd.DataFrame(matriz_ventas, index=vendedores, columns=dias)
print("\nDataFrame Ventas simuladas:")
print(df_ventas)

# === CALCULAR TOTALES POR VENDEDOR ===
df_ventas['Total Vendedor'] = df_ventas.sum(axis=1)
# === CALCULAR TOTALES POR DÍA ===
totales_dia = df_ventas.sum(axis=0)
print("\nTOTALES POR DÍA:")
print(totales_dia)

# === GRAFICAR BARRAS APILADAS DE LAS VENTAS ===
df_ventas.drop(columns=['Total Vendedor']).T.plot(kind='bar', stacked=True, figsize=(12,6))
plt.title('Ventas Simuladas por Día (Barras Apiladas)')
plt.xlabel('Día')
plt.ylabel('Ventas')
plt.legend(title='Vendedor')
plt.show()

# === SIMULACIÓN DE 1000 REGISTROS DE VENTAS ===
np.random.seed(42)
# Simular 1000 IDs de vendedores aleatorios
vendedores = np.random.choice(['Juan', 'Ana', 'Pedro', 'Laura', 'Carlos'], size=1000)
# Simular montos de ventas aleatorios entre 100 y 5000
ventas = np.random.randint(100, 5000, size=1000)
# Simular fechas aleatorias (últimos 30 días)
fechas = pd.to_datetime('2025-08-01') + pd.to_timedelta(np.random.randint(0,30, size=1000), unit='D')
# Crear DataFrame masivo
df_masivo = pd.DataFrame({
    'Fecha': fechas,
    'Vendedor': vendedores,
    'Venta': ventas
})
print("\nPrimeros 10 registros del DataFrame Masivo:")
print(df_masivo.head(10))

# === ESTADÍSTICAS CON NUMPY ===
media_ventas = np.mean(ventas)
desviacion_ventas = np.std(ventas)
print(f"\nMEDIA DE VENTAS: {media_ventas:.2f}")
print(f"Desviación ESTANDAR DE VENTAS: {desviacion_ventas:.2f}")
# === EXPORTAR A EXCEL ===
df_masivo.to_excel('ventas_simuladas_masivas.xlsx', index=False)
print("\nArchivo generado exitosamente")
