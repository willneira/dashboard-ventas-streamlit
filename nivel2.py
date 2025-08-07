import pandas as pd

#--Leer desde archivo Excel
df = pd.read_excel('ventas.xlsx', sheet_name='Datos')
df.columns = df.columns.str.strip()  # Limpiar espacios en nombres de columnas
print("DATOS")
print(df)
#--Total ventas por vendedor
ventas_por_vendedor = df.groupby('Vendedor')['Ventas'].sum()
print("\n TOTAL VENTAS X VENDEDOR")
print(ventas_por_vendedor)
# Total ventas por región y producto
ventas_por_region_producto = df.groupby(['Region','Producto'])['Ventas'].sum()
print("\n VENTAS X REGION Y PRODUCTO")
print(ventas_por_region_producto)
#--Agregar columna  de Comisión(5%)
df['Comisión'] = df['Ventas'] * 0.05
print("\n DATOS CON COMISIÓN")
print(df)
#--Guardar resultado en nuevo archivo Excel
df.to_excel('ventas_con_comision.xlsx', index=False)
