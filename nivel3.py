import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ventas_diarias.csv', parse_dates=['Fecha'])

print("DATOS")
print(df)
#-- Agrupar por fechas(sumando ventas)
ventas_diarias = df.groupby('Fecha')['Ventas'].sum().reset_index()
print("\nVentas por fecha")
print(ventas_diarias)

#--Filtrar datos desde el 03 de agosto de 2025 en adelante
fecha_inicio = '2025-08-03'
ventas_filtradas = df[df['Fecha'] >= fecha_inicio]
print(f"\n Ventas desde {fecha_inicio} en adelante ")
print(ventas_filtradas) 

# Agrupar las ventas filtradas por Fecha
ventas_filtradas_por_fecha = ventas_filtradas.groupby('Fecha')['Ventas'].sum().reset_index()

# Graficar las ventas filtradas
plt.figure(figsize=(10,5))
plt.plot(ventas_filtradas_por_fecha['Fecha'], ventas_filtradas_por_fecha['Ventas'], marker='o', color='orange')
plt.title(f'Ventas desde {fecha_inicio} en adelante')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()


# Graficar Ventas por fecha
plt.figure(figsize=(10,5))
plt.plot(ventas_diarias['Fecha'], ventas_diarias['Ventas'], marker='o')
plt.title('Ventas Diarias Totales')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.grid(True)
plt.show()

#--Agrupar por vendedor y sumar ventas
ventas_por_vendedor =df.groupby('Vendedor')['Ventas'].sum().reset_index()
print("\nVENTAS TOTALES POR VENDEDOR")
print(ventas_por_vendedor)

#--Graficar Ventas por vendedor(Barras)
plt.figure(figsize=(8,5))
plt.bar(ventas_por_vendedor['Vendedor'], ventas_por_vendedor['Ventas'])
plt.title('Ventas Totales por Vendedor')
plt.xlabel('Vendedor')
plt.ylabel('Ventas')
plt.show()

# Crear resumen de ventas diarias (total por fecha)
resumen_diario = df.groupby('Fecha')['Ventas'].sum().reset_index()
# Exportar el resumen a un archivo Excel
resumen_diario.to_excel('resumen_ventas_diarias.xlsx', index=False)
print("\n ARCHIVO GENERADO CORRECTAMENTE.")
