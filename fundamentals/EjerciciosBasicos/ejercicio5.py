 #0,1,1,2,3,5,8
 

def fibonacci (a, b, n):
    if  n == 1:
        print( a+b)
        return a + b 
    
    print(a + b, ", ", end="")
    return fibonacci(b, a+b, n-1) + a+b

#print(fibonacci(13,21,1))
#print(0, ",", 1 , ", ", end="")
a = 0
b = 1
print(a , "," , b , ", ",  end="")
print("Suma total: ", fibonacci(a,b,2)+ a+b )

