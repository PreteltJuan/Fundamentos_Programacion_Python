numerosT = []
print("Ingresar F para terminar de llenar el arreglo")

while (True):
    a = input("Ingrese un valor: ")
    if(a == 'f' or a == 'F'):
        break
    elif( not a.isnumeric()):
        print("El valor ingresado no es un número")
        continue   
    numerosT.append(int(a))



def suma(numeros):

    if(len(numeros) == 1):
        return numeros[0]
        
    return suma(numeros[0:-1]) + numeros[-1]


print( suma(numerosT) )