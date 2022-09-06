import streamlit as st 
import pickle
import numpy as np 
import pandas as pd 
import time 
from PIL import Image
import base64

classifier = pickle.load(open("xgb_model.sav", "rb"))

plantuu = ("Plan Tuu", "Paln Tuu+", "Simple", "OpenRetail Microempresa")

mcc = (' MUJERES Y NINOS',
 'AGENCIA DE VIAJES',
 'AGENTES ENCARGADOS DE LAS PROPIEDADES',
 'AGUA',
 'AMBULANCIAS',
 'ANIMALES DOMESTICOS',
 'ARTES GRAFICAS',
 'ARTESANIA',
 'ARTICULOS DEPORTIVOS',
 'ARTICULOS ORTOPEDICOS',
 'BALDOSAS Y PISOS',
 'BANQUETEROS',
 'BARES',
 'BOTILLERIAS',
 'CAMPOS DE ATLETISMO Y DEPORTES',
 'CARNICERIAS',
 'CARPAS',
 'CLINICAS',
 'CLINICAS VETERINARIAS',
 'CLUBES SOCIALES',
 'COMP. EQUIP.PERIFERICO',
 'COMPRAVENTA AUTOMOVILES',
 'COMPRAVENTA DE MOTOS',
 'CONFITERIAS',
 'CONTRATISTAS',
 'DENTISTAS',
 'DISCOTEQUES',
 'EQUIPO STEREO',
 'EQUIPOS HERRAMIENTAS Y ARRIENDOS',
 'ESTACIONAMIENTO DE AUTOMOVILES',
 'FARMACIAS',
 'FLORERIAS',
 'FOTOCOPIAS',
 'FRIGORIFICOS',
 'GARAGES',
 'GAS',
 'HOTELES',
 'INSTRUMENTOS MUSICALES',
 'INSUMOS Y SUMINISTROS INDUSTR.',
 'JARDINES BOTANICOS',
 'JOYERIAS Y RELOJERIAS',
 'JUGUETERIAS',
 'LABORATORIOS MEDICOS Y DENTALES',
 'LAVANDERIAS',
 'LIBRERIAS',
 'LUZ',
 'MARRIOTT',
 'MATERIALES PARA CONSTRUCCION',
 'MUEBLERIAS',
 'NEUMATICOS',
 'NIGHT CLUB',
 'OPTICAS',
 'ORGANIZACIONES DE CARIDAD',
 'OTRAS TIENDAS DE ALIMENTOS',
 'OTRO',
 'OTROS ARTICULOS PARA EL HOGAR',
 'OTROS CONTRATISTAS ESPECIALIZADOS',
 'OTROS LUGARES DE RECREACION',
 'OTROS NO CLASIFICADOS',
 'OTROS SERVICIOS DE TRANSPORTE',
 'OTROS SERVICIOS PROFESIONALES',
 'PANADERIAS',
 'PARQUES DE ENTRETENCIONES',
 'PELETERIAS',
 'PELUQUERIAS Y SALONES DE BELLEZA',
 'PERFUMERIAS',
 'PIERCING',
 'PUBLICACIONES E IMPRESION',
 'RADIO',
 'REPUESTOS Y ACCESORIOS AUTOMOVILES',
 'RESTAURANT FAST FOOD',
 'SALONES ESCUELAS Y ESTUDIOS DE BAILE',
 'SASTRERIAS',
 'SERV.CORREDORES',
 'SERVICIO',
 'SERVICIO DE ASEO',
 'SERVICIOS DE TELECOMUNICACIONES',
 'SOFTWARE',
 'SUPERMERCADOS',
 'TATUAJE',
 'TEATROS Y CINES',
 'TELEFONO',
 'TELEVISION',
 'TIENDAS DE BICICLETAS',
 'TIENDAS DE CRISTAL Y ARTICULOS DE VIDRIO',
 'TIENDAS DE DEPARTAMENTO SSS',
 'TIENDAS DE MATERIALES PARA EL HOGAR',
 'TIENDAS LIBRES DE IMPUESTO',
 'TIMESHARES(TIEMPO COMPARTIDO)',
 'VENTA DE FICHAS DE JUEGO',
 'VESTUARIO HOMBRES',
 'VINAS',
 'ZAPATERIAS')

