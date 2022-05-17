def llenarComuna(proyectos_inversion):
  encabezado = proyectos_inversion.readline()
  mi_comuna = open("miComuna14.csv", "w") 
  mi_comuna.write(encabezado)
  for datos in proyectos_inversion:
    datos_separados = datos.split(';')
    if '0' in datos_separados[2] and '14' in datos_separados[5]:
      mi_comuna.write(datos)


def total_inversionxDependencia(mi_comuna):
  mi_comuna.seek(0)
  diccionario = {}
 
  for datos in mi_comuna:
    
    datos_separados = datos.split(';')
    dependencia = datos_separados[1]
    valor = datos_separados[7]


    charsToRemove = [".", "$"]
    for i in charsToRemove:
      valor =  valor.replace(i,"") 


    try:
      valor = (int(valor))
      if diccionario.get(dependencia): 
        diccionario[dependencia] =  valor + diccionario.get(dependencia)
      else: 
        diccionario[dependencia] =  valor
    except:
      None
    

  return diccionario

def proyectosxDepencia(mi_comuna):
  mi_comuna.seek(0)
  diccionario = {}
 
  for datos in mi_comuna:
    
    datos_separados = datos.split(';')
    dependencia = datos_separados[1]

    if diccionario.get(dependencia): 
      diccionario[dependencia] =  1 + diccionario.get(dependencia)
    else: 
      diccionario[dependencia] =  1

  for key in diccionario:
    print("La dependencia " , key, " tiene ", diccionario[key], " proyectos." )

def main():


  proyectos_inversion = open("./proyectos_inversion2020.csv")
  llenarComuna(proyectos_inversion)

  mi_comuna = open("miComuna14.csv")

  proyectosxDepencia(mi_comuna)
  print(total_inversionxDependencia(mi_comuna))

  mi_comuna.close()
  proyectos_inversion.close()

main()