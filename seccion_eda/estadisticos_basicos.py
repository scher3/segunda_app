# Tambien se puede hacer from streamlit in * (pero si hay dos 
# librerias con la misma funcion de comando utilizará la ultima cargada)
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Lorem ipsum')

# Podemos ir definiendo las cosas que vamos a hacer
# Vamos a empezar a mostrar los datos crudos del dataset

st.markdown('## Datos Crudos del dataset')
df =pd.read_csv('bike_dataset_hour.csv')   # cargar el dateframe
st.dataframe(df.head(500))                 # mostramos los 500 primeros del dataframe,pues si son mas se trabaria

# Vamos a mostrar los estadísticos
st.markdown('## Datos sobre el dataset')
#st.markdown(df.describe().T) #da la info en un string
st.dataframe(df.describe().T) #da la info en un dataframe

# Ahora vamos a trabajar sobre los estadisticos basicos, no sin antes analizar los datos
# Estamos trabajando con datos normalizados
# La mediana no va a ser útil
# La media de alquileres por hora es de 189.46308763450142
st.markdown('## Estadísticos básicos')
st.dataframe(df[['dteday','temp','windspeed','hum','cnt']].describe().T[['count','std','mean']]) # de df nosotros queremos las variables por tanto traspuesta de lo que queramos

# Vamos a hacer una representacion de los datos
st.markdown('## Distribución de las variables')

# No funciona pues tenemos que cargar los datos en columnas
cols = st.columns(3)
with cols[0]:
    fig, ax= plt.subplots()       # si ponemos fig, ax= plt.figure(figsize=(8,5)) 
    sns.histplot(df['temp'], kde=True)       # una sola figura
    plt.title('Distribución Temp.')
    st.pyplot(fig)                # Pyplot se encarga de cargar la figura

with cols[1]:
    fig, ax= plt.subplots()       # figura del histograma
    sns.histplot(df['hum'], kde=True)
    plt.title('Distribución Humedad.')
    st.pyplot(fig)             # Pyplot se encarga de cargar la figura

with cols[2]:
    fig, ax= plt.subplots()       # figura del histograma
    sns.histplot(df['windspeed'], kde=True)
    plt.title('Distribución velocidad del viento.')
    st.pyplot(fig)             # Pyplot se encarga de cargar la figura

st.markdown('---')
# Vamos a hacer una unica columna
cols_target, = st.columns(1)
with cols_target:
    fig, ax= plt.subplots()       # figura del histograma
    sns.histplot(df['cnt'], kde=True)
    plt.title('Distribución de ventas.')
    st.pyplot(fig)             # Pyplot se encarga de cargar la figura

# a veces no tiene sentido calcular la correlacion de todas las columnas
# solo la queremos de las columnas numericas.
st.markdown('## Matriz de correlación')
# anhadimos las columnas numericas
cols_interes = ['temp', 'hum', 'windspeed','casual', 'cnt']
# st.markdown(df[cols_interes].corr())   # como string
st.dataframe(df[cols_interes].corr())                 # como panda trabaja con dataframe todo lo que trabaja lo es

# Conclusiones: hay dos correlaciones fuerte directas, y dos inversas
# Si tuvieramos una matriz más grande, realizamos un mapa de calor
matriz_correlacion = df[cols_interes].corr()

col, = st.columns(1)
with col:
    fig, ax = plt.subplots()
    sns.heatmap(matriz_correlacion, annot=True)
    plt.title('Matriz correlacion con cnt')
    st.pyplot(fig)

# Hay casos en los que cuesta hacer una diferenciacion entre colores
# Por tanto preferimos poner en cada heatmap anotaciones annot=True


# Nos haria falta una sesión de entrenamiento y una sesion de demo,
# con esto podriamos formas un proyecto