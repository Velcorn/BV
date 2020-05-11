import numpy as np
from skimage.io import imread

# 1.
mandrill = imread("mandrill.png")

# 2.
minimum = np.amin(mandrill)
maximum = np.amax(mandrill)
average = np.average(mandrill)
deviation = np.std(mandrill)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)
print("Deviation:", deviation)

# 3.
minxy = np.unravel_index(np.argmin(mandrill, axis=None), mandrill.shape)
maxxy = np.unravel_index(np.argmax(mandrill, axis=None), mandrill.shape)
print("Minimum xy:", minxy)
print("Maximum xy:", maxxy)

# 4.
even_count = np.count_nonzero(mandrill % 2 == 0)
odd_count = np.count_nonzero(mandrill % 2 != 0)
print("Even:", even_count)
print("Odd:", odd_count)

# 5.
coordinates = np.argwhere(mandrill % 2 == 0)
print("Even coordinates:", coordinates)
