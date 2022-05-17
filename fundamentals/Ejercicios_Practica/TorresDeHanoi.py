

def moverFicha(indexFicha, indexTorreOrigen, indexTorreDestino, indexTorreApoyo):

    dato = esMovimientoPosible(indexFicha, indexTorreOrigen, indexTorreDestino)

    while(dato != -1 ):
        if(dato == -2):
            moverFicha(indexFicha+1, indexTorreOrigen, indexTorreApoyo, indexTorreDestino)
        else:
            moverFicha(dato, indexTorreDestino, indexTorreApoyo, indexTorreOrigen)
       
        dato = esMovimientoPosible(indexFicha, indexTorreOrigen, indexTorreDestino)

    imprimirMovimiento(indexFicha, indexTorreOrigen, indexTorreDestino)


def imprimirMovimiento(indexFicha, indexTorreOrigen, indexTorreDestino):
    print(contador[-1], ") Mover ficha de la torre ", indexTorreOrigen + 1, " hacia la torre ", indexTorreDestino+1)
    torres[indexTorreDestino].append(torres[indexTorreOrigen][indexFicha])
    torres[indexTorreOrigen].pop()
    contador.append(contador[-1]+1)


def esMovimientoPosible(indexFicha, indexTorreOrigen, indexTorreDestino):
    
    if(torres[indexTorreOrigen][-1] == torres[indexTorreOrigen][indexFicha]):
            if(len(torres[indexTorreDestino]) == 0):
                return -1
            elif(len(torres[indexTorreDestino]) == 1):
                if( torres[indexTorreDestino][0] >  torres[indexTorreOrigen][indexFicha]):
                    return -1
                else:    
                    return 0
            else:
                for i in range(0, len(torres[indexTorreDestino]) ):
                    if(torres[indexTorreDestino][i] < torres[indexTorreOrigen][indexFicha]):
                        return i
                return -1
    else:       
        return -2

def organizarTorres(cantFichas):

    if(cantFichas == 0): 
        print("No hay fichas para mover") 
        return

    for i in range(cantFichas, 0, -1):
        torres[0].append(i)
   
    for i in range(0, cantFichas):
        
        if (len(torres[0]) == 0):
            moverFicha(0, 1, 2, 0)
        elif (len(torres[1]) == 0):
            moverFicha(0, 0, 2, 1)
        elif (torres[0][0] > torres[1][0]):
           moverFicha(0, 0, 2, 1)
        else :
           moverFicha(0, 1, 2, 0)


    print("Todas las fichas se movieron a la torre 3")
        
torre1 = []
torre2 = []
torre3 = []
torres = [torre1, torre2, torre3]
contador = [1]


cantFichas = int(input("Ingrese la cantidad de fichas: "))

organizarTorres(cantFichas)


