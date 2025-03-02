import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


st.set_page_config(
    page_title='EDAs',
    initial_sidebar_state='collapsed' 
)

st.title('1.-EDAs')

@st.cache_data
def load_diamonds_data():
    df = pd.read_csv("diamonds.csv")
    df.drop(columns=["Unnamed: 0"], inplace=True, errors="ignore")
    return df

df = load_diamonds_data()

st.title("EDA de Diamantes")
st.header("Dataset Diamonds:")
st.table(df.head()) 


if "mostrar_df" not in st.session_state:
    st.session_state.mostrar_df = False

if st.button("Mostrar todo el Dataset"):
    st.session_state.mostrar_df = not st.session_state.mostrar_df
    
if st.session_state.mostrar_df:
    st.dataframe(df, use_container_width=True)  


st.title('1.- Distrubición de datos (Precio) | Análisis Univariante')

grafico = st.selectbox("Selecciona el gráfico que quieras para analizar el precio:", 
                       ["Histograma con KDE", "Boxplot", "Gráfico de Densidad (KDE)", "Violin Plot"])

fig, ax = plt.subplots(figsize=(10, 6))

if grafico == "Histograma con KDE":
    sns.histplot(df['price'], bins=30, kde=True, color="skyblue", ax=ax)
    ax.set_title("Distribución del Precio con KDE")
    ax.set_xlabel("Precio")
    ax.set_ylabel("Nº Diamantes")

elif grafico == "Boxplot":
    sns.boxplot(x=df['price'], color="red", ax=ax)
    ax.set_title("Boxplot del Precio")
    ax.set_xlabel("Precio")


elif grafico == "Gráfico de Densidad (KDE)":
    sns.kdeplot(df['price'], shade=True, color="green", ax=ax)
    ax.set_title("Gráfico de Densidad del Precio")
    ax.set_xlabel("Precio")


elif grafico == "Violin Plot":
    sns.violinplot(x=df['price'], color="purple", ax=ax)
    ax.set_title("Violin Plot del Precio")
    ax.set_xlabel("Precio")

st.pyplot(fig)



st.title("2.- Análisis del Corte de los Diamantes | Análisis Bivariante")

opcion = st.selectbox("Selecciona un gráfico para analizar el corte:", 
                       ["Box Plot", "Violin Plot", "Bar Chart - Precio Promedio", "Scatter Plot - Precio vs Quilates"])

if opcion == "Box Plot":
    fig = px.box(df, x="cut", y="price", color="cut",
                 title="Distribución del Precio según Calidad del Corte",
                 labels={"cut": "Calidad del Corte", "price": "Precio"})
    st.plotly_chart(fig)

elif opcion == "Violin Plot":
    fig = px.violin(df, x="cut", y="price", color="cut",
                    title="Distribución del Precio según Calidad del Corte",
                    labels={"cut": "Calidad del Corte", "price": "Precio"},
                    box=True, points="all")
    st.plotly_chart(fig)

elif opcion == "Bar Chart - Precio Promedio":
    df_avg_price = df.groupby("cut")["price"].mean().reset_index()
    fig = px.bar(df_avg_price, x="cut", y="price", color="cut",
                 title="Precio Promedio por Calidad del Corte",
                 labels={"cut": "Calidad del Corte", "price": "Precio Promedio"})
    st.plotly_chart(fig)

elif opcion == "Scatter Plot - Precio vs Quilates":
    fig = px.scatter(df, x="carat", y="price", color="cut",
                     title="Relación entre Quilates y Precio, según Calidad del Corte",
                     labels={"carat": "Quilates", "price": "Precio"})
    st.plotly_chart(fig)


st.title("3.- Análisis de múltiples variables | Análisis Multivariante")

sample_size = st.slider("Selecciona el tamaño de la muestra:", min_value=50, max_value=len(df), value=1000, step=100)
df_sample = df.sample(n=sample_size, random_state=42)

grafico = st.selectbox("Selecciona un gráfico multivariante:", 
                       ["Scatter 3D", "Bubble Chart", "Pair Plot", "Heatmap de Correlaciones"])

if grafico == "Scatter 3D":
    fig = px.scatter_3d(df_sample, x="carat", y="price", z="depth", color="cut",
                        title="Relación entre Quilates, Precio y Profundidad",
                        labels={"carat": "Quilates", "price": "Precio", "depth": "Profundidad", "cut": "Calidad del Corte"})
    st.plotly_chart(fig)

elif grafico == "Bubble Chart":
    fig = px.scatter(df_sample, x="carat", y="price", size="depth", color="cut",
                     title="Relación entre Precio, Quilates y Profundidad",
                     labels={"carat": "Quilates", "price": "Precio", "depth": "Profundidad", "cut": "Calidad del Corte"})
    st.plotly_chart(fig)

elif grafico == "Pair Plot":
    fig = px.scatter_matrix(df_sample, dimensions=["carat", "price", "depth", "table"],
                            color="cut",
                            title="Matriz de Dispersión de Variables Numéricas",
                            labels={"carat": "Quilates", "price": "Precio", "depth": "Profundidad", "table": "Tabla", "cut": "Calidad del Corte"})
    st.plotly_chart(fig)

elif grafico == "Heatmap de Correlaciones":
    corr_matrix = df_sample[["carat", "price", "depth", "table"]].corr()
    fig, ax = plt.subplots(figsize=(15, 10))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5, ax=ax,
                cbar_kws={"shrink": 0.8})
    ax.set_title("Mapa de Calor de Correlaciones", fontsize= 30)
    ax.set_xticklabels(["Quilates", "Precio", "Profundidad", "Tabla"], fontsize=18)
    ax.set_yticklabels(["Quilates", "Precio", "Profundidad", "Tabla"], fontsize=18)

    st.pyplot(fig)




col1, col2, col3 = st.columns(3)

with col1:
    if st.button('🏠Volver al Inicio del análisis'): 
        st.switch_page('Inicio.py')
with col2:    
    if st.button("💰Ir a la Predicción de Precio"):
        st.switch_page("pages/2 Predicción Precio.py")  # Asegúrate de que el nombre es correcto
with col3:
    if st.button("💎Ir a Clasificación por Corte"):
        st.switch_page("pages/3 Clasificacion Corte.py")