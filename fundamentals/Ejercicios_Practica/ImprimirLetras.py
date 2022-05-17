
def imprimirLetras(finalWord, n = 1):
    if(n == len(finalWord)):
        print(finalWord)
        return
    print( finalWord[0:n] )
    return imprimirLetras(finalWord, n +1)

word = str(input("Ingrese una palabra para imprimir sus letras: "))
imprimirLetras(word)
