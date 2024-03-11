#1. SMART QUESTION

    #¿Cuantos y cuales son los insumos que se han comprado por encima de la cantidad configurada de compra en el último año de manera que pueda 
    #hacer más eficiente el proceso de abastecimiento de materiales?

#2. Importar librerías 

    #Importamos las librerías para el manejo de datasets
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as mp
    import seaborn as sb
    from locale import normalize

    #Importamos los paquetes sickit learn para ML

    # Libreria para la creación de Pipeline
    from sklearn.pipeline import Pipeline

    # Importamos un clasificador: Support Vector Classifier
    from sklearn.svm import SVC

    # Scaler estandar
    from sklearn.preprocessing import StandardScaler

    # Splitter para partir el dataset en entrenamiento/prueba
    from sklearn.model_selection import train_test_split


    from sklearn.decomposition import PCA
    from sklearn.ensemble import GradientBoostingClassifier

    from sklearn.impute import SimpleImputer
    from sklearn.preprocessing import OneHotEncoder

#3. Importar el conjunto de datos

    ruta1 = "D:\OneDrive - Tecnoquimicas\99. PERSONAL\Formación\Maestria\Semestre 1\Analisis Exploratorio Datos\Clase 5\CONSULTA_COMPRAS_234.xlsx"
    ruta2 = "D:\OneDrive - Tecnoquimicas\99. PERSONAL\Formación\Maestria\Semestre 1\Analisis Exploratorio Datos\Clase 5\CATEGORIA_COMPRAS.xlsx"

    #Cargar el dataset
    ds1 = pd.read_excel(ruta1)
    ds2 = pd.read_excel(ruta2)

    #Exploramos ambos datasets y conocemos su estructura

    #Dataset transaccional de compras
    ds1.info()
    ds1.head()
    ds1.shape

    #Dataset categorias de compras
    ds2.info()
    ds2.head()
    ds2.shape
#4. Se hace merge de ambos datasets

    #Elimino columnas que no son relevantes para el ejercicio o son redundantes
    ds1.drop(columns=['NUM_OC','DESCRIPCION','ESTADO','DIRECCION_ENVIO'], inplace=True)
    ds2.drop(columns=['UNIDAD_PRIMARIA','Tamaño de lote','CANTIDAD_PEDIDO_FIJO','CANT MINIMA','FECHA_ACT','FIJO','org/ins','COMPRADOR','COMPRADOR.1','LT COMP',
                      'VALIDACIÓN','Ultimo proveedor'],inplace=True)

    #Corroboro que haya quedada modificada la estructura del dataset
    ds1.info()
    ds2.info()
    
    #Se modifican los rotulos de las columnas para hacerlas coincidir
    header_ds1=['OC','CODIGO','PARTE','UDM','OQ','CANT_REC','CANT_ACEP','CANT_RECH','PRECIO','IMPORTE','MONEDA',
                'FECHA_CREACION_OC','FECHA_PROMESA_OC','AÑO_CREACION','AÑO_ENTREGA','PROVEEDOR','COMPRADOR','IMPORTADO','ORG_ENTREGA',
                'COMENTARIOS','CANCELADA']
    ds1.columns = header_ds1

    header_ds2 =['PARTE','CODIGO','DESCRIPCION','TIPO_INSUMO','UN','PLANEADOR','MOQ','ORG','t_PROC','t_POST',
                 't_TOTAL','CANT_MAX','MULTP_LOTE','LINEA','COSTO_STD','FECHA_CREACION_ART','OQ_CONFIG','LT']
    ds2.columns = header_ds2

    #Se verifica que hayan quedado los rótulos
    ds1.info()
    ds1.head()

    ds2.info()
    ds2.head()

    merged = pd.merge(ds1, ds2, on=['PARTE','CODIGO'])
    

#5. Analizo la estructura del nuevo dataset creado
    merged.shape
    merged.info()
    merged.describe()
    merged.dtypes

    #Separo las fechas en sus distintos componentes para hacer 

    merged['MES_CREACION'] = pd.to_datetime(merged['FECHA_CREACION_OC']).dt.month
    merged['DIA_CREACION'] = pd.to_datetime(merged['FECHA_CREACION_OC']).dt.day

    merged['MES_PROMESA'] = pd.to_datetime(merged['FECHA_PROMESA_OC']).dt.month
    merged['DIA_PROMESA'] = pd.to_datetime(merged['FECHA_PROMESA_OC']).dt.day

    merged.drop(columns=['FECHA_CREACION_OC','FECHA_PROMESA_OC'],inplace=True)
    merged.info

    #Reviso los datos nulos
    missing_data = merged.isnull()
    missing_data.head(5)

    for column in missing_data.columns.values.tolist():
        print(column)
        print (missing_data[column].value_counts())
        print("")
