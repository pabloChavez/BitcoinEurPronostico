import numpy as np
import math
from sklearn.metrics import mean_squared_error
from BitcoinPredict.WebScrapingBtc import informacionBtcOnline
from ConnectMysql import coneccionDb, insertDatosFinales
from DeliveryEmail import deliveryEmail
from NormalizacionDatos import normalizacionDatos
from Practica.RNNLstmBtc import RedesNeuronalesLstm
from PlotLibrary import graficoPerdidas, graficoConsolidado

epochs =1
mirar_atras = 10
porcenTrainning = 0.67
LSTMValue = 1
Hidden= 40

# Cargamos datos de BTC online a la BD
informacionBtcOnline()

# Coneccion Base de datos.
dataframe = coneccionDb()

# Normalizacion de datos.
entrenamiento, test, escalado, datos = normalizacionDatos(dataframe, porcenTrainning)

# Conversion Array-Matriz
def create_base_datos(datos, mirar_atras=1):
	datosX, datosY = [], []
	for i in range(len(datos)-mirar_atras-1):
		a = datos[i:(i+mirar_atras), 0]
		datosX.append(a)
		datosY.append(datos[i+mirar_atras, 0])
	return np.array(datosX), np.array(datosY)

# Datos Listos para Modelo.
tX, tY = create_base_datos(entrenamiento, mirar_atras)
testX, testY = create_base_datos(test, mirar_atras)
tX = np.reshape(tX, (tX.shape[0], 1, tX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))

# Definicion del modelo.
model = RedesNeuronalesLstm(LSTMValue, mirar_atras, Hidden)

# Compilar modelo y ajustarlo.
model.compile(loss='mean_squared_error', optimizer='adam')
history=model.fit(tX, tY, epochs=epochs, batch_size=1, verbose=1)

graficoPerdidas(history)

# Prediccion 1 dias
proximodia = tX[:1]
proximodia = model.predict(proximodia)
proximodia = escalado.inverse_transform(proximodia)
pronostico = np.array(proximodia)

# Realizacion de predicciones
prediciones_entrenamiento = model.predict(tX)
prediciones_test = model.predict(testX)

# Inversion de las predicciones para calcular su error
prediciones_entrenamiento = escalado.inverse_transform(prediciones_entrenamiento)
tY = escalado.inverse_transform([tY])
prediciones_test = escalado.inverse_transform(prediciones_test)
testY = escalado.inverse_transform([testY])

# Calculo de la raiz del error cuadratico medio o RMSE
Puntuacion_Train = math.sqrt(mean_squared_error(tY[0,:], prediciones_entrenamiento[:,0]))
Puntuacion_Test = math.sqrt(mean_squared_error(testY[0], prediciones_test[:,0]))
print('Puntuacion Train: %.2f RMSE  y Puntuacion Test: %.2f RMSE'
      % (Puntuacion_Train,Puntuacion_Test))

# Desplazamiento de predicciones de entrenamiento
plot_prediccion_entrenamiento = np.empty_like(datos)
plot_prediccion_entrenamiento[:, :] = np.nan
plot_prediccion_entrenamiento[mirar_atras:len(prediciones_entrenamiento)+mirar_atras, :] = prediciones_entrenamiento

# Desplazamiento de predicciones de test
plot_prediccion_test = np.empty_like(datos)
plot_prediccion_test[:, :] = np.nan
plot_prediccion_test[len(prediciones_entrenamiento)+(mirar_atras*2)+1:len(datos)-1, :] = prediciones_test

# Concatenamos Prediccion Test Con Prediccion de 1 dias
plot_prediccion_test = np.concatenate((plot_prediccion_test, pronostico))

graficoConsolidado(escalado, datos, plot_prediccion_entrenamiento, plot_prediccion_test)

datosUlt = escalado.inverse_transform(datos)
datosUlt = int(datosUlt[-1])
puntuaciontrain = int(Puntuacion_Train)
puntuaciontest = int(Puntuacion_Test)
pronostico = int(pronostico)

insertDatosFinales(puntuaciontrain, puntuaciontest, pronostico)

deliveryEmail(puntuaciontrain, puntuaciontest, pronostico, datosUlt)
