

def invertirNumero(numero, indice = 0):
    if(indice == len(numero) - 1):
        return (numero[indice])
    else:
        return (invertirNumero(numero, indice + 1) +  numero[indice])


numero = input("Ingrese el número que desesa invertir: ")
numeroInvertido = invertirNumero(numero)

print("El número invertido es: ", numeroInvertido)
    
    
