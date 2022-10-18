import streamlit as st
import base64
from PIL import Image

from predict_page import user_input_features
from main import show_main
from explore_page import show_explore


def get_base_64(bin_file):
    with open(bin_file, 'rb') as f :
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base_64(png_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])


st.sidebar.image("haulmer_logo.png") # Insertar logo_haulmer
st.sidebar.markdown("## Predictor De Cluster para Comercios")
pagina = st.sidebar.selectbox("Seleccione una vista", ("Principal", "Cluster Prediction", "Explorar datos"))

st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
    background-image: linear-gradient(#F4AC1A,#F4AC1A);
    color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


if pagina == "Cluster Prediction":
   user_input_features()

elif pagina == "Principal" : 
    show_main()

elif pagina == "Explorar datos": 
    show_explore()
