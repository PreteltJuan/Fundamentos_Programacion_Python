from random import random as rd
import numpy as np
import pandas as pd

def main():
    datos = llenarInformacion()
    imprimirDatos(datos)
    consumoTotalOxigeno = obtenerConsumoTotalOxigeno(datos)
    imprimirConsumoOxigeno(consumoTotalOxigeno)
    obtenerCultivoMayorConsumoOxigeno(consumoTotalOxigeno)

def llenarInformacion():
    arr = np.zeros((4,10), dtype=int)
    for i in range(4):
        for j in range(10):
            if j == 0:
                arr[i][j] = rd() * 200 + 1800
            else:
                porcentaje = rd() * 10 + 90
                arr[i][j] = arr[i][j-1] - (400 * (porcentaje / 100))
    
    return arr

def imprimirDatos(datos):
    index = ["Semana 1", "Semana 2", "Semana 3" , "Semana 4", "Semana 5", "Semana 6", "Semana 7", "Semana 8", "Semana 9", "Semana 10"  ]
    columns = ["Cultivo 1", "Cultivo 2", "Cultivo 3", "Cultivo 4"]
    data = np.array(datos)
    data = pd.DataFrame(data, columns,  index, )
    pd.set_option('display.width', 120)
    print("                                	 	 Presiones en Pa")
    print(data)

def imprimirConsumoOxigeno(datos):
    index = ["Semana 1 y 2", "Semana 2 y 3", "Semana 3 y 4" , "Semana 4 y 5", "Semana 5 y 6", "Semana 6 y 7", "Semana 7 y 8", "Semana 8 y 9", "Semana 9 y 10" ]
    columns = ["Cultivo 1", "Cultivo 2", "Cultivo 3", "Cultivo 4"]
    data = np.array(datos)
    data = pd.DataFrame(data, columns,  index, )
    pd.set_option('display.width', 120)
    print("                                	 	 Consumo de Oxígeno")
    print(data)

def consumoOxigeno(presion1, presion2 ):
    cambioPresion = presion1 - presion2
    volumenRecipiente = 0.01
    molaridad02 = 12
    R = 0.082
    T = 298
    return (cambioPresion * volumenRecipiente * molaridad02) / (R * T)

def obtenerConsumoTotalOxigeno(datos):
    consumo = np.zeros((4,9), dtype=float)
    for i in range(len(datos)):
        for j in range(len(datos[i])-1):
            consumo[i][j] = consumoOxigeno(datos[i][j], datos[i][j+1])
    return consumo

def obtenerCultivoMayorConsumoOxigeno(datos):
    maximos = np.unravel_index(datos.argmax(), datos.shape)
    print("El cultivo que presentó el mayor consumo de oxígeno fue el número ", maximos[0] +1, ", durante las semanas ", maximos[1] + 1 ," y ", maximos[1] + 2, "." )
main()