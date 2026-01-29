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
cols = st.columns(1)
with cols[0]:
    fig, ax= plt.subplots()       # si ponemos fig, ax= plt.figure(figsize=(8,5)) 
    sns.histplot(df['temp'], kde=True)       # una sola figura
    plt.title('Distribución Temp.')
    st.pyplot(fig)                # Pyplot se encarga de cargar la figura

with cols[1]:
    fig, ax= plt.subplots()       # figura del histograma
    sns.histplot(df['temp'], kde=True)
    plt.title('Distribución Humedad.')
    st.pyplot(fig)             # Pyplot se encarga de cargar la figura

with cols[2]:
    fig, ax= plt.subplots()       # figura del histograma
    sns.histplot(df['temp'], kde=True)
    plt.title('Distribución velocidad del viento.')
    st.pyplot(fig)             # Pyplot se encarga de cargar la figura


st.markdown('## Matriz de correlación')
