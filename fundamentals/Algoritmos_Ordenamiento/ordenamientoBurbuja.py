def ordenar(arr):
    for i in range (1, len(arr)):
        for j in range (len(arr)-2):
            if (arr[j] > arr[j+1]):
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
            
arr = {3,4,3,6,8,2,4}

ordenar(arr)

print(arr)
