import numpy as np


x_array = np.array([
    [10, -2, 3], 
    [-2, 8, -1], 
    [3, -1, 6]
])
y_array = np.array([12, -5, 15])
solution = np.linalg.solve(x_array, y_array)
print("Solution for (I1, I2, I3):", solution)