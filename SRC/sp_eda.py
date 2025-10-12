import pandas as pd
import numpy as np


def calcular_nulos(df):    
    """Función para calcular numero de nulos por columna y porcentaje de nulos por columna

    Args:
        dataframe (df.pandas): dataframe a analizar
    
    Returns:
        tupla: dos series de pandas con los datos numericos de nulos y los datos porcentuales de nulos
    """
    numero_nulos = df.isnull().sum()
    porcentaje_nulos = df.isnull().sum() / df.shape[0] * 100
    return numero_nulos, porcentaje_nulos


def analisis_general_cat(df):
    """Función para realizar un análisis general de las columnas categóricas de un dataframe

    Args:
        df (df.pandas): dataframe a analizar
    
    Returns:
        None: imprime el análisis por pantalla
    """
    col_catg = df.select_dtypes(include="O").columns

    if len(col_catg) == 0:
        print("No hay columnas categóricas en el dataframe.")
    
    else: 
        for col in col_catg:
            print(f"La distribución de la columna {col.upper()}")
            print(f"Esta columna tiene {len(df[col].unique())} valores únicos")
            display(df[col].value_counts(normalize=True))
            print("--------------\n Describe")
            display(df[col].describe())
            print("--------------")
        
    