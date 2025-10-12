# Importaciones
import pandas as pd
import numpy as np

def calcular_solo_col_nul(dataframe, umbral=10):
    columns_with_nulls = dataframe.columns[dataframe.isnull().any()] # Filtrar columnas con nulos

    # Crear un DataFrame con las columnas, sus tipos, al cantidad de nulos y el porcentaje de nulos
    null_columns_info = pd.DataFrame({
        'Column': columns_with_nulls,
         'DataType': [dataframe[col].dtype for col in columns_with_nulls],
         'NullCount': [dataframe[col].isnull().sum() for col in columns_with_nulls],
         'Null%': [((dataframe[col].isnull().sum() / dataframe.shape[0]) * 100) for col in columns_with_nulls]
    })

    # Mostrar la lista resultante
    display(null_columns_info)
    high_null_cols = null_columns_info[null_columns_info['Null%'] > umbral]['Column'].tolist()
    low_null_cols = null_columns_info[null_columns_info['Null%'] <= umbral]['Column'].tolist()
    return high_null_cols, low_null_cols

