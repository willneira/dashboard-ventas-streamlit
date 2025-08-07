import pandas as pd

# Leer archivo Excel que ya tiene la columna Comisión
df = pd.read_excel('ventas_con_comision.xlsx')

# Agrupar por Vendedor y sumar Ventas y Comisión
resumen = df.groupby('Vendedor')[['Ventas', 'Comisión']].sum().reset_index()

# Cambiar nombres de columnas para claridad
resumen = resumen.rename(columns={
    'Ventas': 'Total Ventas',
    'Comisión': 'Total Comisión'
})

# Mostrar el resumen en consola
print("=== Resumen por Vendedor ===")
print(resumen)

# Guardar el resumen en un nuevo archivo Excel
resumen.to_excel('resumen_vendedores.xlsx', index=False)
