import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="DASHBOARD VENTAS", layout="wide")
st.title("DASBOARD INTERACTIVO")
st.markdown("ANÁLISIS INTERACTIVO VENTAS POR FECHA Y VENDEDOR")
#--Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("ventas_diarias.csv", parse_dates=["Fecha"])
df = cargar_datos()
st.subheader("Vista previa de los datos")
st.dataframe(df.head())

st.subheader("FILTROS")
#--filtros interactivos
fecha_min = df["Fecha"].min()
fecha_max = df["Fecha"].max()
fecha_inicio, fecha_fin = st.date_input(
    "Rango de fechas",
    value=[fecha_min, fecha_max],
    min_value=fecha_min,
    max_value=fecha_max
)
vendedores = st.multiselect("Selecciona Vendedor(es)", options=df["Vendedor"].unique(), default=df["Vendedor"].unique())
# Aplicar filtros
df_filtrado = df[
    (df["Fecha"] >= pd.to_datetime(fecha_inicio)) &
    (df["Fecha"] <= pd.to_datetime(fecha_fin)) &
    (df["Vendedor"].isin(vendedores))

]
st.subheader("VENTAS TOTALES POR FECHA")
ventas_por_fecha = df_filtrado.groupby("Fecha")["Ventas"].sum()

fig, ax = plt.subplots()
ventas_por_fecha.plot(ax=ax)
ax.set_title("VENTAS POR FECHA")
ax.set_ylabel("Ventas")
ax.set_xlabel("Fecha")
st.pyplot(fig)