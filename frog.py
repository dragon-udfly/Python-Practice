import numpy as np 

array = np.array([34, 22, 99, 90, 34, 54, 23, 39])

print(f"Array: \n{array}")

array = array * 2 

print(f"New Array: \n{array}")

print(f"Dimension: {array.ndim}")

arr = np.array([
    [34, 30, 10, 34, 23, 29], 
    [34, 10, 20, 34, 42, 95], 
    [94, 53, 92, 84, 20, 25]
])

print(f"Dimension: {arr.ndim}")

arr1 = np.array([
    [[34, 233, 23], [33, 53, 32], [23, 0, 23]], 
    [[34, 99, 78], [33, 56, 78], [23, 24, 93]], 
    [[34, 34, 43], [56, 78, 33], [0, 0, 0]]
])

print(f"Dimension: {arr1.ndim}")

print(f"Depth: {arr1.shape[0]}, Rows: {arr1.shape[1]}, Columns: {arr1.shape[2]}")

arr2 = np.array([
    [[56, 233, 23], [33, 53, 32], [23, 0, 23]], 
    [[67, 99, 78], [33, 56, 78], [23, 24, 93]]
])

print(f"Depth: {arr2.shape[0]}, Rows: {arr2.shape[1]}, Columns: {arr2.shape[2]}")

print(f"Element: {arr2[0][0][2]}")