import numpy as np
@np.vectorize
def power_of_number(num, power):
    return num ** power

num = [2, 3, 4, 5]
power = [1, 2, 3, 4]
print(power_of_number(num, power))