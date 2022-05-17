from random import random


def main():
    sector = []
    taxis = []

    filas = int(random() * 10 + 20)
    columnas = int(random() * 5 + 10)
    cantTaxis = int(filas * columnas * 0.3)

    inicializarSectorYTaxis(sector, taxis, filas, columnas)
    crearTaxis(sector, taxis, filas, columnas, cantTaxis)

    x,y = celdaAlAzar(filas, columnas, sector)
    
    #Punto 1:
    print("Cantidad de taxis en 5 cuadras a la redonda  de la celda ", x, ", ",  y, ": ", cantTaxisCercanos(x, y, sector, 5))

    x,y = celdaAlAzar(filas, columnas, sector)
    #Punto 2:
    arr = taxisCercanos(x,y, sector)
    imprimirTaxisPorFecha(x, y, arr, taxis)

    x,y = celdaAlAzar(filas, columnas, sector)
    #Punto 3:
    arr = taxisCercanosModelosRecientes(x, y, sector, taxis)
    imprimirTaxisPorPlaca(x, y, arr)

    x,y = celdaAlAzar(filas, columnas, sector)
    #Punto 4:
    arr = taxisEnXCuadra(x, y, sector, 3)
    imprimirTaxisEnXCuadra(x, y, arr, taxis, 3)
    print("Taxis totales: ", cantTaxis)
    return 0

#Retorna la posición de una celda en blanco aleatoria
def celdaAlAzar(filas, columnas, sector):
    x = int(random() * filas)
    y = int(random() * columnas)
    while sector[x][y] != None:
        x = int(random() * filas)
        y = int(random() * columnas)
    return x, y

#Encuentra los taxis en un radio dado de cuadras
def cantTaxisCercanos(x, y, sector, radio):
    cant = 0
    for i in range(x-radio, x+radio+1):
        for j in range(y-radio, y+radio+1):
            if (i >= 0 and j >= 0) and (i < len(sector) and j < len(sector[0])):
                if sector[i][j] != None:
                    cant += 1
    return cant

#Encuentra los taxis más cercanos a la cuadra x, y.
def taxisCercanos(x, y, sector):
    arr = []
    i = 1
    B = True
    while i < len(sector) and B:
        for j in range(x-i, x+i +1):
            for k in range(y-i, y+i +1):
                if (j >= 0 and k >= 0) and (j < len(sector) and k < len(sector[0])):
                    if sector[j][k] != None:
                        arr += (j,k)
                        B =  False
        i += 1
    arr.append(i-1)
    return arr

#Imprime los taxis enviados ordenados por la fecha de modelo.
def imprimirTaxisPorFecha(x,y,arr, taxis):
    print()
    if len(arr) == 1: 
        print("No hay taxis cercanos al punto ", x, ", " , y,"." )
        return None
    elif len(arr) == 3:
        print("El taxi más cercano del punto",  x, ", " , y," está a ", arr[-1], " cuadra.")
    else:
        print("Los taxis más cercanos del punto",  x, ", " , y," están a ", arr[-1], " cuadras.")
    datos = []
    for i in range(0,len(arr)-1,2):
        datos.append(taxis[arr[i]][arr[i+1]])
    datos.sort(key=lambda datos : datos[2])
    for i in range(len(datos)):
        print(i+1,": ",  datos[i][0], " - ", datos[i][2], " - ",  datos[i][1] )
    print()

#Encuentra los taxis que se encuentras a d cuadras
def taxisEnXCuadra(x, y, sector, d ):
    arr = []
    for j in range(x-d, x+d+1):
        for k in range(y-d, y+d +1):
            if (j >= 0 and k >= 0) and (j < len(sector) and k < len(sector[0])):
                if (j == x-d or j == x+d) or (k == y-d or k == y+d ):
                    if sector[j][k] != None:
                        arr += (j,k)
    return arr
    
