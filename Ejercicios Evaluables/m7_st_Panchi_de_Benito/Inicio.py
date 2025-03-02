import streamlit as st


st.set_page_config(
    page_title='DIAMONDS', 
    page_icon='💎', 
    layout='wide', 
    initial_sidebar_state='collapsed')


st.markdown(
    "<h1 style='text-align: center; color: #ff5733; font-size: 46px;'>Análisis de Diamantes<br></h1>", 
    unsafe_allow_html=True
    )

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Descubrir análisis EDAs'):
        st.switch_page('pages/1EDAs.py')
    st.image("Images\diamantes 1.png", width=180)
        
with col2:
    if st.button('Predcciones del Precio'):
        st.switch_page("pages/2 Predicción Precio.py")
    st.image("Images\Regresion.jpeg", width=180)
        
with col3:
    if st.button('Clasificación por Corte'):
        st.switch_page("pages/3 Clasificacion Corte.py")
    st.image("Images\clasificacion.webp", width=180)
    
st.markdown("""
    <style>
    .stButton>button {
        background-color: #FF5733;
        color: black;
        font-size: 16px;
        padding: 10px 10px;
        border-radius: 20px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1E90FF
    }
    </style>
""", unsafe_allow_html=True)

with st.expander("ℹ️ **Haz clic aquí para ver más información sobre el análisis**."):
    st.write("""
    **Este análisis de diamantes** se centra en explorar la relación entre el peso en quilates, la calidad del corte, 
    el color, la claridad y el precio a traves de EDA (Exploratory Data Analysis). 
    
    EDA es el proceso de examinar, visualizar y resumir datos para entender sus patrones y 
    generar hipótesis para posteriormente aplicar modelos para llevar a cabo predicciones o clasificaciones 
    a través de técnicas de Machine Learning, como regresión para estimar precios y clasificación para evaluar la calidad del corte. 
      
    🔹 **¿Qué encontrarás en este estudio?**  
    - Exploración de datos con gráficos interactivos.  
    - Modelos de regresión para predecir precios de diamantes.  
    - Clasificación de diamantes según su calidad de corte.  
    
    🎯 **Objetivo:** Ayudar a tomar decisiones informadas sobre precios y calidad del corte.
    """)
    st.caption("Fuente de datos: [Kaggle](https://www.kaggle.com/shivam2503/diamonds) | [Giphy](https://giphy.com) | [Dalle3](https://openai.com/index/dall-e-3/)")
    st.caption("Proyecto realizado como desarrollo del Modulo 7 del Bootcamp Data Science. Hack a Boss | NTTData. FEB-2025.")

with st.expander("🤓 **Atribución de Autoría**."):
    st.write("**Autoría:** Francisca (Panchi) de Benito Ducos")
    st.write("**Contacto:** [franciscadebenito@gmail.com](mailto:franciscadebenito@gmail.com)")
    st.write(" **LinkedIn:** [linkedin.com/in/franciscadebenitoducos](https://linkedin.com/in/franciscadebenitoducos)")
    st.write("**GitHub:** https://github.com/Panchi-db")  

