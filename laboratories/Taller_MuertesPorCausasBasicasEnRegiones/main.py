from random import random

def totalMuertesDepartamento(datos):
    total = 0
    for i in range (len(datos)):
        for j in range(len(datos[i])):
            total += datos[i][j]
    return total

def porcentajeMuertesPorCausa(datos, totalMuertes):
    porcentajes = []
    for i in range (len(datos)):
        temp = 0
        for j in range(len(datos[i])):
            temp += datos[i][j]
        porcentajes.append(round((temp * 100/totalMuertes), 2))
    return porcentajes
    
def causaYRegionConMenosMuertes(datos, regiones, causabasica):
    x = 0
    y = 0
    for i in range (len(datos)):
        for j in range(len(datos[i])):
            if datos[i][j] < datos[x][y]:
                x = i
                y = j
    print("La menor causa de muertes fue ", causabasica[x], " en la region ", regiones[y], " con " , datos[x][y], " muertes ")


def regionsMayorNumeroMuertes(datos, regiones):
    cantMuertesPorRegion = [0,0,0,0,0,0,0,0,0,0]
    indicesRegionesMayorNumeroMuertes = [0,0]

    for i in range(len(datos)):
        for j in range(len(datos[i])):
            cantMuertesPorRegion[j] += datos[i][j]
            
    
    for i in range(len(cantMuertesPorRegion)):

        if cantMuertesPorRegion[i] > cantMuertesPorRegion[indicesRegionesMayorNumeroMuertes[0]]:
            indicesRegionesMayorNumeroMuertes[1] = indicesRegionesMayorNumeroMuertes[0]
            indicesRegionesMayorNumeroMuertes[0] = i
        elif cantMuertesPorRegion[i] > cantMuertesPorRegion[indicesRegionesMayorNumeroMuertes[1]]:
            indicesRegionesMayorNumeroMuertes[1] = i

    print("Las regiones con mayor número de muertes son ", regiones[indicesRegionesMayorNumeroMuertes[0]], " y " , regiones[indicesRegionesMayorNumeroMuertes[1]])
    


datos = [[],[],[],[],[]]
regiones = ["Medellín", "Uraba", "B. Cauca", "Oriente", "V. Aburrá", "Suroeste", "Occidente", "Nordeste", "Norte", "Magdalena"]
causasBasicas = ["Trastornos hipertensivos del embarazo","Sepsis no obstétrica","Hemorragia","Cáncer","Aborto",]


def llenarInformacion():
   
    for i in range(len(causasBasicas)):
        for j in range(len(regiones)):
            #print("Datos para la región ", regiones[i])
            #print("Ingrese número de muertes por " + causaBasica[j], ": ", end="")
            #datos[j].append( input())
            datos[i].append(int(random() * 20))

        

def mostrarInformacion():
    for i in regiones:
        print(i, " ", end="")
    print()
    for i in range (len(datos)):
        
        for j in range(len(datos[i])):
            print("   ", datos[i][j], "  ", end="")
        print("- ", causasBasicas[i], " ", end="")
        print()
        
    

llenarInformacion()
mostrarInformacion()

totalMuertes = totalMuertesDepartamento(datos)

print("Total muertes departamento: " , totalMuertes)
print()


porcentajes = porcentajeMuertesPorCausa(datos, totalMuertes)
print("Porcentajes de muertes por cada causa: ")
for i in range(len(causasBasicas)):
    print(causasBasicas[i], ": ", end="")
    print(porcentajes[i], "%")
    
causaYRegionConMenosMuertes(datos, regiones, causasBasicas)
regionsMayorNumeroMuertes(datos, regiones)