from random import random

def main():
    print("Ingrese un valor para n: ", end="")
    n = int(input())

    print("Ingrese un valor para m: ", end="")
    m = int(input())

    MAT3 = []
    VEC2 = []
    VEC22 = []

    for i in range(n):
        MAT3.append([ 0] * m)


    llenadoAleatorio(MAT3)
    VEC2 = vectorUnion(MAT3)
    VEC22 = [0] * 3
    VEC22[0] = porcentajeDatosEntre(120, 170, MAT3)
    VEC22[1] = promedioMatriz(MAT3)
    VEC22[2] = promedioMinyMax(MAT3)
    print("Matriz: ")
    print(MAT3)
    print()
    print("Vector unión: ")
    print(VEC2)
    print()
    print("El porcentaje de datos entre 120 y 170 es", VEC22[0], "%.")
    print("El promedio de datos de toda la matriz es ", VEC22[1])
    print("El promedio entre el número máximo y el mínimo de la matriz es ", VEC22[2])


#Pasamos la matriz por referencia, por lo tanto no hay que retornarla
def llenadoAleatorio(MAT):
    for i in range(len(MAT)):
        for j in range(len(MAT[0])):
            MAT[i][j] = int(random() * 100 + 100) 

def vectorUnion(MAT):
    vectorUnion = []
    for i in MAT[0]:
        vectorUnion.append(i)
    for i in MAT[-1]:
        vectorUnion.append(i)
    return vectorUnion

def porcentajeDatosEntre(min, max, MAT):
    totalDatos = len(MAT) * len(MAT[0])
    contador = 0
    for i in MAT:
        for j in i:
            if j >= min and j <= max:
                contador += 1
    return round(contador * 100/totalDatos, 2)

def promedioMatriz(MAT):
    totalDatos = len(MAT) * len(MAT[0])
    suma = 0
    for i in MAT:
        for j in i:
            suma += j
    return round(suma/totalDatos, 2)

def promedioMinyMax(MAT):

    minValue = min(MAT[0])
    maxValue = max(MAT[0])

    for i in MAT:
        if min(i) < minValue:
            minValue = min(i)
        if max(i) > maxValue:
            maxValue = max(i)

    return  round((minValue + maxValue) / 2, 2)
main()