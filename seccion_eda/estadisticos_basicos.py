# Tambien se puede hacer from streamlit in * (pero si hay dos 
# librerias con la misma funcion de comando utilizará la ultima cargada)
import streamlit as st
import pandas as pd
import matplotlib as plt
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
# La media de alquileres va a ser 
st.markdown('## Estadísticos básicos')
st.dataframe(df[['dteday','temp','windspeed','hum','cnt']].describe().T[['count','std','mean']]) # de df nosotros queremos las variables por tanto traspuesta de lo que queramos


st.markdown('## Distribución de las variables')

st.markdown('## Matriz de correlación')
