import numpy as np


x_array = np.array([
    [4, 5, 6], 
    [3, -1, 1], 
    [2, 1, -2]
])
y_array = np.array([7, 4, 5])

print(np.linalg.solve(x_array, y_array))
