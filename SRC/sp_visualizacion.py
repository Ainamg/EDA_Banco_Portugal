import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def subplot_col_cat(df):

    #Seleccionar columnas categóricas
    cat_cols = df.select_dtypes(include=['object', 'category']).columns

    if len(cat_cols) == 0:
        print("No hay columnas categóricas para graficar.")
        return
    
    #Configurar el tamaño de la figura
    num_cols = len(cat_cols)
    rows = (num_cols + 2) // 3  # Tres columnas por fila
    fig, axes = plt.subplots(rows, 3, figsize=(15, rows * 5))
    axes = axes.flatten()  # Aplanar la matriz de ejes para facilitar el acceso

    #Generar gráficos de barras para cada columna categórica
    for i, col in enumerate(cat_cols):
        sns.countplot(data=df, x=col, ax=axes[i], hue=col, palette="tab10", legend=False)
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')
        axes[i].tick_params(axis='x', rotation=90)  # Rotar etiquetas del eje x para mejor visibilidad

    #Eliminar ejes vacíos si hay menos columnas que subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    #Ajustar diseño 
    plt.tight_layout()
    plt.show()

def subplot_col_num (dataframe, col):
    num_graph = len(col)

    num_rows = (num_graph + 2) // 2 

    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows*5))

    for i, col in enumerate(col):
        sns.histplot(data=dataframe, x=col, ax = axes[i,0], bins=200)
        axes[i,0].set_title(f'Distribución de {col}')
        axes[i,0].set_ylabel('Frecuencia')

        sns.boxplot(data=dataframe, x=col, ax = axes[i,1])
        axes[i,1].set_title(f'Boxplot de {col}')

    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()

    

    