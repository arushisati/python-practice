import numpy as np

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

for matrix in arr:
    for row in matrix:
        for item in row:
            print(item)

