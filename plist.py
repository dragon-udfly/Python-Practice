import numpy as np 

def total(arr): 
    total = 0 
    for i in arr: 
        total = total + i

    return total

def calculate(arr): 
    "calculate from list"
    mean = total(arr) / len(arr) 
    mean = int(mean)
    arr2 = []

    for i in arr: 
        arr2.append(i + mean)

    return arr2

arr1 = np.array([2, 3, 4, 8, 3, 1, 0])

print(arr1)

print(calculate(arr1))