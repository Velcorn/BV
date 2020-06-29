import math
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import sobel


# 1.
mandrill = imread("mandrill.png")
mandrill_sobel = sobel(mandrill)
plt.imshow(mandrill_sobel)
plt.show()

threshold = 0.15
mandrill_sobel[mandrill_sobel > threshold] = 1
mandrill_sobel[mandrill_sobel < threshold] = 0
plt.imshow(mandrill_sobel)
plt.show()

# Die wichtigsten Kanten wurden gefunden,
# es werden allerdings auch das Fell um den Kopf herum sowie die Barthaare erkannt.


# 2.