lista_signif = [' MUJERES Y NINOS',
 'AGENCIA DE VIAJES',
 'AGENTES ENCARGADOS DE LAS PROPIEDADES',
 'AGUA',
 'AMBULANCIAS',
 'ANIMALES DOMESTICOS',
 'ARTES GRAFICAS',
 'ARTESANIA',
 'ARTICULOS DEPORTIVOS',
 'ARTICULOS ORTOPEDICOS',
 'BALDOSAS Y PISOS',
 'BANQUETEROS',
 'BARES',
 'BOTILLERIAS',
 'CAMPOS DE ATLETISMO Y DEPORTES',
 'CARNICERIAS',
 'CARPAS',
 'CLINICAS',
 'CLINICAS VETERINARIAS',
 'CLUBES SOCIALES',
 'COMP. EQUIP.PERIFERICO',
 'COMPRAVENTA AUTOMOVILES',
 'COMPRAVENTA DE MOTOS',
 'CONFITERIAS',
 'CONTRATISTAS',
 'DENTISTAS',
 'DISCOTEQUES',
 'EQUIPO STEREO',
 'EQUIPOS HERRAMIENTAS Y ARRIENDOS',
 'ESTACIONAMIENTO DE AUTOMOVILES',
 'FARMACIAS',
 'FLORERIAS',
 'FOTOCOPIAS',
 'FRIGORIFICOS',
 'GARAGES',
 'GAS',
 'HOTELES',
 'INSTRUMENTOS MUSICALES',
 'INSUMOS Y SUMINISTROS INDUSTR.',
 'JARDINES BOTANICOS',
 'JOYERIAS Y RELOJERIAS',
 'JUGUETERIAS',
 'LABORATORIOS MEDICOS Y DENTALES',
 'LAVANDERIAS',
 'LIBRERIAS',
 'LUZ',
 'MARRIOTT',
 'MATERIALES PARA CONSTRUCCION',
 'MUEBLERIAS',
 'NEUMATICOS',
 'NIGHT CLUB',
 'OPTICAS',
 'ORGANIZACIONES DE CARIDAD',
 'OTRAS TIENDAS DE ALIMENTOS',
 'OTRO',
 'OTROS ARTICULOS PARA EL HOGAR',
 'OTROS CONTRATISTAS ESPECIALIZADOS',
 'OTROS LUGARES DE RECREACION',
 'OTROS NO CLASIFICADOS',
 'OTROS SERVICIOS DE TRANSPORTE',
 'OTROS SERVICIOS PROFESIONALES',
 'PANADERIAS',
 'PARQUES DE ENTRETENCIONES',
 'PELETERIAS',
 'PELUQUERIAS Y SALONES DE BELLEZA',
 'PERFUMERIAS',
 'PIERCING',
 'PUBLICACIONES E IMPRESION',
 'RADIO',
 'REPUESTOS Y ACCESORIOS AUTOMOVILES',
 'RESTAURANT FAST FOOD',
 'SALONES ESCUELAS Y ESTUDIOS DE BAILE',
 'SASTRERIAS',
 'SERV.CORREDORES',
 'SERVICIO',
 'SERVICIO DE ASEO',
 'SERVICIOS DE TELECOMUNICACIONES',
 'SOFTWARE',
 'SUPERMERCADOS',
 'TATUAJE',
 'TEATROS Y CINES',
 'TELEFONO',
 'TELEVISION',
 'TIENDAS DE BICICLETAS',
 'TIENDAS DE CRISTAL Y ARTICULOS DE VIDRIO',
 'TIENDAS DE DEPARTAMENTO SSS',
 'TIENDAS DE MATERIALES PARA EL HOGAR',
 'TIENDAS LIBRES DE IMPUESTO',
 'TIMESHARES(TIEMPO COMPARTIDO)',
 'VENTA DE FICHAS DE JUEGO',
 'VESTUARIO HOMBRES',
 'VINAS',
 'ZAPATERIAS', 'OpenRetail Microempresa',
 'Plan Tuu',
 'Plan Tuu+',
 'Simple']


