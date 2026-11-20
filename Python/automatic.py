#WAP to perform basic arithmetic operation on numpy array

import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print ("Array A:", a)
print ("Array B:", b)

print ("Addition of A and B:", np.add(a,b))
print ("Subtraction of A and B:", np.subtract(a,b))
print ("Multiplication of A and B:", np.multiply(a,b))
print ("Division of A and B:", np.divide(a,b))
print ("Power of A and B:", np.power(a,b))

print(b)