def areaTriangulo(base, altura):

   return base * altura / 2

print(areaTriangulo(4,3))

def factorial(n):

    producto =1

    for i in range(1, n+1):

        producto *=i

        print(" para el valor",i,producto)

    return producto


print(" el resultado del factorial es",factorial(4))