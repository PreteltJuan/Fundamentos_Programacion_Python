def fib_intervalo(x):
    """ Retorna los números de Fibonacci 
    mayor que x y menor que x"""
    if x < 0:
        return -1
    ant,post, lub = (0,1,0)
    while True:
        if post >= x:
            return (ant, post)
            #lub = post 
        (ant,post) = (post,ant+post)   
        
        
            
while True:
    x = int(input("Ingrese un número entero >0 (<0 para interrumpir): "))
    if x <= 0:
        break #interrumpe el programa si x<0
    lub, sup = fib_intervalo(x)
    print("Mayor número de Fibonacci menor que x: " + str(lub))
    print("Menor número de Fibonacci mayor que x: " + str(sup))



