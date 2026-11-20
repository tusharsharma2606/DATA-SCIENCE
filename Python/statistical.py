# WAP to compute basic statistical measure on a numpy array

import numpy as np
a = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

np.mean(a)
np.std(a)

print("Mean of the array:", np.mean(a))
print("Standard Deviation of the array:", np.std(a))