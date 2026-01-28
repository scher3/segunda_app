import streamlit as st

pg_intro = st.Page('introduccion.py', tittle='Introducción')
pg_eda_intro = st.Page('seccion_eda/introduccion.py', tittle='Intro EDA')

navigation_env = st.navigation(
    {
        'Inicio': [pg_intro],
        'EDA': [pg_eda_intro]
    }
)
navigation_env.run()