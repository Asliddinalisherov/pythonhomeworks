import numpy as np
@np.vectorize
def fahrenheit_to_celsius(f):
    return (f - 32) * ( 5 / 9 )

f_temperature = np.array([32,68,100,212,77])
c_temperature = fahrenheit_to_celsius(f_temperature)
print(c_temperature)