import streamlit as st 
import pickle
import numpy as np 
import pandas as pd 
import time 
from PIL import Image
import base64

classifier = pickle.load(open("xgb_model.sav", "rb"))

plantuu = ('OpenRetail Microempresa',
 'Plan Tuu',
 'Plan Tuu+',
 'Simple')

mcc = ('AGENCIA_DE_VIAJES',
 'AGENTES_ENCARGADOS_DE_LAS_PROPIEDADES',
 'AMBULANCIAS',
 'ANIMALES_DOMESTICOS',
 'ARTESANIA',
 'ARTES_GRAFICAS',
 'ARTICULOS_DEPORTIVOS',
 'ARTICULOS_ORTOPEDICOS',
 'BALDOSAS_Y_PISOS',
 'BANQUETEROS',
 'BARES_NIGHT_CLUB_DISCOTEQUES',
 'BOTILLERIAS_VINAS',
 'CAMPOS_DE_ATLETISMO_Y_DEPORTES',
 'CARNICERIAS_FRIGORIFICOS',
 'CARPAS',
 'CLINICAS',
 'CLINICAS_VETERINARIAS',
 'CLUBES_SOCIALES',
 'COMPRAVENTA_AUTOMOVILES',
 'COMPRAVENTA_DE_MOTOS',
 'COMP__EQUIP_PERIFERICO_SOFTWARE',
 'CONFITERIAS',
 'CONTRATISTAS',
 'DENTISTAS',
 'EQUIPOS_HERRAMIENTAS_Y_ARRIENDOS',
 'ESTACIONAMIENTO_DE_AUTOMOVILES',
 'FARMACIAS',
 'FLORERIAS',
 'FOTOCOPIAS',
 'GARAGES',
 'HOTELES',
 'INSTRUMENTOS_MUSICALES',
 'INSUMOS_Y_SUMINISTROS_INDUSTR_',
 'JARDINES_BOTANICOS',
 'JOYERIAS_Y_RELOJERIAS',
 'JUGUETERIAS',
 'LABORATORIOS_MEDICOS_Y_DENTALES',
 'LAVANDERIAS',
 'LIBRERIAS',
 'MARRIOTT',
 'MATERIALES_PARA_CONSTRUCCION',
 'MUEBLERIAS',
 'NEUMATICOS',
 'OPTICAS',
 'ORGANIZACIONES_DE_CARIDAD',
 'OTRAS_TIENDAS_DE_ALIMENTOS',
 'OTROS_ARTICULOS_PARA_EL_HOGAR',
 'OTROS_CONTRATISTAS_ESPECIALIZADOS',
 'OTROS_LUGARES_DE_RECREACION',
 'OTROS_NO_CLASIFICADOS',
 'OTROS_SERVICIOS_DE_TRANSPORTE',
 'OTROS_SERVICIOS_PROFESIONALES',
 'PANADERIAS',
 'PARQUES_DE_ENTRETENCIONES',
 'PELETERIAS',
 'PELUQUERIAS_Y_SALONES_DE_BELLEZA',
 'PERFUMERIAS',
 'PUBLICACIONES_E_IMPRESION',
 'RADIO_TELEVISION_EQUIPO_STEREO',
 'REPUESTOS_Y_ACCESORIOS_AUTOMOVILES',
 'RESTAURANT_FAST_FOOD',
 'SALONES_ESCUELAS_Y_ESTUDIOS_DE_BAILE',
 'SASTRERIAS',
 'SERVICIOS_DE_TELECOMUNICACIONES',
 'SERVICIO_DE_ASEO',
 'SERVICIO_LUZ_AGUA_TELEFONO_GAS',
 'SERV_CORREDORES_PIERCING_TATUAJE_OTRO',
 'SUPERMERCADOS',
 'TEATROS_Y_CINES',
 'TIENDAS_DE_BICICLETAS',
 'TIENDAS_DE_CRISTAL_Y_ARTICULOS_DE_VIDRIO',
 'TIENDAS_DE_DEPARTAMENTO_SSS',
 'TIENDAS_DE_MATERIALES_PARA_EL_HOGAR',
 'TIENDAS_LIBRES_DE_IMPUESTO',
 'TIMESHARES_TIEMPO_COMPARTIDO_',
 'VENTA_DE_FICHAS_DE_JUEGO',
 'VESTUARIO_HOMBRES__MUJERES_Y_NINOS',
 'ZAPATERIAS')

