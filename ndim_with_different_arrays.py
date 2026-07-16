import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
c = np.array([[[1], [2]], [[3], [4]]])

print("1D ndim:", a.ndim)
print("2D ndim:", b.ndim)
print("3D ndim:", c.ndim)
