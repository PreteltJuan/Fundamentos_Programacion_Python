import numpy as np
import pandas as pd


def main():
    sector = []
    taxis = []
    filas, columnas, totalTaxis, sector = inicializarDatos()

    crearTaxisAleatorios(sector, taxis, filas, columnas, totalTaxis)
    # imprimirSector(sector)

    celda = celdaAleatoriaEnBlanco(sector)

    # Mostrar El número de taxis que se encuentran a cinco cuadras o menos a la redonda sobre una celda en blanco seleccionada a azar
    print("\n")
    print("Hay ", taxisA5Cuadras(celda, sector),
          " taxis a 5 cuadras a la redonda de la cuadra ", celda)
    print("\n")
    # Mostrar la placa y el modelo del taxi que se encuentra a menor distancia en cuanto a número de cuadras por recorrer para llegar a i, j. En caso que varios taxis se encuentren a la misma distancia, mostrar el listado de las placas  de los taxis ordenadas por fecha del modelo. Mostrar también la fecha y la marca

    placasTaxisCercanos = taxisCercanos(celda, sector)
    imprimirTaxisCercanos(celda, placasTaxisCercanos, taxis)

    taxisCercanosModelosRecientes(taxis)

    taxisEnXCuadras = taxisEnXCuadra(celda, sector, 5)
    imprimirTaxisEnXCuadra(celda, taxisEnXCuadras, taxis, 5)
    # print("Taxis totales: ", cantTaxis)


# Crear valores aleatorios para las filas y columnas e inicializa la matrices con valor 0
def inicializarDatos():
    filas = int(np.random.rand() * 11) + 20
    columnas = int(np.random.rand() * 6) + 10
    canTaxis = int(filas * columnas * 0.3)

    # sector = np.zeros((filas, columnas), dtype=object)
    sector = []
    for i in range(filas):
        sector.append([0] * columnas)
    return [filas, columnas, canTaxis, sector]


def imprimirSector(sector):
    dataFrame = pd.DataFrame(sector)
    print(dataFrame)


def imprimirTaxis(taxis):
    columns = ["Nombre", "Edad", "Empresa", "Labor", "Frecuencia cardiaca", "Frecuencia respiratoria",
               "Dominancia", "Lesiones en hombros", "Lesiones en espalda", "Lesiones en cuello"]
    dataFrame = pd.DataFrame(taxis)
    print(dataFrame)


# Crea taxis en posiciones aleatorias con datos aleatorios
def crearTaxisAleatorios(sector, taxis, filas, columnas, cantTaxis):
    for i in range(cantTaxis):
        while True:
            fila = np.random.randint(filas)
            columna = np.random.randint(columnas)

            if not sector[fila][columna]:
                placa = crearPlacaAleatoria()
                taxis.append([placa, crearMarcaAleatoria(
                ), crearFechaModeloAleatorio(), crearCedulaAleatoria()])
                sector[fila][columna] = placa
                break


# #Retorna la posición de una celda en blanco aleatoria
def celdaAleatoriaEnBlanco(sector):
    fila = columna = -1
    while True:
        fila = np.random.randint(len(sector))
        columna = np.random.randint(len(sector[0]))
        if not sector[fila][columna]:
            break
    return fila, columna

# #Encuentra los taxis en un radio dado de cuadras


def taxisA5Cuadras(celda, sector):
    cantTaxis = 0
    taxis = taxisALaRedonda(celda, sector, 5)
    for i in taxis:
        for j in i:
            if j != "0":
                cantTaxis += 1
    return cantTaxis

# Encuentra los taxis más cercanos a la cuadra enviada


def taxisCercanos(celda, sector):

    placas = []
    cuadras = 0
    taxiEncontrado = False
    while cuadras < len(sector) and not taxiEncontrado:
        arr = taxisEnXCuadra(celda, sector, cuadras)
        for i in arr:
            for j in i:
                if len(j) != 0:
                    for k in j:
                        if k != "0":
                            placas.append(k)
                            taxiEncontrado = True
        cuadras += 1
    placas.append(cuadras)
    return placas

# Imprime los taxis enviados ordenados por la fecha de modelo.


