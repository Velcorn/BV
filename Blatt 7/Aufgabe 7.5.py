import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import gaussian
from skimage.segmentation import *


# 1.
einstein = imread("einstein.png")
einstein_gauss = gaussian(einstein, sigma=10)
plt.imshow(einstein_gauss, cmap="gray")
# plt.show()

# Ungefähr 10, die Kopfform, die Augen, der Mund und die Nase bleiben erkennbar,
# aber sämtliche Details gehen verloren.


# 2.
ballon = imread("ballon.png")
plt.imshow(ballon)
# plt.show()

# Regenbogenfarbene "Kacheln" des Ballons, die sich auf dem Grund spiegeln und die Person.

ballon_gauss = gaussian(ballon, sigma=20, multichannel=True)
plt.imshow(ballon_gauss)
# plt.show()

# Bei Sigma 10 lässt sich sowohl die Spiegelung als auch die Person noch erkennen.
# Kacheln verschwimmen schon leicht, Absätze sind allerdings noch zu erkennen.
# Ab Sigma 20+ sind die Kacheln fast vollständig verschwommen, man erkennt kaum noch die Spiegelung
# und die Person ist definitiv nicht mehr zu erkennen und auch quasi nicht mehr zu erahnen.


# 3.
gletscher = imread("gletscher.png")
plt.imshow(gletscher, cmap="gray")
plt.show()
