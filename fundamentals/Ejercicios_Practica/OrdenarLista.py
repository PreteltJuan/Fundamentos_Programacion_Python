def ordenarListas(lista, cant): 

    if cant > 1: 
        for x in range(0, cant-1): 
            if lista[x] > lista[x+1]:
                Variable_Auxiliar = lista[x]
                lista[x] = lista[x+1]                 
                lista[x+1] = Variable_Auxiliar         
        ordenarListas(lista, cant-1)  


datos = []

#LLenar arreglo
print("Ingresar F para terminar de llenar el arreglo")
while (True):
    a = input("Ingrese un valor: ")
    if(a == 'f' or a == 'F'):
        break
    elif( not a.isnumeric()):
        print("El valor ingresado no es un número")
        continue   
    datos.append(int(a))


print("Lista inicial: ", datos) 
ordenarListas(datos, len(datos)) 
print("Lista ordenada: ", datos)