def imprimirTaxisCercanos(celda, placas, taxis):

    if len(placas) == 1:
        print("No hay taxis cercanos a la cuadra  ", celda,  ".")
    elif len(placas) == 3:
        print("El taxi más cercano de la cuadra ",
              celda, " está a ", placas[-1], " cuadra(s):")
    else:
        print("Los taxis más cercanos a la cuadra ", celda, " son:")
    columns = ["Placa", "Marca", "Fecha del modelo", "Cédula conductor"]
    dataTaxi = pd.DataFrame(taxis, columns=columns)
    taxisFiltro = dataTaxi[dataTaxi.Placa.isin(placas)]
    if not taxisFiltro.empty:
        print(taxisFiltro)

# Encuentra los taxis que se encuentras a x cuadras


def taxisALaRedonda(celda, sector, c):
    taxis = []
    initX = celda[0] - c if celda[0] - c >= 0 else 0
    initY = celda[1] - c if celda[1] - c >= 0 else 0
    taxis = np.array(sector)
    return taxis[initX:celda[0]+c+1, initY:celda[1]+c+1]


def taxisEnXCuadra(celda, sector, c):
    taxis = []
    initX = celda[0] - c if celda[0] - c >= 0 else 0
    initY = celda[1] - c if celda[1] - c >= 0 else 0
    finX = celda[0] + c
    finY = celda[1] + c

    sectorNP = np.array(sector)
    taxis.append(sectorNP[initX:initX+1, initY:finY+1])
    taxis.append(sectorNP[finX:finX+1, initY:finY+1])
    taxis.append(sectorNP[initX:finX+1, initY:initY+1])
    taxis.append(sectorNP[initX:finX+1, finY:finY+1])

    return taxis

# Imprime los taxis encontrados por taxisEnXCuadra.


def imprimirTaxisEnXCuadra(celda, taxiEnXCuadra, taxis, c):

    placas = []
    for i in taxiEnXCuadra:
        for j in i:
            if len(j) != 0:
                for k in j:
                    if k != "0":
                        placas.append(k)

    print("\n")
    if len(placas) == 0:
        print("No se encontrarron taxis a ", c,
              " cuadras de la cuadra ", celda)
    elif len(placas) == 1:
        print("Se encontró un taxi a ", c,
              " cuadras de la cuadra ", celda, ": ")
    else:
        print("Se encontraron estos taxis a ", c,
              " cuadras de la cuadra ", celda, ": ")
    columns = ["Placa", "Marca", "Fecha del modelo", "Cédula conductor"]
    dataTaxi = pd.DataFrame(taxis, columns=columns)
    taxisFiltro = dataTaxi[dataTaxi.Placa.isin(placas)]
    if not taxisFiltro.empty:
        print(taxisFiltro)


# Encuentra el o los taxis con el modelo más reciente
def taxisCercanosModelosRecientes(taxis):
    print("\n")

    columns = ["Placa", "Marca", "Fecha del modelo", "Cédula conductor"]
    dataTaxi = pd.DataFrame(taxis, columns=columns)
    taxisFiltro = dataTaxi.sort_values('Fecha del modelo', ascending=False)

    modelosMasRecientes = []
    for i in taxisFiltro.values:
        if i[2] == taxisFiltro.iloc[0, 2]:
            modelosMasRecientes.append(i)
        else:
            break
    if len(modelosMasRecientes) == 1:
        print("EL modelo más reciente es ")
    else:
        print("Los modelos más recientes son: ")
    print(pd.DataFrame(modelosMasRecientes, columns=columns))

# #Crea una placa de forma aleatoria.


def crearPlacaAleatoria():
    placa = ""
    letras = np.random.randint(65, 90, 3)
    numeros = np.random.randint(48, 58, 3)

    for i in range(len(letras)):
        placa += chr(letras[i])
    for i in range(len(numeros)):
        placa += chr(numeros[i])
    return placa

# #Retorna una marca aleatoria.


def crearMarcaAleatoria():
    marcas = ["Toyota", "Cadillac", "Renault", "Dodge",
              "Chevrolet", "Mazda", "Ford", "Volkswagen"]
    return np.random.choice(marcas)

# #Retorna una fecha aleatoria entre 1950 y 2015.


def crearFechaModeloAleatorio():
    return np.random.randint(1950, 2016)

# Retorna una cédula aleatoria


def crearCedulaAleatoria():
    return np.random.randint(1000000000, 1003000000)


main()
