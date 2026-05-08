import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================
# Título
# ==========================
st.title("Análisis de coches 🚗")
st.header("Cuadro de mandos de anuncios de autos")

# ==========================
# Cargar datos
# ==========================
df = pd.read_csv("cars.csv")

st.write("Vista previa de los datos:")
st.dataframe(df)

# ==========================
# Filtros en sidebar
# ==========================
st.sidebar.header("Filtros")

# Marcas
marcas = df["make"].dropna().unique()
marca_seleccionada = st.sidebar.multiselect(
    "Selecciona la marca:",
    marcas,
    default=list(marcas)
)

# Filtrar por marca
df_filtrado = df[df["make"].isin(marca_seleccionada)]

# Modelos
modelos = df_filtrado["model"].dropna().unique()
modelo_seleccionado = st.sidebar.multiselect(
    "Selecciona el modelo:",
    modelos,
    default=list(modelos)
)

df_filtrado = df_filtrado[df_filtrado["model"].isin(modelo_seleccionado)]

# Años
anos = df_filtrado["year"].dropna().unique()
ano_seleccionado = st.sidebar.multiselect(
    "Selecciona el año:",
    anos,
    default=list(anos)
)

df_filtrado = df_filtrado[df_filtrado["year"].isin(ano_seleccionado)]

# ==========================
# Mostrar datos filtrados
# ==========================
if df_filtrado.empty:
    st.warning("No hay datos con los filtros seleccionados 😕")
else:
    st.dataframe(df_filtrado)

    # ==========================
    # Gráfico de barras
    # ==========================
    st.subheader("Precio por modelo")

    fig_bar = px.bar(
        df_filtrado,
        x="model",
        y="price",
        color="make",
        title="Precio por modelo"
    )
    st.plotly_chart(fig_bar, use_container_width=True)

    # ==========================
    # Histograma
    # ==========================
    st.subheader("Histograma de precios")

    if st.button("Generar histograma"):
        fig_hist = px.histogram(
            df_filtrado,
            x="price",
            nbins=20,
            title="Distribución de precios"
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    # ==========================
    # Scatter plot
    # ==========================
    st.subheader("Relación precio vs odómetro")

    if st.button("Generar scatter plot"):
        fig_scatter = px.scatter(
            df_filtrado,
            x="odometer",
            y="price",
            color="make",
            title="Relación entre kilometraje y precio"
        )
        st.plotly_chart(fig_scatter, use_container_width=True)