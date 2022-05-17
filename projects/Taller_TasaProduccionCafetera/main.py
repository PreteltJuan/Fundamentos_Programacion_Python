from random import random as rd
import numpy as np
import pandas as pd

def main():
    datos = llenarInformacion()
    calcularTVMvalor(datos)
    calcularTVMvolumen(datos)
    calcularPromedios(datos)
    imprimirDatos(datos)
    imprimirMayoresTVM(datos)
    imprimirConTVM_Ascendente(datos)

def llenarInformacion( ):
    arr = np.zeros((12,8), dtype=float)
    for i in range(len(arr)-1):
        for j in range(len(arr[0])-4):
            if j % 2 == 0:
                arr[i][j] = round(rd() * 10 + 0.5, 1)
            else:
                arr[i][j] = round(rd() * 7 + 0.5, 1)
    return arr

def imprimirDatos(datos):
    print("\n")
    columns = ['2012',  "2013",  "TVM 2012",  "TVM 2013" ]
    index = ["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6", "Mes 7", "Mes 8", "Mes 9", "Mes 10", "Mes 11", "Promedio"]
    mux = pd.MultiIndex.from_product([columns, ['Volumen','Valor']])
    data = np.array(datos)
    data = pd.DataFrame(data,index, mux  )
    data.index.name = "Meses"
    data = np.round(data, decimals = 2 )
    #pd.set_option('display.width', 120)
    print("        Volumen y valor de la cosecha cafetera")
    print()
    print(data)

def calcularTVMvalor(datos):
    for i in range(1, len(datos) - 1):
        datos[i][5] = calcularTVM( datos[i][1], datos[i-1][1])
        datos[i][7] = calcularTVM( datos[i][3], datos[i-1][3])
    
def calcularTVMvolumen(datos):
    for i in range(1, len(datos) - 1):
        datos[i][4] = calcularTVM( datos[i][0], datos[i-1][0])
        datos[i][6] = calcularTVM( datos[i][2], datos[i-1][2])

def calcularTVM(valor1, valor2):
    return  (valor1 / valor2 - 1) * 100

def calcularPromedios(datos):
    promedios = np.mean(datos, 0)
    datos[-1] = promedios
    for i in range(4):
        datos[len(datos)-1][len(datos[0])-(i+1)] = 0
    # datos[len(datos)-1][len(datos[0])-2] = 0
    # datos[len(datos)-1][len(datos[0])-3] = 0
    # datos[len(datos)-1][len(datos[0])-4] = 0

def imprimirMayoresTVM(datos):
    print("\n")
    amax = datos.max(axis=0)
    amin = datos.min(axis=0)
    maximos = np.where(-amin > amax, amin, amax)

    maximosImportante = [None, None]
    if maximos[4] > maximos[6]:
        maximosImportante[0] = np.where(datos == maximos[4])
    else:
        maximosImportante[0] = np.where(datos == maximos[6])
    
    if maximos[5] > maximos[7]:
        maximosImportante[1] = np.where(datos == maximos[5])
    else:
        maximosImportante[1] = np.where(datos == maximos[7])

    print("La mayor variación en la tasa de producción fue en el mes ", maximosImportante[0][0][0] + 1, " del año ", end="")
    print( "2012" if maximosImportante[0][1][0] == 4 else "2013")
    print("La mayor variación en el valor fue en el mes ", maximosImportante[1][0][0] + 1, " del año ", end="")
    print( "2012" if maximosImportante[1][1][0] == 4 else "2013")

def imprimirConTVM_Ascendente(datos):
    print("\n")
    arr1 = np.zeros((11,2), dtype=float)
    a = datos[0:-1,0]
    b = datos[0:-1,4]
    ab = np.stack([a, b], axis=1)

    arr2 = np.zeros((11,2), dtype=float)
    c = datos[0:-1,2]
    d = datos[0:-1,6]
    cd = np.stack([c, d], axis=1)


    columns1 = ['2012', "TVM" ]
    columns2 = ['2013', "TVM" ]


    index = ["Mes 1", "Mes 2", "Mes 3", "Mes 4", "Mes 5", "Mes 6", "Mes 7", "Mes 8", "Mes 9", "Mes 10", "Mes 11"]

    mux1 = pd.MultiIndex.from_product([columns1, ['Volumen']])
    mux2 = pd.MultiIndex.from_product([columns2, ['Volumen']])

    data1 = np.array(ab)
    data2 = np.array(cd)

    data1 = pd.DataFrame(data1,index, columns=mux1 )
    data2 = pd.DataFrame(data2,index, columns=mux2 )

    data1.index.name = "Meses"
    data2.index.name = "Meses"

    data1 = np.round(data1, decimals = 2 )
    data2 = np.round(data2, decimals = 2 )


    data1.sort_values( ('TVM',"Volumen"), inplace=True, ascending=True, key=abs )
    data2.sort_values( ('TVM',"Volumen"), inplace=True, ascending=True, key=abs )

    print("\nDatos del año 2012 - Orden: TVM  de producción ascendente")
    print(data1)
    print("\n")

    print("\nDatos del año 2013 - Orden: TVM de producción ascendente")
    print(data2)
    print("\n")

main()