#Imprime los taxis encontrados por taxisEnXCuadra.
def imprimirTaxisEnXCuadra(x, y, arr, taxis, d):
    print()
    if len(arr) == 0:
        print("No se encontrarron taxis a " , d, " cuadras del punto",  x, ", " , y)
        return None
    elif len(arr) == 2:
        print("Se encontró un taxi a ", d, " cuadras del punto",  x, " " , y)
    else:
        print("Se encontraron estos taxis a ", d, " cuadras del punto",  x, " " , y)

    datos = []
    for i in range(0,len(arr),2):
        datos.append(taxis[arr[i]][arr[i+1]])
    for i in range(len(datos)):
        print(i+1,": ",  datos[i][0], " - ", datos[i][1], " - ",  datos[i][2], " - ",  datos[i][3] )
    print()

#Encuentra el o los taxis con el modelo más reciente
def taxisCercanosModelosRecientes(x, y, sector, taxis):
    arr = []
    delta = 0
    j = 1
    while j < len(sector):

        temp = taxisEnXCuadra(x,y,sector,j)
        j += 1
        if len(temp) == 0: continue
        
        datos = []
        for i in range(0,len(temp),2):
            datos.append(taxis[temp[i]] [temp[i+1]])
        datos.sort(key=lambda datos: datos[2], reverse=True)
        
        if len(arr) == 0: 
            arr.append( datos[0])
            delta = j-1

        for i in datos:
            if i[2] > arr[0][2]: 
                arr =  []
                arr.append(i)
                delta = j
            elif i[3] != arr[0][3] and i[2] == arr[0][2] and j == delta:
                arr.append(i)
            elif i[2] < arr[0][2]: 
                break
    arr.append(delta)
    return arr

#Imprime los datos de los taxis enviados teniendo en cuenta el orden de sus placas
def imprimirTaxisPorPlaca(x, y,arr):
    print()
    if len(arr) == 1: 
        print("No hay taxis cercanos al punto del punto",  x, ", " , y)
        return None
    elif len(arr) == 2:
        print("El taxi de modelo más reciente está a ", arr[-1], " cuadras del punto",  x, ", " , y)
    else:
        print("Los taxis de modelo más reciente están a ", arr[-1], " cuadras del punto",  x, ", " , y)
    for i in range(0, len(arr)-1):
        print(i+1,": ",  arr[i][0], " - ", arr[i][1], " - ",  arr[i][2], " - ",  arr[i][3] )
    print()

def getModelo(x, y, taxis):
    return taxis[x][y][2]
#Crea una placa de forma aleatoria.
def crearPlaca():
    str = ""
    for i in range(3):
        str += chr(int(random() * 25 + 65))
    for i in range(3):
        str += chr(int(random() * 10 + 48))
    return str

#Retorna una marca aleatoria.
def crearMarca():
    marcas = ["Renault", "Chevrolet", "Mazda",
              "Nissan", "Kia", "Toyota", "Volkswagen"]
    return marcas[int(random() * len(marcas))]

#Retorna una fecha aleatoria entre 2000 y 2020.
def crearFechaModelo():
    return int(random() * 21 + 2000)

#Retorna una cédula entre 1,000,000,000 y 1,010,000,000.
def crearCedula():
    return int(random() * 10000000 + 1000000000)

#Inicializa la matrices con la cantidad de filas y columnas dadas
def inicializarSectorYTaxis(sector, taxis, filas, columnas):
    for i in range(filas):
        sector.append([None] * columnas)
        taxis.append([None] * columnas)

#Crea taxis en posiciones aleatorias con datos aleatorios 
def crearTaxis(sector, taxis, filas, columnas, cantTaxis):
    for i in range(cantTaxis):
        B = True
        while B:
            x = int(random() * filas)
            y = int(random() * columnas)

            if sector[x][y] == None:
                sector[x][y] = crearPlaca()
                taxis[x][y] = [(sector[x][y]), crearMarca(),
                               crearFechaModelo(), crearCedula()]
                B = False

main()