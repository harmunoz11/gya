"""
********************************************************************
* Asignatura: Gestion en Almacenamiento de datos                   *
* Date = '18/14/2024'                                              *
* Description = Streamlit App - Estaciones de Servicios - MAIN     *
********************************************************************
"""

# Librerias

import streamlit as st
import pandas as pd
import pyodbc as pydb
from PIL import Image
import time
import json
import random
from datetime import datetime
import datetime
import os
import numpy as np
import requests
from tqdm import tqdm
import ast

import folium
from shapely.geometry import Polygon
import numpy as np
import geojson
import geopandas as gpd
from tqdm import tqdm
from shapely.geometry import Polygon
import shapely.wkt
from haversine import haversine, Unit
import random
import time
from pyproj import Geod

from shapely import wkt
from geopandas import datasets, GeoDataFrame, read_file, points_from_xy

from folium.plugins import MeasureControl
from folium.plugins import MarkerCluster

from streamlit_folium import folium_static
from tools import GetLatLon2,cal_dist,distance_estac,transform_df_map,marker_rest,Getkey,Conexion


## Obtiene Parametros de Conexion

YOUR_API_KEY = Getkey()

cnxn = Conexion()


image = Image.open('1_Fuel-prices.jpg')
st.sidebar.image(image , caption="Estacion Cercana",width = 256)
app_mode = st.sidebar.selectbox("Elige el modo", ["Ejecutar Aplicacion","Acerca de Nosotros"])



if app_mode == 'Ejecutar Aplicacion':

    st.title('APP - Estaciones de Servicio Cercanas')
    st.markdown('Opciones:')

    query = "SELECT [municipio] as Municipio, [nombre_comercial] as Nombre_comercial, [bandera] as Bandera, [direccion] as Direccion, [producto] as Producto, [precio] as Precio, [lat] as LAT, [long] as LNG FROM precios_combustibles;"
    df_map = pd.read_sql(query, cnxn)

    cities =  list(df_map['Municipio'].unique())

    c1,c2,c3,c4,c5 = st.columns((1,6,6,6,1))

    choose_city =  c2.selectbox("Elija Ciudad", cities)

    central_location = c2.text_input('Su ubicacion', 'CC Chipichape , Cali')

    DEVELOPER_KEY = YOUR_API_KEY

    if len(central_location) != 0 :

        R = GetLatLon2(central_location,YOUR_API_KEY)
        geo_source = R[1],R[2]

        unit = 'Km'
        rad = c4.slider('Radius',1,3,1)

        df_city = df_map[df_map['Municipio']==choose_city]
        df_city.reset_index(inplace = True)
        df_city.drop(columns = 'index',inplace = True)

        df_city =  transform_df_map(df_city)

        results = distance_estac(geo_source,df_city,rad,unit)
        results = results.reset_index()
        results = results.drop(columns = 'index')
        products =  list(results['Producto'].unique())

        gdf_stores_results = GeoDataFrame(results,
                                            geometry=points_from_xy(results.LNG,results.LAT))


        choose_products =  c3.selectbox("Tipo combustible", products)

        if c3.button('SHOW MAP'):

            gdf_stores_results2 = gdf_stores_results[gdf_stores_results['Producto']==choose_products]
            gdf_stores_results2 = gdf_stores_results2.reset_index()
            gdf_stores_results2 = gdf_stores_results2.drop(columns = 'index')
            icono = "usd"

            m = folium.Map([geo_source[0],geo_source[1]], zoom_start=15)

            # Circle
            folium.Circle(
            radius=int(rad)*1000,
            location=[geo_source[0],geo_source[1]],
            color='green',
            fill='red').add_to(m)

            # Centroid
            folium.Marker(location=[geo_source[0],geo_source[1]],
                                icon=folium.Icon(color='black', icon_color='white',
                                icon="home", prefix='glyphicon')
                                ,popup = "<b>CENTROID</b>").add_to(m)

            marker_rest(gdf_stores_results2,m,unit,choose_products,icono)

            # Renderizar mapa desde  Folium en Streamlit
            folium_static(m)













elif app_mode == "Acerca de Nosotros":
    st.title('APP - Estaciones de Servicio Cercanas')
    st.success("Elaborado por:")

    col1,col2,col3,col4 = st.columns((2,1,2,1))
    col1.markdown('* **ANGIE TATIANA APARICIO OCHOA**')
    col1.markdown('* **ALEJANDRO GOMEZ TUSARMA**')
    col1.markdown('* **JORGE CASTAÑO LOPEZ**')
    col1.markdown('* **HAROLD MUÑOZ**')
    image2 = Image.open('profile.jpg')
    col3.image(image2,width=230)