lista_signif = ['AGENCIA_DE_VIAJES',
 'AGENTES_ENCARGADOS_DE_LAS_PROPIEDADES',
 'AMBULANCIAS',
 'ANIMALES_DOMESTICOS',
 'ARTESANIA',
 'ARTES_GRAFICAS',
 'ARTICULOS_DEPORTIVOS',
 'ARTICULOS_ORTOPEDICOS',
 'BALDOSAS_Y_PISOS',
 'BANQUETEROS',
 'BARES_NIGHT_CLUB_DISCOTEQUES',
 'BOTILLERIAS_VINAS',
 'CAMPOS_DE_ATLETISMO_Y_DEPORTES',
 'CARNICERIAS_FRIGORIFICOS',
 'CARPAS',
 'CLINICAS',
 'CLINICAS_VETERINARIAS',
 'CLUBES_SOCIALES',
 'COMPRAVENTA_AUTOMOVILES',
 'COMPRAVENTA_DE_MOTOS',
 'COMP__EQUIP_PERIFERICO_SOFTWARE',
 'CONFITERIAS',
 'CONTRATISTAS',
 'DENTISTAS',
 'EQUIPOS_HERRAMIENTAS_Y_ARRIENDOS',
 'ESTACIONAMIENTO_DE_AUTOMOVILES',
 'FARMACIAS',
 'FLORERIAS',
 'FOTOCOPIAS',
 'GARAGES',
 'HOTELES',
 'INSTRUMENTOS_MUSICALES',
 'INSUMOS_Y_SUMINISTROS_INDUSTR_',
 'JARDINES_BOTANICOS',
 'JOYERIAS_Y_RELOJERIAS',
 'JUGUETERIAS',
 'LABORATORIOS_MEDICOS_Y_DENTALES',
 'LAVANDERIAS',
 'LIBRERIAS',
 'MARRIOTT',
 'MATERIALES_PARA_CONSTRUCCION',
 'MUEBLERIAS',
 'NEUMATICOS',
 'OPTICAS',
 'ORGANIZACIONES_DE_CARIDAD',
 'OTRAS_TIENDAS_DE_ALIMENTOS',
 'OTROS_ARTICULOS_PARA_EL_HOGAR',
 'OTROS_CONTRATISTAS_ESPECIALIZADOS',
 'OTROS_LUGARES_DE_RECREACION',
 'OTROS_NO_CLASIFICADOS',
 'OTROS_SERVICIOS_DE_TRANSPORTE',
 'OTROS_SERVICIOS_PROFESIONALES',
 'PANADERIAS',
 'PARQUES_DE_ENTRETENCIONES',
 'PELETERIAS',
 'PELUQUERIAS_Y_SALONES_DE_BELLEZA',
 'PERFUMERIAS',
 'PUBLICACIONES_E_IMPRESION',
 'RADIO_TELEVISION_EQUIPO_STEREO',
 'REPUESTOS_Y_ACCESORIOS_AUTOMOVILES',
 'RESTAURANT_FAST_FOOD',
 'SALONES_ESCUELAS_Y_ESTUDIOS_DE_BAILE',
 'SASTRERIAS',
 'SERVICIOS_DE_TELECOMUNICACIONES',
 'SERVICIO_DE_ASEO',
 'SERVICIO_LUZ_AGUA_TELEFONO_GAS',
 'SERV_CORREDORES_PIERCING_TATUAJE_OTRO',
 'SUPERMERCADOS',
 'TEATROS_Y_CINES',
 'TIENDAS_DE_BICICLETAS',
 'TIENDAS_DE_CRISTAL_Y_ARTICULOS_DE_VIDRIO',
 'TIENDAS_DE_DEPARTAMENTO_SSS',
 'TIENDAS_DE_MATERIALES_PARA_EL_HOGAR',
 'TIENDAS_LIBRES_DE_IMPUESTO',
 'TIMESHARES_TIEMPO_COMPARTIDO_',
 'VENTA_DE_FICHAS_DE_JUEGO',
 'VESTUARIO_HOMBRES__MUJERES_Y_NINOS',
 'ZAPATERIAS',
 'OpenRetail Microempresa',
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
    porcentajeComision = st.number_input("Porcentaje Comision", min_value=0.0, key="5", step=1., format="%.2f")
    codSII = st.number_input("Código de actividad", min_value=0, key="6")
    MCC = st.selectbox("MCC", mcc, help = "lorem ipsum dolor et sit amet")
    credito = st.number_input("Cantidad de transacciones con tarjeta de crédito", min_value=0, key="7")
    debito = st.number_input("Cantidad de transacciones con tarjeta de débito", min_value=0, key="8")
    has_hes = st.selectbox("Ha sufrido incidencias?", (1,0), help = "lorem ipsum dolor et sit amet")
    planTUU = st.selectbox("Plan asociado", plantuu, help = "lorem ipsum dolor et sit amet") 
    compra_inicio = st.number_input("Tiempo (en días) desde que compró e inició la certificación", min_value=1, key="9")
    certifDuration = st.number_input("Tiempo (en días) que duró su proceso de certificación", min_value=1, key="11")
    timeasclient_compra = st.number_input("Tiempo (en días) como cliente desde que compró", min_value=1, key="12")

    dictionary = dict.fromkeys(lista_signif, 0)
    dictionary["montoTotal"] = montoTotal
    dictionary["cantidadTransacciones"] = cantidadTransacciones
    dictionary["porcentajeComision"] = porcentajeComision
    dictionary["codSII"] = codSII
    dictionary["debito"] = debito
    dictionary["credito"] = credito
    dictionary["has_hes"] = has_hes
    dictionary["compra_inicio"] = compra_inicio
    dictionary["certifDuration"] = certifDuration
    dictionary["timeasclient_compra"] = timeasclient_compra
    dictionary = asignar_valores(dictionary, MCC)
    dictionary = asignar_valores(dictionary, planTUU)

    features = pd.DataFrame(dictionary, index =[0])
    features = features[['montoTotal',
 'cantidadTransacciones',
 'porcentajeComision',
 'codSII',
 'debito',
 'credito',
 'has_hes',
 'compra_inicio',
 'certifDuration',
 'timeasclient_compra',
 'AGENCIA_DE_VIAJES',
 'AGENTES_ENCARGADOS_DE_LAS_PROPIEDADES',
 'AMBULANCIAS',
 'ANIMALES_DOMESTICOS',
 'ARTESANIA',
 'ARTES_GRAFICAS',
 'ARTICULOS_DEPORTIVOS',
 'ARTICULOS_ORTOPEDICOS',
 'BALDOSAS_Y_PISOS',
 'BANQUETEROS',
 'BARES_NIGHT_CLUB_DISCOTEQUES',
 'BOTILLERIAS_VINAS',
 'CAMPOS_DE_ATLETISMO_Y_DEPORTES',
 'CARNICERIAS_FRIGORIFICOS',
 'CARPAS',
 'CLINICAS',
 'CLINICAS_VETERINARIAS',
 'CLUBES_SOCIALES',
 'COMPRAVENTA_AUTOMOVILES',
 'COMPRAVENTA_DE_MOTOS',
 'COMP__EQUIP_PERIFERICO_SOFTWARE',
 'CONFITERIAS',
 'CONTRATISTAS',
 'DENTISTAS',
 'EQUIPOS_HERRAMIENTAS_Y_ARRIENDOS',
 'ESTACIONAMIENTO_DE_AUTOMOVILES',
 'FARMACIAS',
 'FLORERIAS',
 'FOTOCOPIAS',
 'GARAGES',
 'HOTELES',
 'INSTRUMENTOS_MUSICALES',
 'INSUMOS_Y_SUMINISTROS_INDUSTR_',
 'JARDINES_BOTANICOS',
 'JOYERIAS_Y_RELOJERIAS',
 'JUGUETERIAS',
 'LABORATORIOS_MEDICOS_Y_DENTALES',
 'LAVANDERIAS',
 'LIBRERIAS',
 'MARRIOTT',
 'MATERIALES_PARA_CONSTRUCCION',
 'MUEBLERIAS',
 'NEUMATICOS',
 'OPTICAS',
 'ORGANIZACIONES_DE_CARIDAD',
 'OTRAS_TIENDAS_DE_ALIMENTOS',
 'OTROS_ARTICULOS_PARA_EL_HOGAR',
 'OTROS_CONTRATISTAS_ESPECIALIZADOS',
 'OTROS_LUGARES_DE_RECREACION',
 'OTROS_NO_CLASIFICADOS',
 'OTROS_SERVICIOS_DE_TRANSPORTE',
 'OTROS_SERVICIOS_PROFESIONALES',
 'PANADERIAS',
 'PARQUES_DE_ENTRETENCIONES',
 'PELETERIAS',
 'PELUQUERIAS_Y_SALONES_DE_BELLEZA',
 'PERFUMERIAS',
 'PUBLICACIONES_E_IMPRESION',
 'RADIO_TELEVISION_EQUIPO_STEREO',
 'REPUESTOS_Y_ACCESORIOS_AUTOMOVILES',
 'RESTAURANT_FAST_FOOD',
 'SALONES_ESCUELAS_Y_ESTUDIOS_DE_BAILE',
 'SASTRERIAS',
 'SERVICIOS_DE_TELECOMUNICACIONES',
 'SERVICIO_DE_ASEO',
 'SERVICIO_LUZ_AGUA_TELEFONO_GAS',
 'SERV_CORREDORES_PIERCING_TATUAJE_OTRO',
 'SUPERMERCADOS',
 'TEATROS_Y_CINES',
 'TIENDAS_DE_BICICLETAS',
 'TIENDAS_DE_CRISTAL_Y_ARTICULOS_DE_VIDRIO',
 'TIENDAS_DE_DEPARTAMENTO_SSS',
 'TIENDAS_DE_MATERIALES_PARA_EL_HOGAR',
 'TIENDAS_LIBRES_DE_IMPUESTO',
 'TIMESHARES_TIEMPO_COMPARTIDO_',
 'VENTA_DE_FICHAS_DE_JUEGO',
 'VESTUARIO_HOMBRES__MUJERES_Y_NINOS',
 'ZAPATERIAS',
 'OpenRetail Microempresa',
 'Plan Tuu',
 'Plan Tuu+',
 'Simple']]
    predecir = st.button("Predice el Cluster")
    if predecir : 
        prediction = classifier.predict(features)
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100): 
            latest_iteration.text(f'Estimando cluster...{i+1}%')
            bar.progress(i+1)
            time.sleep(0.1)
        st.success("El resultado de la predicción para el comercio RUT {} es : {}".format(rut, prediction))
        col1, col2, col3 = st.columns([1,2,1])