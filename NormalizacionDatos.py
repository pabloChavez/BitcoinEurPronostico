from sklearn.preprocessing import MinMaxScaler
import pandas as np

# Normalizacion de Datos
def normalizacionDatos(dataframe, porcenTrainning):
    datos = dataframe.values
    datos = datos.astype('float32')

    #Normalizacion de Datos
    escalado = MinMaxScaler(feature_range=(0, 1))
    datos = escalado.fit_transform(datos)

    #Division en Train/Test
    tsize = int(len(datos) * porcenTrainning)
    testsize = len(datos) - tsize
    entrenamiento, test = datos[0:tsize,:], datos[tsize:len(datos),:]
    return entrenamiento, test, escalado, datos
