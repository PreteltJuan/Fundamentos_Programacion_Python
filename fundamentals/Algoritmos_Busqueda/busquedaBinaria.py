def busquedaBinaria(lista, item):
    inicio = 0
    fin = len(lista)-1

    while( not inicio > fin):

        medio = int((inicio + fin)/2)
        if lista[medio] == item:
            return medio
        elif item > lista[medio]:
            inicio = medio + 1  
        else:
            fin = medio - 1

        



lista = [1, 2, 3, 4]
print(busquedaBinaria(lista, 3))
