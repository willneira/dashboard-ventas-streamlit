import pandas as pd

#--Lerr archivo CSV
empleados_df = pd.read_csv('empleados.csv')
#--Mostrar primeras filas
print("=== Datos ===")
print(empleados_df)
#--Ver estadisticas
print("\n=== Estadísticas ===")
print(empleados_df.describe())
#--Filtrar empleados con salario > 3000
print("\n=== Empleados con Salario > 3000 ===")
print(empleados_df[empleados_df['Salario'] > 3000])
#--Agregar nueva columna Bonificación (10% del salario)
empleados_df['Bonificación'] = empleados_df['Salario'] * 0.10
print("\n=== Con Bonificaión ==0")
print(empleados_df)
# Guardar el resultado en un nuevo archivo
empleados_df.to_csv('empleados_con_bono.csv', index=False)