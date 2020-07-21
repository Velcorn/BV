import numpy as np
import matplotlib.pyplot as plt
from skimage.io import ImageCollection

imgs = ImageCollection("bild*.png")

# 1.
# Gamma correction: "Aufhellen" des relevanten Bildbereichs.
gamma = 1.5
img1 = np.power(imgs[0], gamma)
plt.imshow(img1, cmap="gray", vmin=0, vmax=255)
plt.show()

# Es sind 8 Poller (den halbwegs verdeckten mitgezählt)


# 2.
# Contrast stretching: Differenzierung der Farben.
minimum = np.min(imgs[1])
maximum = np.max(imgs[1])
img2 = np.round((imgs[1] - minimum) / (maximum - minimum) * 255)
plt.imshow(img2, cmap="gray")
plt.show()


# 3.
# Intensity-level slicing: Hervorheben eines Farbbereichs.
img3 = imgs[2]
img3[np.logical_and(imgs[2] > 100, imgs[2] < 140)] = 255
plt.imshow(img3, cmap="gray")
plt.show()
