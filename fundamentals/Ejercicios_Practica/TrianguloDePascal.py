def siguienteLinea( n, arr=[1]):

    print(arr)
    if(len(arr) == n):
        return
    arr2 = [1]
    for i in range(0, len(arr)-1):
        arr2.append(arr[i]+arr[i+1])
    arr2.append(1)
    siguienteLinea(n,arr2) 

    
n = int(input("Ingrese la cantidad de iteraciones que desea imprimir: "))
siguienteLinea(n)
