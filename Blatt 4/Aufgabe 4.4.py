import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

tv = imread("tv.png")


# 1.
def scale(img, factor):
    # Calculate new image shape and create new image with it.
    height, width = img.shape[:2]
    new_height, new_width = (int(height * factor), int(width * factor))[:2]
    scaled_img = np.zeros([new_height, new_width])

    # Iterate over all pixels and set their values based on the input image.
    for x in range(new_height):
        for y in range(new_width):
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
