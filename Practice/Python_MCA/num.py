#numpy arrays
import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print(type(b))

c = np.array([1, 2, 3, 4, 5], ndmin = 2)
print(c)
print(type(c))

d = np.array([1, 2, 3], dtype = complex)
print(d)
print(type(d))

e = np.array([[1, 2, 3], [4, 5, 6]], dtype = complex)
print(e)
print(type(e))