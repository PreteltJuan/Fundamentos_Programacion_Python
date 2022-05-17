def factorial(n):
    
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


print("El factorial es: ", factorial(4))