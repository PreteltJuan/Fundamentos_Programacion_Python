def maximoComunDivisor(a, b):
    if(a < b):
        return maximoComunDivisor (b, a)
    elif(b == 0):
        return a
    else:
        return maximoComunDivisor(b, a%b)

a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

resultado = maximoComunDivisor(a,b)
print (" El MCD es ", resultado )