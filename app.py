import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis de coches 🚗")

# Leer datos del CSV
df = pd.read_csv("cars.csv")
st.write("Aquí están los datos de coches:")
st.dataframe(df)

# Histograma por año
if st.button("Mostrar histograma por año"):
    fig = px.histogram(df, x="year", color="make", title="Cantidad de coches por año")
    st.plotly_chart(fig)
