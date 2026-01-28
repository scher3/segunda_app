import streamlit as st

st.title('Primer Pasos para el EDA del alquier bicis')
# Tenemos que recuperar los datos de las bicis (dataset de bicis)

# En el EDA, nos interesará saber las dimensiones del dataset,
# la distribución, la clase objetivo, los estadisticos, correlacion que exite

# Separandolo por secciones
st.markdown('''
# Modelado de patron de alquiler de bicis en ciudad Z
Esta aplicación tiene como objetivo poder modelar el alquiler de bicis futuro en la ciudad usando
varias tecnicas de ML

**Navegación** En el menú de la izquierda tienes todo lo necesario para empezar a predecir el alquiler de bicis
''')
# Para ello creamos otra pagina