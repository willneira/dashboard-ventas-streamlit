import pandas as pd
#---Leer el archivo csv que tienen los datos.
empleados_df = pd.read_csv('empleados.csv')
#--crear columna bonificación.
empleados_df['Bonificación'] = empleados_df['Salario'] * 0.10
#---crear columna Salario Total.
empleados_df['Salario Total'] = empleados_df['Salario'] + empleados_df['Bonificación']

# Filtrar empleados con Salario Total > 4000
empleados_filtrados = empleados_df[empleados_df['Salario Total'] > 4000]

print(empleados_df[empleados_df['Salario'] > 4000])
print(empleados_df)
# Guardar en archivo CSV
#empleados_filtrados.to_csv('empleados_filtrados.csv', index=False)

