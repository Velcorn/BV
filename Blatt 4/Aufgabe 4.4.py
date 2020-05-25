import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

tv = imread("tv.png")


# 1.
def scale(img, factor):
    # Calculate new image shape and create new image with it.
    size = (int(img.shape[0] * factor), int(img.shape[1] * factor))
    scaled_img = np.zeros(size)

    # Iterate over all pixels and set their values based on the input image.
    for x in range(size[0]):
        for y in range(size[1]):
            scaled_img[x, y] = img[int(x / factor), int(y / factor)]

    return scaled_img


# 2.
plt.imshow(scale(tv, 2), cmap="gray")
plt.show()

# 3.
# Sieht nicht danach aus. Vorausgesetzt die Funktion ist richtig implementiert ^^

# 4.
half_size = scale(tv, 0.5)
original_size = scale(half_size, 2)
plt.imshow(original_size, cmap="gray")
plt.show()
# Nein, da beim Verkleinern Informationen verloren gehen,
# die beim Vergrößern nicht zurückgewonnen werden (können).
