

def main():
    datosPrestamo = open("prestamo.txt")
    datos = datosPrestamo.readlines()

    valorPrestamo = round(float(datos[0]),2)

    intereses = round(float(datos[1]), 2)
    intereses = intereses / 100
    periodos = round(int(datos[2]),2)
    
    
    saldoActual = valorPrestamo

    file = open("DatosCuotas.txt", "w")
    file.write("Periodo,Intereses,Amortizacion,Cuota,Saldo\n")
    header = "0, , , ," + str(valorPrestamo) + "\n"
    file.write(header)
    for i in range(1, periodos+1):
        periodoActual = str(i) + ","

        interes = nuevosIntereses(saldoActual, intereses)
        periodoActual += str(interes) + ","

        amortizacion = nuevaAmortizacion(valorPrestamo, intereses, periodos, saldoActual)
        periodoActual += str(amortizacion) + ","

        cuota = nuevaCuota(interes, amortizacion)
        periodoActual += str(cuota) + ","

        saldoActual = nuevoSaldo(saldoActual, amortizacion)
        periodoActual += str(saldoActual) + "\n"

        file.write(periodoActual)

    file.close()
    datosPrestamo.close()
    return 0



def nuevosIntereses(valor, interes):
    resultado = valor * interes
    return round(resultado,2)


def nuevaAmortizacion(valorPrestamo, interes, periodos, saldoAnterior):
    resultado = valorPrestamo * ((pow((1 + interes), periodos) * interes) / (
        pow((1 + interes), periodos) - 1)) - (interes * saldoAnterior)
    return round(resultado, 2)


def nuevaCuota(intereses, amortizacion):
    resultado = intereses + amortizacion
    return  round(resultado, 2)


def nuevoSaldo(saldo, amortizacion):
    resultado = saldo-amortizacion
    return  round(resultado, 2)


main()
