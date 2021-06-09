import matplotlib.pylab as plt
import numpy as np

# Grafico de Perdidas
def graficoPerdidas(history):
    plt.figure(1)
    plt.plot(history.history['loss'])
    plt.title('Perdidas del Modelo')
    plt.ylabel('Perdidas')
    plt.xlabel('Epocas')
    plt.legend(['Entrenamiento'], loc='upper left')

    return plt.show()


def graficoConsolidado(escalado, datos, plot_prediccion_entrenamiento, plot_prediccion_test):
    # Mostrar predicciones y datos
    plt.figure(2)
    plt.figure(figsize=(18, 13))
    plt.plot(escalado.inverse_transform(datos), "r.-", color="black", label="Datos")
    plt.plot(plot_prediccion_entrenamiento, "r.-", color="blue", label="Prediccion Entrenamiento")
    plt.plot(plot_prediccion_test, "r.-", color="red", label="Prediccion Test")
    plt.yticks(np.arange(0, 100000, 5000))
    plt.xticks(np.arange(0, len(datos) + 1, 5))
    plt.legend()
    plt.savefig('C:/Users/pablo/Dropbox/DeepLearning/Img/plotbitcoins.png')