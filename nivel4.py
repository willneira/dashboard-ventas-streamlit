import pandas as pd
import matplotlib.pyplot as plt
#--Leer csv con fechas
df = pd.read_csv('ventas_diarias.csv', parse_dates=['Fecha'])
#--Agrupar por fechas(total ventas diarias)
ventas_diarias = df.groupby('Fecha')['Ventas'].sum().reset_index()
#--Agrupar por vendedor(total ventas por vendedor)
ventas_vendedor = df.groupby('Vendedor')['Ventas'].sum().reset_index()

# === GRÁFICO 1: LÍNEAS Y BARRAS JUNTOS ===
plt.figure(figsize=(10,6))
plt.bar(ventas_diarias['Fecha'], ventas_diarias['Ventas'], alpha=0.6, label='Ventas (Barras)')
plt.plot(ventas_diarias['Fecha'], ventas_diarias['Ventas'], marker='o', color='red', label='Ventas (Línea)')
plt.title('Ventas Diarias Totales (Barras + Línea)')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.legend()
plt.grid(True)
plt.show()

# === GRÁFICO 2: PASTEL (Ventas por Vendedor) ===
plt.figure(figsize=(8,8))
plt.pie(ventas_vendedor['Ventas'], labels=ventas_vendedor['Vendedor'], autopct='%1.1f%%', startangle=140)
plt.title('Distribución de Ventas por Vendedor')
plt.show()

#--Exportar un dashboard Excel
with pd.ExcelWriter('dashboard_ventas.xlsx') as writer:
    ventas_diarias.to_excel(writer, sheet_name='Resumen Diario', index=False)
    ventas_vendedor.to_excel(writer, sheet_name='Resumen por Vendedor', index=False)
print("\nArchivo generado correctamente.")

#--Crear tabla dinamica de ventas por fecha y vendedor
pivot = df.pivot_table(index='Fecha', columns='Vendedor', values='Ventas', aggfunc='sum', fill_value=0)

# Graficar Barras Apiladas
pivot.plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Ventas Diarias por Vendedor (Barras Apiladas)')
plt.xlabel('Fecha')
plt.ylabel('Ventas')
plt.legend(title='Vendedor')
plt.grid(True)
plt.show()