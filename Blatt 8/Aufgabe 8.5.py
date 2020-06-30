import math
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import sobel, sobel_h, sobel_v

opera = imread("opera.png")
blueness = np.zeros((opera.shape[0], opera.shape[1]))
for x in range(blueness.shape[1]):
    for y in range(blueness.shape[0]):
        px = opera[y, x]
        euclidian_distance = np.linalg.norm(px - np.asarray([0, 0, 255]))
        blueness[y, x] = euclidian_distance
blueness *= (255.0 / np.max(blueness))
blueness_sobel = sobel(blueness)


# 1.
degrees = np.degrees(np.arctan(np.divide(sobel_v(blueness), sobel_h(blueness) + 0.0001)))
degrees[np.logical_and(degrees > -22.5, degrees < 22.5)] = 0
degrees[np.logical_and(degrees > 22.5, degrees < 67.5)] = 45
degrees[np.logical_and(degrees > -67.5, degrees < -22.5)] = -45
degrees[np.logical_or(degrees > 67.5, degrees < -67.5)] = 90
result = np.zeros(blueness.shape)


# 2.+3.
height, width = blueness_sobel.shape[:2]
for x in range(width):
    for y in range(height):
        if degrees[y, x] == 0:
            if x-1 >= 0:
                n1 = blueness_sobel[y, x-1]
            else:
                n1 = 0
            if x+1 <= width-1:
                n2 = blueness_sobel[y, x+1]
            else:
                n2 = 0
        elif degrees[y, x] == 45:
            if x-1 >= 0 and y-1 >= 0:
                n1 = blueness_sobel[y-1, x-1]
            else:
                n1 = 0
            if x+1 <= width-1 and y+1 <= height-1:
                n2 = blueness_sobel[y+1, x+1]
            else:
                n2 = 0
        elif degrees[y, x] == -45:
            if x-1 >= 0 and y+1 <= height-1:
                n1 = blueness_sobel[y+1, x-1]
            else:
                n1 = 0
            if x+1 <= width-1 and y-1 >= 0:
                n2 = blueness_sobel[y-1, x+1]
            else:
                n2 = 0
        else:
            if y-1 >= 0:
                n1 = blueness_sobel[y-1, x]
            else:
                n1 = 0
            if y+1 <= height-1:
                n2 = blueness_sobel[y+1, x]
            else:
                n2 = 0

        if blueness_sobel[y, x] > n1 or blueness_sobel[y, x] > n2:
            result[y, x] = blueness_sobel[y, x]
        else:
            result[y, x] = 0
result *= (1.0 / np.max(result))


plt.imshow(result)
# plt.show()

# Sieht ok aus ^^'


# 4.
threshold = 0.2
result[result > threshold] = 1
result[result < threshold] = 0

plt.imshow(result)
plt.show()

# Nicht ganz, aber lassen wir mal gelten. (Mir fällt einfach keine Lösung ein :P)
