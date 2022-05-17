from random import random as rd
import numpy as np
import pandas as pd


def main():

    cantTrabajadores = int(rd() * 11) + 5
    datos = crearInformacion(cantTrabajadores)

    promedios = getPromedios(datos)
    lesiones = lesionMasComunPorLabor(datos)

    mostrarInformacion(datos)
    mostrarPromedios(promedios)
    mostrarLesiones(lesiones)

    mostrarInformacionEmpresa(datos, "A")


def mostrarInformacionEmpresa(datos, empresa):
    print("\n")
    columns = ["Nombre", "Edad", "Empresa", "Labor", "Frecuencia cardiaca", "Frecuencia respiratoria",
               "Dominancia", "Lesiones en hombros", "Lesiones en espalda", "Lesiones en cuello"]
    dataFrame = pd.DataFrame(datos, columns=columns)

    dataFrame = dataFrame[dataFrame.Empresa == empresa]

    if dataFrame.empty:
        print("No se encontraron trabajadores para la empresa ", empresa)
    else:
        print("Trabajador(es) de la empresa ", empresa)
        print(dataFrame.sort_values("Edad", ascending=True))


def mostrarInformacion(datos):
    print("\n")
    columns = ["Nombre", "Edad", "Empresa", "Labor", "Frecuencia cardiaca", "Frecuencia respiratoria",
               "Dominancia", "Lesiones en hombros", "Lesiones en espalda", "Lesiones en cuello"]

    dataFrame = pd.DataFrame(datos, columns=columns)
    print(dataFrame)


def getPromedios(datos):
    edades = [fila[1] for fila in datos]
    frecuenciasCardiacas = [fila[4] for fila in datos]
    frecuenciaRespiratoria = [fila[5] for fila in datos]

    return [np.mean(edades), np.mean(frecuenciasCardiacas), np.mean(frecuenciaRespiratoria)]


def mostrarPromedios(promedios):
    print("\n")
    print("Promedio de edades ", round(promedios[0], 2))
    print("Promedio de frecuencias cardiacas", round(promedios[1], 2))
    print("Promedio de frecuencias respiratorias", round(promedios[2], 2))
    print("\n")


def lesionMasComunPorLabor(datos):
    labores = []
    for i in range(3):
        labores.append([0] * 3)

    for i in datos:
        datoL = [0, 0, 0]
        if i[7] == "Sí":
            datoL[0] += 1
        if i[8] == "Sí":
            datoL[1] += 1
        if i[9] == "Sí":
            datoL[2] += 1

        if i[3] == "plomero":
            labores[0][0] += datoL[0]
            labores[0][1] += datoL[1]
            labores[0][2] += datoL[2]
        elif i[3] == "obrero":
            labores[1][0] += datoL[0]
            labores[1][1] += datoL[1]
            labores[1][2] += datoL[2]
        elif i[3] == "carpintero":
            labores[2][0] += datoL[0]
            labores[2][1] += datoL[1]
            labores[2][2] += datoL[2]

    lesiones = [None, None, None]

    for i in range(len(lesiones)):
        if np.max(labores[i]) != 0:
            lesiones[i] = np.where(labores[i] == np.max(labores[i]))
    return lesiones


def mostrarLesiones(lesiones):
    print("\n")
    labores = ["plomero", "obrero", "carpintero"]
    for i in range(len(labores)):
        if lesiones[i]:
            if len(lesiones[i][0]) == 1:
                print("La lesión más común para el oficio de ",
                      labores[i], " es ", end="")
                if lesiones[i][0][0] == 0:
                    print(" lesión de hombros.")
                elif lesiones[i][0][0] == 1:
                    print(" lesión de espalda.")
                else:
                    print(" lesión de cuello.")
            else:
                print("Las lesiones más comunes en el oficio de ",
                      labores[i], " son : ")
                for j in lesiones[i][0]:
                    if j == 0:
                        print("- lesión de hombros.")
                    elif j == 1:
                        print("- lesión de espalda.")
                    else:
                        print("- lesión de cuello.")
        else:
            print("No se presentaron lesiones para el oficio de ", labores[i])

    # if lesiones[0][0]
    # print(lesiones[0][0])

# Se crea la información de cada trabajador


def crearInformacion(cantTrabajadores):
    datos = [None] * cantTrabajadores

    for i in range(len(datos)):
        datosTrabajador = []
        datosTrabajador.append("Trabajador " + str(i+1))
        datosTrabajador.append(getEdad())
        empresa = getEmpresa()
        datosTrabajador.append(empresa)
        datosTrabajador.append(getLabor(empresa))
        datosTrabajador.append(getFrecuenciaCardiaca())
        datosTrabajador.append(getFrecuenciaRespiratoria())
        datosTrabajador.append(getDominancia())
        datosTrabajador.append(getLesionHombro())
        datosTrabajador.append(getLesionEspalda())
        datosTrabajador.append(getLesionCuello())
        datos[i] = datosTrabajador
    return datos


def getEdad():
    return int(rd() * 46) + 25


def getEmpresa():
    empresas = ["A", "B", "C"]
    return empresas[int(rd() * len(empresas))]


def getLabor(empresa):
    labores = ["obrero", "carpintero", "plomero"]
    if empresa == "A":
        return labores[int(rd() * 2)]
    elif empresa == "B":
        return labores[int(rd() * len(labores))]
    return labores[int(rd() * 2) + 1]


def getFrecuenciaCardiaca():
    return int(rd() * 101) + 50


def getFrecuenciaRespiratoria():
    return int(rd() * 16) + 10


def getDominancia():
    dominancias = ["Diestro", "Zurdo", "Ambidiestro"]
    return dominancias[int(rd() * len(dominancias))]


def getLesionHombro():
    opciones = ["Sí", "No"]
    return opciones[int(rd() * 2)]


def getLesionEspalda():
    opciones = ["Sí", "No"]
    return opciones[int(rd() * 2)]


def getLesionCuello():
    opciones = ["Sí", "No"]
    return opciones[int(rd() * 2)]


main()
