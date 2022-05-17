def invertirpalabra(string):
    if len(string) == 0:
        return(string)
    else:
        return invertirpalabra(string[1:]) + string[0]

string=str(input("ingrese la palabra que quiere invertir: "))
print("original: ")
print(string)
print("invertido: ")
print(invertirpalabra(string))