import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# === TÍTULO DEL DASHBOARD ===
st.title("Dashboard de Ventas Interactivo")
# === CARGA DE DATOS ===
df = pd.read_excel('ventas_simuladas_masivas.xlsx')
# === SIDEBAR FILTROS ===
vendedores = st.sidebar.multiselect(
    "Selecciona Vendedores",
    options=df['Vendedor'].unique(),
    default=df['Vendedor'].unique()
)
# === FILTRAR DATOS ===
df_filtrado = df[df['Vendedor'].isin(vendedores)]
# === KPIs ===
total_ventas = df_filtrado['Venta'].sum()
ventas_promedio = df_filtrado['Venta'].mean()
st.metric("Total Ventas", f"${total_ventas:,.2f}")
st.metric("VENTA PROMEDIO", f"${ventas_promedio:,.2f}")
# === GRAFICO BARRAS VENTAS POR VENDEDOR ===
ventas_por_vendedor = df_filtrado.groupby('Vendedor')['Venta'].sum()
st.subheader("VENTAS POR VENDEDOR")
st.bar_chart(ventas_por_vendedor)
# === GRAFICO LINEAL DE VENTAS DIARIAS ===
ventas_diarias = df_filtrado.groupby('Fecha')['Venta'].sum()
st.subheader("VENTAS DIARIAS TOTALES")
st.line_chart(ventas_diarias)
# === HISTOGRAMA DE VENTAS ===
st.subheader("DISTRIBUCIÓN DE VENTAS")
fig, ax = plt.subplots()
ax.hist(df_filtrado['Venta'], bins=20, color='skyblue', edgecolor='black')
st.pyplot(fig)