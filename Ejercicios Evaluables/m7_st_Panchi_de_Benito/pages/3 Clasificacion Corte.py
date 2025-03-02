import streamlit as st
import joblib
import pandas as pd


st.set_page_config(
    page_title="Clasificación",
    page_icon="🗂️",
    initial_sidebar_state="collapsed"
)

st.title("Predicción del Corte del Diamante | Clasificación")


@st.cache_data
def load_diamonds_data():
    df = pd.read_csv("diamonds.csv")
    df.drop(columns=["Unnamed: 0"], inplace=True, errors="ignore")
    return df

df = load_diamonds_data()

st.header("Vista Previa del Dataset")
st.table(df.head())

if "mostrar_df" not in st.session_state:
    st.session_state.mostrar_df = False

if st.button("Mostrar todo el Dataset"):
    st.session_state.mostrar_df = not st.session_state.mostrar_df
    
if st.session_state.mostrar_df:
    st.dataframe(df, use_container_width=True)  
    
@st.cache_resource
def load_classification_model():
    return joblib.load("models\pipeline_calsification.joblib")

model = load_classification_model()

st.header("Predicción de la Calidad del Corte")
st.write("Introduce las características del diamante para predecir su calidad de corte.")

with st.form("diamonds_classification_form"):
    carat = st.slider("Peso en Quilates (carat)", 0.1, 5.0, float(df['carat'].mean()), 0.01)
    color = st.selectbox("Color del Diamante (color)", df["color"].unique())
    clarity = st.selectbox("Claridad del Diamante (clarity)", df["clarity"].unique())
    depth = st.slider("Profundidad (%) (depth)", 50.0, 75.0, float(df['depth'].mean()), 0.1)
    table = st.slider("Proporción de la Tabla (%) (table)", 50.0, 80.0, float(df['table'].mean()), 0.1)
    x = st.slider("Longitud (x) en mm", 0.0, 10.0, float(df['x'].mean()), 0.1)
    y = st.slider("Ancho (y) en mm", 0.0, 10.0, float(df['y'].mean()), 0.1)
    z = st.slider("Altura (z) en mm", 0.0, 10.0, float(df['z'].mean()), 0.1)

    boton_enviar = st.form_submit_button("🔮 Predecir Calidad del Corte")

if boton_enviar:
    X_new = pd.DataFrame({
        "carat": [carat],
        "color": [color],
        "clarity": [clarity],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z]
    })

    prediccion = model.predict(X_new)[0]

    # Mostrar el resultado con un mensaje visual
    st.subheader(f"✨ Predicción: **{prediccion.upper()}** ✨")

    # 🔹 Agregar un GIF según la clasificación del corte
    if prediccion.lower() == "ideal":
        st.success("🌟 ¡Tu diamante tiene el corte PERFECTO! 🌟")
        st.image("https://media.giphy.com/media/3o7WIPcHACrlW8M3Go/giphy.gif", width=300)
    elif prediccion.lower() == "premium":
        st.info("💎 ¡Este diamante tiene un corte de ALTA CALIDAD! 💎")
        st.image("https://media.giphy.com/media/26AHONQ79FdWZhAI0/giphy.gif", width=300)
    else:
        st.warning("📉 Parece que el corte del diamante no es el mejor.")
        st.image("https://media.giphy.com/media/3orieTeUbojj1Jck9C/giphy.gif", width=300)

    # 🎈 Efecto visual de globos
    st.balloons()

    # 📩 Botón para descargar la predicción
    pred_df = X_new.copy()
    pred_df["Predicted Cut"] = prediccion

    csv_data = pred_df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Descargar Predicción",
        data=csv_data,
        file_name="prediccion_corte_diamante.csv",
        mime="text/csv")
    
    
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('🏠Volver al Inicio del análisis'): 
        st.switch_page('Inicio.py')
with col2:    
    if st.button("📊 Análisis EDAs del Dataset"):
        st.switch_page("pages/1EDAs.py")  
with col3:
    if st.button("💶 Ir a Prediccón del Precio"):
        st.switch_page("pages/2 Predicción Precio.py")