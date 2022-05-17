def potencia(base, exponente):

    if exponente == 0:
        resultado = 1
    else:
        resultado = base * potencia(base, exponente-1) 

    return resultado

base = int(input("Ingrese el valor de la base: "))
exponente = int(input("Ingrese el valor del exponente: "))

if exponente < 0:
    print("El algoritmo no se puede ejecutar para el exponente ingresado")
else:
    print(potencia(base, exponente))

