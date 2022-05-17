
nombres = []
edades = []

while (True):

    nombre = str(input("Ingrese el nombre del estudiante : "))
    if(nombre == '*'):
        break
   
    edad = int(input("Ingrese la edad del estudiante : ")) 

    nombres.append(nombre)
    edades.append(edad)

datos = list(zip(nombres, edades))
indexMayorEdad = 0

for i in range(0, len(datos)):

    if(datos[i][1] >= 18):
        print(datos[i][0], " es Mayor de edad, pa")

    if(datos[i][1] > datos[indexMayorEdad][1]):
        indexMayorEdad = i
print("La persona de mayor edad es: ", datos[indexMayorEdad][1])