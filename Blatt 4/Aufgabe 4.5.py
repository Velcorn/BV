import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

tv = imread("tv.png")


# 1.
def scale(mode, img, factor):
    if mode == 1:
        # Calculate new image shape and create new image with it.
        size = (int(img.shape[0] * factor), int(img.shape[1] * factor))
        scaled_img = np.zeros(size)

        # Iterate over all pixels and set their values based on the input image.
        for x in range(size[0]):
            for y in range(size[1]):
                scaled_img[x, y] = img[int(x / factor), int(y / factor)]

        return scaled_img

    elif mode == 2:
        return ""
    else:
        return "Select either nearest neighbor (1) or bilinear (2)!"


# 2.
plt.imshow(scale(1, tv, 2), cmap="gray")
plt.show()
