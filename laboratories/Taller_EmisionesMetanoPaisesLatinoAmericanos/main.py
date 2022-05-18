
def main():

    emisiones_metano = open("EMISIONES DE METANO.csv", encoding="utf8")
    paisesLatinoAmericanos = obtenerInfoPaisesLatinoAmericanos(
        emisiones_metano)

    emisionesTotalesPorPais(paisesLatinoAmericanos)
    emisionesTotalesPorAño(paisesLatinoAmericanos)
    emisiones_metano.close()


def emisionesTotalesPorAño(data):
    emisionesPorAño = [0] * 10
    for i in range(10):
        for j in range(10):
            emisionesPorAño[i] += float(data[j][53+i])

    
    em = "Emisiones de metano(kt de equivalente de CO2)"
    emisionesTotalesPorAño = open(
        "emisionesTotalesPorAñoPaisesLatinoAmericanos.csv", "w", encoding="utf8")
    emisionesTotalesPorAño.write("Año,Emisión Total,Indicator Name,\n")
    for i in range(10):
        line = str(2009+i) + "," + str(emisionesPorAño[i]) + "," + em + ",\n"
        emisionesTotalesPorAño.write(line)
    emisionesTotalesPorAño.close()

def emisionesTotalesPorPais(data):

    emisionesPorPais = [0] * 10
    for i in range(10):
        for j in range(53, 63):
            emisionesPorPais[i] += float(data[i][j])
        
    em = "Emisiones de metano(kt de equivalente de CO2)"
    emisionesTotalesPorPais = open(
        "emisionesTotalesPorPaisPaisesLatinoAmericanos.csv", "w", encoding="utf8")
    emisionesTotalesPorPais.write(
        "Country Name,Country Code,Indicator Name,Total Emissions2009-2018,\n")
    for i in range(10):
        line = data[i][0] + "," + data[i][1] + "," + em + "," + str(emisionesPorPais[i]) + ",\n"
        emisionesTotalesPorPais.write(line)
    emisionesTotalesPorPais.close()


def obtenerInfoPaisesLatinoAmericanos(data):
    paisesLatinoAmericanos = ["ARG", "BOL", "BRA",
                              "CHL", "COL", "ECU", "PRY", "PER", "URY", "VEN"]

    dataPaisesLatinoAmericanos = []
    
    for datos in data:
        datos_separados = datos.split(",")
        print(datos_separados[0])
        if datos_separados[1] in paisesLatinoAmericanos:
            dataPaisesLatinoAmericanos.append(datos_separados)
    return dataPaisesLatinoAmericanos


main()
