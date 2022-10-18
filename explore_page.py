from pandas.core.indexes.base import Index
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import os
import seaborn as sns
from PIL import Image, ImageEnhance, ImageFilter
import base64
import altair as alt

columns = (
   "montoTotal","cantidadTransacciones"
)


def display_app_header(main_txt,sub_txt,is_sidebar = False):
    """
    function to display major headers at user interface
    ----------
    main_txt: str -> the major text to be displayed
    sub_txt: str -> the minor text to be displayed 
    is_sidebar: bool -> check if its side panel or major panel
    """

    html_temp = f"""
    <h2 style = "color:#000000; text_align:center; font-weight: bold;"> {main_txt} </h2>
    <p style = "color:#191919; text_align:center;"> {sub_txt} </p>
    </div>
    """
    if is_sidebar:
        st.sidebar.markdown(html_temp, unsafe_allow_html = True)
    else: 
        st.markdown(html_temp, unsafe_allow_html = True)

def load_data():
    df = pd.read_csv("df_kmeans_cluster.csv")
    #df.drop(columns = ["Unnamed: 0"], inplace=True)
    return df 

df = load_data()

def plot_with_freq(df, col) :
    plt.figure(figsize=(10,7))
    aux_dict = df[col].value_counts().to_dict()
    y = list(aux_dict.values())
    plt.barh(*zip(*aux_dict.items()))
    for index, value in enumerate(y):
        plt.text(value, index, str(value))
    plt.title("Frecuencia de la columna {}", format(col))

def plot_hist_custom(var, titulo = ''):
    tmp = var.dropna() # Borramos, si es que existen nulls
    plt.hist(tmp, color = 'dodgerblue')
    plt.title(titulo, size = 17)
    plt.axvline(tmp.mean(), color = 'tomato', linewidth = 2,
                linestyle = '--', label = 'Media ')
    plt.legend()

def plot_hist_custom_type(df, tipo, titulo = ''):
    df_aux = df[df["Type"]==tipo]
    tmp = df_aux["Score"].dropna() # Borramos, si es que existen nulls
    plt.hist(tmp, color = 'dodgerblue')
    plt.title(titulo, size = 17)
    plt.axvline(tmp.mean(), color = 'tomato', linewidth = 2,
                linestyle = '--', label = 'Media de Score para {}'.format(tipo))
    plt.legend()


def show_explore():
    
    #st.title("Análisis Exploratorio de datos de Anime")
    display_app_header(main_txt='Análisis Exploratorio de datos de Comercio',
                       sub_txt='Análisis exploratorio de los comercios y sus características, registrados en las bases de datos de Haulmer')
    st.markdown("""
        ### Descripción 
    """)

    data_dim = st.radio('Seleccione una opción para ver cantidad',('Registros','Atributos'))
    if data_dim == 'Registros':
        st.text("Cantidad de Comercios Registrados")
        st.write(len(df))
    if data_dim == "Atributos":
        st.write(df.shape[1])

    if st.checkbox("Mostrar Atributos de los Comercios"):
        st.text("Características:")
        st.write(df.columns)

    if st.checkbox("Visualizar datos"):
        if st.button("Primeros Registros"):
            st.write(df.head())
        if st.button("Últimos Registros"):
            st.write(df.tail())

    if st.checkbox("Descripción de datos"):
        st.write(df.describe())
    
    st.markdown("""
    ### Análisis por característica
    """)

    column_selected = st.selectbox("Seleccione Columna",columns, index=2)
    
    if column_selected == "montoTotal":
        plot_hist_custom(df["montoTotal"], "")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot() 

    if column_selected == "cantidadTransacciones":
        plot_hist_custom(df["cantidadTransacciones"], "")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


    