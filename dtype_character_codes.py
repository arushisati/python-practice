import numpy as np

arr1 = np.array([1, 2, 3], dtype="i")
arr2 = np.array([1, 2, 3], dtype="f")
arr3 = np.array([True, False], dtype="?")

print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)
