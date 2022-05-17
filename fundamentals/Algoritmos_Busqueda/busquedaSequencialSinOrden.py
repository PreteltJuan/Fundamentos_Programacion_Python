def busquedaSecuencial(lista, item):
    for i in range(0, len(lista)):
        if(lista[i] == item):
            return True
    return False

listaPrueba = [54, 93, 55, 20, 17, 26, 44, 65, 31, 77]

print(busquedaSecuencial(listaPrueba, 54))