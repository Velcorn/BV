import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

tv = imread("tv.png")


# 1.
def scale(img, factor):
    # Get new height and new width.
    height, width = img.shape[0], img.shape[1]
    new_height, new_width = (np.round(height * factor)).astype(int), (np.round(width * factor)).astype(int)

    # Divide indices of scaled image by factor and unite them with input image.
    x_indices = (np.arange(new_width) / factor).astype(int)
    y_indices = (np.arange(new_height) / factor).astype(int)

    return img[np.ix_(y_indices, x_indices)]


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