dictionary = dict.fromkeys(lista_signif, 0)

def asignar_valores(dicti, comp):
    for k,v in dicti.items():
        if k in comp : 
            dicti[k] = 1
    return dicti

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


def user_input_features(): 
    display_app_header(main_txt="Predictor de cluster de comercios",
                        sub_txt="Ingrese información del comercio para predecir Cluster")
    rut = st.text_input("RUT del comercio")
    montoTotal = st.number_input("Monto total de transacciones", min_value=0, key="1")
    cantidadTransacciones = st.number_input("Cantidad total de transacciones", min_value=0, key="2")
    comisionNeta = st.number_input("Monto total de comision neta", min_value=0, key="3")
    comisionIVA = st.number_input("Monto total de comision IVA", min_value=0, key ="4")
    porcentajeComision = st.number_input("Porcentaje Comision", min_value=0, key="5")
    codSII = st.number_input("Código de actividad", min_value=0, key="6")
    MCC = st.selectbox("MCC", mcc, help = "lorem ipsum dolor et sit amet")
    credito = st.number_input("Cantidad de transacciones con tarjeta de crédito", min_value=0, key="7")
    debito = st.number_input("Cantidad de transacciones con tarjeta de débito", min_value=0, key="8")
    has_hes = st.selectbox("Ha sufrido incidencias?", (1,0), help = "lorem ipsum dolor et sit amet")
    planTUU = st.selectbox("Plan asociado", plantuu, help = "lorem ipsum dolor et sit amet") 
    compra_inicio = st.number_input("Tiempo (en días) desde que compró e inició la certificación", min_value=1, key="9")
    compra_fin = st.number_input("Tiempo (en días) desde que compró y finalizó la certificación", min_value=1, key="10")
    certifDuration = st.number_input("Tiempo (en días) que duró su proceso de certificación", min_value=1, key="11")
    timeasclient_compra = st.number_input("Tiempo (en días) como cliente desde que compró", min_value=1, key="12")
    timeasclient_certificado = st.number_input("Tiempo (en días) como cliente dsde de certificadó", min_value=1, key="13")

    dictionary = dict.fromkeys(lista_signif, 0)
    dictionary["montoTotal"] = montoTotal
    dictionary["cantidadTransacciones"] = cantidadTransacciones
    dictionary["comisionNeta"] = comisionNeta
    dictionary["comisionIVA"] = comisionIVA
    dictionary["porcentajeComision"] = porcentajeComision
    dictionary["codSII"] = codSII
    dictionary["debito"] = debito
    dictionary["credito"] = credito
    dictionary["has_hes"] = has_hes
    dictionary["compra_inicio"] = compra_inicio
    dictionary["compra_fin"] = compra_fin
    dictionary["certifDuration"] = certifDuration
    dictionary["timeasclient_compra"] = timeasclient_compra
    dictionary["timeasclient_certificado"] = timeasclient_certificado
    dictionary = asignar_valores(dictionary, mcc)
    dictionary = asignar_valores(dictionary, planTUU)

    features = pd.DataFrame(dictionary, index =[0])
    predecir = st.button("Predice el Cluster")
    if predecir : 
        prediction = classifier.predict(features)
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100): 
            latest_iteration.text(f'Estimando cluster...{i+2}%')
            bar.progress(i+1)
            time.sleep(0.1)
        st.success("El resultado de la predicción para el comercio RUT {} es : {}".format(rut, prediction))
        col1, col2, col3 = st.columns([1,2,1])