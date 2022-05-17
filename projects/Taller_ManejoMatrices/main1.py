from random import random as aleatorio


def obtenerVectorUnion(MAT):
    resultado = []
    for i in MAT[0]:
        if i not in resultado:
            resultado.append(i)
    for j in MAT[-1]:
        if j not in resultado:
            resultado.append(j)
    return resultado

def porcentajeEntreElRango(MAT):
    totalElementos = len(MAT) * len(MAT[0])
    cantElementos = 0
    for i in MAT:
        for j in i:
            if j >= 120 and j <= 170:
                cantElementos = cantElementos + 1
    porcentaje = round(cantElementos * 100/totalElementos, 2)
    return porcentaje

def obtenerPromedioDatosMatriz(MAT):
    totalElementos = len(MAT) * len(MAT[0])
    suma = 0
    for i in MAT:
        for j in i:
            suma = suma + j
    promedio = round(suma/totalElementos, 2)
    return promedio

def obtenerPromedioMinMax(MAT):

    valorMinimo = min(MAT[0])
    valorMaximo = max(MAT[0])

    for i in MAT:
        if min(i) < valorMinimo:
            valorMinimo = min(i)
        if max(i) > valorMaximo:
            valorMaximo = max(i)
    promedio = round((valorMinimo + valorMaximo) / 2, 2)
    return  promedio

print("Tamaño para la matriz ")
print("Ingrese n(filas): ")
n = int(input())

print("Ingrese m(columnas): ")
m = int(input())

MAT3 = []


for i in range(n):
    MAT3.append([ 0] * m)

for i in range(len(MAT3)):
    for j in range(len(MAT3[0])):
        MAT3[i][j] = int(aleatorio() * 100 + 100)
         
VEC2 = obtenerVectorUnion(MAT3)
VEC22 = [0,0,0]
VEC22[0] = porcentajeEntreElRango(MAT3)
VEC22[1] = obtenerPromedioDatosMatriz(MAT3)
VEC22[2] = obtenerPromedioMinMax(MAT3)
print("Matriz final con datos aleatorios: ")
print(MAT3)

print("Vector unión resultante: ")
print(VEC2)
print()
print()
print("El porcentaje de datos que se encuentran entre 120 y 170 es", VEC22[0])
print("El promedio de toda la matriz es ", VEC22[1])
print("El promedio entre el número máximo y el mínimo de la matriz es ", VEC22[2])