import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import gaussian
from skimage.segmentation import mark_boundaries


# 1.
einstein = imread("einstein.png")
einstein_gauss = gaussian(einstein, sigma=10)
plt.imshow(einstein_gauss, cmap="gray")
plt.show()

# Ungefähr 10, die Kopfform, die Augen, der Mund und die Nase bleiben erkennbar,
# aber sämtliche Details gehen verloren.


# 2.
ballon = imread("ballon.png")
plt.imshow(ballon)
plt.show()

# Regenbogenfarbene "Kacheln" des Ballons, die sich auf dem Grund spiegeln und die Person.

ballon_gauss = gaussian(ballon, sigma=20, multichannel=True)
plt.imshow(ballon_gauss)
plt.show()

# Bei Sigma 10 lässt sich sowohl die Spiegelung als auch die Person noch erkennen.
# Kacheln verschwimmen schon leicht, Absätze sind allerdings noch zu erkennen.
# Ab Sigma 20+ sind die Kacheln fast vollständig verschwommen, man erkennt kaum noch die Spiegelung
# und die Person ist definitiv nicht mehr zu erkennen und auch quasi nicht mehr zu erahnen.


# 3.
gletscher = imread("gletscher.png")
plt.imshow(gletscher, cmap="gray")
plt.show()

gletscher_slice = np.copy(gletscher)
gletscher_slice[gletscher_slice < 130] = 0
gletscher_slice[np.logical_and(gletscher_slice > 130, gletscher_slice < 180)] = 155
gletscher_slice[gletscher_slice > 180] = 255
plt.imshow(gletscher_slice, cmap="gray")
plt.show()

# Moränen, Berge und Himmel lassen sich durch intensity-level slicing relativ gut trennen.
# Einzelne Elemente im See werden jedoch falsch gefärbt,
# da dort sehr viele unterschiedliche Graustufen vorhanden sind.


# 4.
gletscher_gauss = gaussian(gletscher, sigma=20)
gletscher_gauss_slice = np.copy(gletscher_gauss)
gletscher_gauss_slice[gletscher_gauss_slice < 0.4] = 0
gletscher_gauss_slice[np.logical_and(gletscher_gauss_slice > 0.4, gletscher_gauss_slice < 0.8)] = 0.5
gletscher_gauss_slice[gletscher_gauss_slice > 0.8] = 1
plt.imshow(gletscher_gauss_slice, cmap="gray")
plt.show()

# Grenze zwischen Moränen und Bergen und Himmel wird (nun) wie der See markiert.


# 5.
boundaries = mark_boundaries(gletscher, (255 * gletscher_gauss_slice).astype(int))
plt.imshow(boundaries)
plt.show()

# Übergang zwischen Moränen und Bergen und Himmel verschwimmt beim Weichzeichnen.
# Problem ist also hauptsächlich der Übergang zwischen helle(re)n Grautönen und Weiß.
