import numpy as np
from skimage.io import imread

# 1.
mandrill = imread("mandrill.png")

# 2.
minimum = np.amin(mandrill)
maximum = np.amax(mandrill)
average = np.average(mandrill)
deviation = np.std(mandrill)
print(f"Minimum: {minimum}")
print(f"Maximum: {maximum}")
print(f"Average: {average}")
print(f"Deviation: {deviation}")

# 3.
minxy = np.unravel_index(np.argmin(mandrill, axis=None), mandrill.shape)
maxxy = np.unravel_index(np.argmax(mandrill, axis=None), mandrill.shape)
print(f"Minimum xy: {minxy}")
print(f"Maximum xy: {maxxy}")

# 4.
even_count = np.count_nonzero(mandrill % 2 == 0)
odd_count = np.count_nonzero(mandrill % 2 != 0)
print(f"Even: {even_count}")
print(f"Odd: {odd_count}")

# 5.
coordinates = np.argwhere(mandrill % 2 == 0)
print(f"Even coordinates: {coordinates}")
