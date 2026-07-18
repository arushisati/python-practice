import numpy as np

arr = np.array([1.5, 2.9, 3.1])

print("Original:", arr)

new_arr = arr.astype(int)

print("Converted:", new_arr)
print("Dtype:", new_arr.dtype)
