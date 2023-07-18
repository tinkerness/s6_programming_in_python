import numpy as np

arr = np.array([1,2,3,4,5,6])
print(arr[1:5])   # [2 3 4 5]
print(arr[:4])   # [1 2 3 4]
print(arr[2:-1])  # [3 4 5]
print(arr[-2:-1])   # [5]

# 2d array
arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2[1:,2:4])