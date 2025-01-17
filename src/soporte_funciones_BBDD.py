# Librerías para gestión de tiempos
from time import sleep
from tqdm import tqdm

# Librerías para tratamiento de datos

import pandas as pd
import pickle
import numpy as np
import re

# Librerías para captura de datos
import requests
from bs4 import BeautifulSoup


# Librerías para automatización de navegadores web con Selenium
from selenium import webdriver  
from webdriver_manager.chrome import ChromeDriverManager  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException 

# Librería para gestión de tiempos
import time

# Librería para trabajar con bases de datos SQL
import psycopg2
from psycopg2 import OperationalError, errorcodes, errors
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Librería para gestionar ficheros del sistema y archivos .env, para cargar tokens y claves
import os
import dotenv
dotenv.load_dotenv('C:\\Users\\DELL\\Git\\Proyecto_Final\\src\\.env')

# Librería para ignorar avisos
import warnings
warnings.filterwarnings("ignore") # Ignora TODOS los avisos


# -------------------------------------- #

# Este script permite navegar y extraer información de un sitio web, limpiar y organizar los datos,
# y luego interactuar con una base de datos para almacenar o recuperar información.

# -------------------------------------- #

# Importamos el usuario y contraseña que hemos guardado en el archivo .env, de modo que podamos utilizarlos como inputs de nuestra función.
dbeaver_pw = os.getenv("dbeaver_pw")
dbeaver_user = os.getenv("dbeaver_user")


def dbeaver_crear_db(database_name):
    """
    Crea una base de datos de PostgreSQL si aún no existe.

    Parámetros:
    -----------
    database_name : str
        El nombre de la base de datos a crear.

    Esta función se conecta al servidor PostgreSQL usando credenciales de usuario, verifica si una base 
    de datos con el nombre dado existe y la crea si no existe. Si ocurre un error de conexión, la función 
    imprimirá el tipo específico de error, como una contraseña incorrecta o un problema de conexión.

    Dependencias:
    -------------
    Requiere el paquete psycopg2 y las siguientes variables globales:
    - dbeaver_user: str - El nombre de usuario para conectarse a PostgreSQL.
    - dbeaver_pw: str - La contraseña asociada con el nombre de usuario.

    Retorna:
    --------
    None
    """
    print(dbeaver_user)
    print(dbeaver_pw)
    try:
        conexion = psycopg2.connect(
            dbname="postgres",
            user=dbeaver_user,
            password=dbeaver_pw,
            host="localhost",
            port="5432"
        )

        conexion.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Crear un cursor con la nueva conexión
        cursor = conexion.cursor()
        
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (database_name,))
        
        # Almacenar el resultado de fetchone; si existe, tendrá una fila, de lo contrario None
        bbdd_existe = cursor.fetchone()
        
        # Si bbdd_existe es None, crear la base de datos
        if not bbdd_existe:
            cursor.execute(f"CREATE DATABASE {database_name};")
            print(f"Base de datos {database_name} creada con éxito")
        else:
            print("La base de datos ya existe")
            
        # Cerrar el cursor y la conexión
        cursor.close()
        conexion.close()

    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("Contraseña es errónea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexión")
        else:
            print(f"Ocurrió el error {e}")


def dbeaver_conexion(database):
    """
    Establece una conexión a una base de datos DBeaver.

    Args:
        database (str): El nombre de la base de datos.

    Returns:
        connection: Un objeto de conexión a la base de datos.
    """
    try:
        conexion = psycopg2.connect(
            database=database,
            user=dbeaver_user,
            password=dbeaver_pw,
            host="localhost",
            port="5432"
        )
    except OperationalError as e:
        if e.pgcode == errorcodes.INVALID_PASSWORD:
            print("Contraseña es errónea")
        elif e.pgcode == errorcodes.CONNECTION_EXCEPTION:
            print("Error de conexión")
        else:
            print(f"Ocurrió el error {e}")

    return conexion


def dbeaver_fetch(conexion, query):
    """
    Ejecuta una consulta y obtiene los resultados en un dataframe.

    Args:
        conexion (connection): Un objeto de conexión a la base de datos.
        query (str): La consulta SQL a ejecutar.

    Returns:
        list: Los resultados de la consulta en un dataframe.
    """
    cursor = conexion.cursor()
    cursor.execute(query)
    # resultado_query = cursor.fetchall()
    # Si quisiéramos que el resultado fuera en forma de lista podríamos utilizar esta línea de código.
    # En este caso, sin embargo, nos interesa obtener directamente DFs.
    
    df = pd.DataFrame(cursor.fetchall())
    df.columns = [col[0] for col in cursor.description]

    cursor.close()
    conexion.close()

    return df


def dbeaver_commit(conexion, query, *values):
    """
    Ejecuta una consulta y realiza un commit de los cambios.

    Args:
        conexion (connection): Un objeto de conexión a la base de datos.
        query (str): La consulta SQL a ejecutar.
        *values: Los valores a incluir en la consulta.

    Returns:
        str: Un mensaje de confirmación después del commit.
    """
    cursor = conexion.cursor()
    cursor.execute(query, *values)
    conexion.commit()
    cursor.close()
    conexion.close()
    return print("Commit realizado")


def dbeaver_commitmany(conexion, query, *values):
    """
    Ejecuta múltiples consultas y realiza un commit de los cambios.

    Args:
        conexion (connection): Un objeto de conexión a la base de datos.
        query (str): La consulta SQL a ejecutar.
        *values: Los valores a incluir en la consulta.

    Returns:
        str: Un mensaje de confirmación después del commit.
    """
    cursor = conexion.cursor()
    cursor.executemany(query, *values)
    conexion.commit()
    cursor.close()
    conexion.close()
    return print("Commit realizado")


def csvs_a_tuplas(rutas_archivos):
    """
    Lee múltiples archivos CSV y convierte sus datos en listas de tuplas.

    Parámetros:
    rutas_archivos (list): Lista de rutas de archivos CSV que se leerán.

    Retorna:
    list: Una lista de listas de tuplas, donde cada sublista corresponde a un archivo CSV.
          Cada tupla representa una fila de datos sin el índice.

    Ejemplo:
    rutas_archivos = ["ruta/archivo1.csv", "ruta/archivo2.csv"]
    listas_tuplas = csvs_a_tuplas(rutas_archivos)
    # listas_tuplas será una lista que contiene una lista de tuplas para cada archivo.

    """
    listas_tuplas = []
    for ruta in rutas_archivos:
        df = pd.read_csv(ruta, index_col=0)
        tuplas_df = list(df.itertuples(index=False, name=None))
        listas_tuplas.append(tuplas_df)
    return listas_tuplas
