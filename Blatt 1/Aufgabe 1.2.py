import numpy as np

u = np.zeros(100)
print(u)
print("\n")

v = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(v)
print("\n")

m = np.reshape(v, (3, 4))
print(m)
print("\n")

m = np.multiply(m, 1.2)
print(m)
print("\n")

m = m.astype(int)
print(m)
print("\n")

m = np.multiply(m, 1.2)
print(m)
print("Data type is: " + str(m.dtype))
print("\n")

m = np.multiply(m, m)
print(m)
