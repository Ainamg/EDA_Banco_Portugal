import pandas as pd

def eda_preliminar (df):
    display (df.sample(5))

    print('---------------------')

    print('INFO')

    display(df.info())

    print('---------------------')

    print('NULOS')

    display(round(df.isnull().sum()/df.shape[0] * 100,2))

    print('---------------------')

    print('DUPLICADOS')

    print(df.duplicated().sum())

    print('---------------------')

    print('VALUE COUNTS')

    for col in df.select_dtypes(include ='O').columns:
        print(df[col].value_counts())
        print('---------------------------------')


def valores_minus (df):
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.lower() # Convertir a minúsculas


def zeros (df, lista_col): 

    for col in lista_col:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace('.0', '', regex=False)


def puntos (df, lista_col):

    for col in lista_col:
        df[col] = df[col].astype(str).str.replace('.', ',', regex=False)


def convertir_columnas (df):

    for col in df.columns:
        for dtype in [float, int]:
            try: 
                df[col] = df[col].astype(dtype)
            except:
                pass

        try:
            df[col] = pd.to_datetime(df[col], format='%d-%m-%Y')
        except:
            pass 

