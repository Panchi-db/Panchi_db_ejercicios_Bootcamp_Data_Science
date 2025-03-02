import streamlit as st
import joblib
import seaborn as sns
import pandas as pd 


@st.cache_data
def load_diamonds_data():
    df = pd.read_csv("diamonds.csv")
    df.drop(columns=["Unnamed: 0"], inplace=True, errors="ignore")
    return df

st.set_page_config(
    page_title='Regresión', 
    page_icon='🔮',
    initial_sidebar_state='collapsed')


st.title('Predicción del precio | Regresión')

df = load_diamonds_data()
st.header("Dataset Diamonds:")
st.table(df.head()) 


if "mostrar_df" not in st.session_state:
    st.session_state.mostrar_df = False

if st.button("Mostrar todo el Dataset"):
    st.session_state.mostrar_df = not st.session_state.mostrar_df
    
if st.session_state.mostrar_df:
    st.dataframe(df, use_container_width=True)  
    
@st.cache_resource
def load_scikit_model():
    return joblib.load('models\pipeline_regression.joblib')

model = load_scikit_model()    


st.header('Predicción del precio de un diamante')
st.write('Completa los valores dolicitados para obtener una predicción del precio de tu diamante:')   

with st.form("diamonds_form"):

    carat = st.slider(
        'Introduce el peso en Quilates (carat)',
        min_value=0.1, max_value=5.0, 
        value=float(df['carat'].mean()),  # Valor predeterminado basado en el dataset
        step=0.01
    )

    cut = st.selectbox('Selecciona la calidad del Corte (cut)', df['cut'].unique())
    color = st.selectbox('Selecciona el Color del diamante (color)', df['color'].unique())
    clarity = st.selectbox('Selecciona la Claridad del diamante (clarity)', df['clarity'].unique())


    depth = st.slider(
        'Introduce la Profundidad (%) (depth)',
        min_value=50.0, max_value=75.0, 
        value=float(df['depth'].mean()), 
        step=0.1
    )

    table = st.slider(
        'Introduce la proporción de la Tabla (%) (table)',
        min_value=50.0, max_value=80.0, 
        value=float(df['table'].mean()), 
        step=0.1
    )
    
    
    x = st.slider(
        'Introduce la longitud (x) en mm',
        min_value=0.0, max_value=10.0, 
        value=float(df['x'].mean()), 
        step=0.1
    )

    y = st.slider(
        'Introduce el ancho (y) en mm',
        min_value=0.0, max_value=10.0, 
        value=float(df['y'].mean()), 
        step=0.1
    )

    z = st.slider(
        'Introduce la altura (z) en mm',
        min_value=0.0, max_value=10.0, 
        value=float(df['z'].mean()), 
        step=0.1
    )

    boton_enviar = st.form_submit_button("💰 Generar Predicción")

    if boton_enviar:
        X_new = pd.DataFrame({
            'carat': [carat],
            'cut': [cut],
            'color': [color],
            'clarity': [clarity],
            'depth': [depth],
            'table': [table],
            'x': [x],
            'y': [y],
            'z': [z]
        })

        prediccion = model.predict(X_new)[0]

        precio_medio = df['price'].mean()
        delta_value = prediccion - precio_medio

        col1, col2 = st.columns(2)
        col1.metric('💎💲 Precio Estimado del Diamante', value=f'{prediccion:.2f} $', delta=f'{delta_value:.2f} $')
        col2.metric('💲 Precio Medio en el Dataset', value=f'{precio_medio:.2f} $')



        if prediccion > 10000:
            st.success("✨ ¡Este es un diamante de LUJO! 💎🔥")
            st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWFkaDNhMGozMXJ2dnNlNHczMnlmdjlqYWlhZHYwNTlxOGdncG51diZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LUhUvH4BsfE9USnlPd/giphy.gif",width=100, use_container_width =True)
            st.balloons(repath = True)
            
        elif prediccion > 3932:
            st.info("💠 ¡Tu diamante tiene un gran valor! 📈")
            st.image("https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaTlobmQxaDAzcHRrcGlrcGp0dnZnYnBqbnVicTBya3RzaXphaG9iNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26DOoDwdNGKAg6UKI/giphy.gif",width=100, use_container_width=True)
           
        else:
            st.warning("📉 Este es tu limite? 🥲")
            st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGR6eHZxczZpemQ3ZmkyNXRxY2M1N3BxdmZxdGNycWprMWI3OW82aCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/IT8d252aTz13G/giphy.gif", width=10, use_container_width =True)
            st.snow()


col1, col2, col3 = st.columns(3)

with col1:
    if st.button('🏠Volver al Inicio del análisis'): 
        st.switch_page('Inicio.py')
with col2:    
    if st.button("📊 Análisis EDAs del Dataset"):
        st.switch_page("pages/1EDAs.py")  
with col3:
    if st.button("💎Ir a Clasificación por Corte"):
        st.switch_page("pages/3 Clasificacion Corte.py")