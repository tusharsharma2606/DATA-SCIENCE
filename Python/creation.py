# wap to demonstrate the array creation function in numpy

import numpy as np

a = np.array([1, 2, 3, 4 ,5])
print("Array:", a)

b = np.arange(0, 10, 2)
print("Array with range:", b)

c = np.linspace(0, 1, 5)
print("Array with linspace:", c)

# d = np.eye(3)
# print("Identity matrix\n:", d)