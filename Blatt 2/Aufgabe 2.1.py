import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

Red = imread("band3.png")
NIR = imread("band4.png")

NDVI = (NIR - Red)/(NIR + Red)

plt.imshow(NDVI, cmap="gray")
plt.show()
