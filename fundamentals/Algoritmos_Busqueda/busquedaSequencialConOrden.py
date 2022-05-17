def busquedaSecuencialOrdenada(unaLista, item):

    pos = 0

    encontrado = False

    parar = False

    while pos < len(unaLista) and not encontrado and not parar:

        if unaLista[pos] == item:

            encontrado = True

        else:

            if unaLista[pos] > item:

                parar = True

            else:

                pos = pos+1

    return encontrado


listaPrueba = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]

print(busquedaSecuencialOrdenada(listaPrueba, 20))

print(busquedaSecuencialOrdenada(listaPrueba, 13))
