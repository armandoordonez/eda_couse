# Import
import pandas as pd
import numpy as np
# Pipeline
from sklearn.pipeline import Pipeline

# Scaler estandar preprocesado
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import QuantileTransformer
from sklearn.tree import DecisionTreeClassifier

# Splitter
from sklearn.model_selection import train_test_split

# Importamos un clasificador: Support Vector Classifier para ML
from sklearn.svm import SVC

# Genera un problema de clasificación randmom de n-classes.

from sklearn.datasets import make_classification

ruta = "D:\OneDrive - Tecnoquimicas\99. PERSONAL\Formación\Maestria\Semestre 1\Analisis Exploratorio Datos\Clase 5\Dataset_ejercicio_3_churn.csv"
ds = pd.read_csv(ruta)

ds.info()
ds.head()
ds = ds.replace({"area_code_408": '?'})
ds = np.NaN()
ds.info()
ds.head()
ds['churn'].info
ds['churn'].unique()
ds['area_code'].unique()
ds['area_code'].describe()

X = ds[["number_customer_service_calls", "total_day_calls", "total_intl_charge"]]
Y = ds["churn"]

# Dividir el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# Crea el pipeline
# El pipeline puede usarse como un estimador
# y evita data leaking del test set en el train set

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('quantile', QuantileTransformer()),
    ('decision_tree', DecisionTreeClassifier()),
    ])


# Se aplican los pasos en el dataset de entrenamiento
pipe.fit(X_train, y_train)

# se aplican los pasos en el dataset de prueba
pipe.score(X_test, y_test)