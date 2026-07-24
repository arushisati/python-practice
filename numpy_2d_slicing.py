import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

print(arr[0])        # First row
print(arr[:,1])      # Second column
print(arr[:2,:2])    # 2x2 block
print(arr[1:,1:])    # Bottom-right
