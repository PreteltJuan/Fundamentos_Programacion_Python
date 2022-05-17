a = str(input("Ingrese una palabra: "))


def isPalindromo(cadena, n = 0):

    if(n > int(len(cadena)/2)):
        return True

    if(cadena[n] == cadena[len(cadena)-n-1]):
        return isPalindromo(a, n+1)
    else:
        return False 


if(isPalindromo(a)):
    print(a, "es una palabra palíndromo")
else:
    print(a, "NO es una palabra palíndromo")