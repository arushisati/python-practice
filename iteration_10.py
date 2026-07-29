import numpy as np

arr = np.array([[10, 20],
                [30, 40]])

for row in arr:
    for value in row:
        print("Value =", value)
