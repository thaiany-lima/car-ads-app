import pandas as pd
import plotly.express as px
import streamlit as st

# lendo o arquivo CSV com os dados dos carros
car_data = pd.read_csv("vehicles_us.csv")

st.header("Car Data Visualization")

build_histogram = st.checkbox("Show Histogram")

if build_histogram:
    # criando o histograma com Plotly Express

    st.write("Criando um histograma para o conjunto de dados :")

    fig = px.histogram(car_data, x="price", nbins=20,
                       title="Distribution of Car price")
    st.plotly_chart(fig)

build_scatter = st.checkbox("Show Scatter Plot")

if build_scatter:
    # criando o gráfico de dispersão com Plotly Express

    st.write("Criando um gráfico de dispersão para o conjunto de dados :")
    fig = px.scatter(car_data, x="model_year", y="price",
                     title="Car Price vs Model Year")
    st.plotly_chart(fig)
