# **Proyecto Georeferenciación de Gasolineras - Asignatura Gestion y Almacenamiento de Datos.**

## Integrantes:

* Angie Tatiana Aparicio Ochoa
* Alejandro Gómez Tusarma
* Jorge Castaño
* Harold Muñoz


## Definición: 

Existe una necesidad de identificar rápidamente las gasolineras dentro de un rango de 1 km y acceder a información detallada sobre el costo por galón y por tipo de combustible. 

Esta falta de información centralizada y accesible dificulta la toma de decisiones informadas y eficientes en la compra de combustible, lo que puede resultar en gastos innecesarios y tiempo perdido para los usuarios.

La propuesta es Identificar las gasolineras dentro de un rango de 1 km y mostrar el costo por galón y por tipo de combustible de cada estación de servicio.


## Proceso de despliegue:

Fuente de datos:

https://www.datos.gov.co/Minas-y-Energ-a/precio-mes-combustible/gjy9-tpph/about_data


## Proceso de despliegue:


Los pasos a seguir son:

1- Crear un ambiente virtual de python dentro del sistema operativo. Por ejemplo: 

python -m venv tutorial-env

2- Ejecutar el ambiente del entorno virtual:

cd Scripts
activate.bat

3- Clonar el presente reposotorio.

4- Instalación de librerias de python:

- Actualizar el PIP:

python.exe -m pip install --upgrade pip

- Instalar librerias:

python -m pip install -r requirements.txt

5- Crear una base de datos en MS SQL Server.

6- Abrir la carpeta data y descargar el script "precios_combustibles.sql" el cual debe ser ejecutado en la consola de SQL Server.

7- Editar el archivo "tools.py", dirigirse a la función "Conexion()" y colocar las credenciales de conexión a la base de datos.

8- Crear una cuenta dentro de la plataforma: https://www.here.com/

9- Una vez es dado de alta tramitar el correspondiente API KEY, luego parametrizarlo dentro del archivo "tools.py", función "Getkey()".


## Ejecutar programa:


Para lanzar el servidor web (puerto 8501) se debe ejecutar el siguiente comando desde consola, ubicándose previamente en la carpeta donde descargo el proyecto:

streamlit run app.py


## Analisis y preprocesamiento:

Dentro de la carpeta notebook se encuentra un cuaderno llamado "FinalLab (1).ipynb" el cual detalla el proceso de analisis de la fuente, transformación y enriquecimiento de la data con las coordenadas de las estaciones de servicio.


--------------------------------------------------------------------------



# Conclusiones: 

* Este proyecto nos ayudó a consumir información de diferentes fuentes y transformarla a las necesidades de nuestro proyecto.

* Por otra parte este proyecto nos permitió poner en práctica los conocimientos de transformación y enriquecimiento de datos aprendidos en la asignatura.

* En este proyecto llevamos la información previamente enriquecida y transformada a una herramienta tecnológica que le permitirá al usuario final observar y consumir dicha información de forma más sencilla e interactiva.


