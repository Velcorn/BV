import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from math import ceil, floor
from scipy.ndimage import zoom

tv = imread("tv.png")


# 1.
def scale(mode, img, factor):
    if mode == 1:
        height, width = img.shape[:2]
        new_height, new_width = (int(height * factor), int(width * factor))[:2]
        scaled_img = np.zeros([new_height, new_width])

        for x in range(new_width):
            for y in range(new_height):
                scaled_img[y, x] = img[int(y / factor), int(x / factor)]

        return scaled_img

    elif mode == 2:
        height, width = img.shape[:2]
        new_height, new_width = (int(height * factor), int(width * factor))[:2]
        scaled_img = np.zeros([new_height, new_width])

        x_ratio = float((width-1) / (new_width-1)) if new_width > 0 else 0
        y_ratio = float((height-1) / (new_height-1)) if new_height > 0 else 0

        for x in range(new_width):
            for y in range(new_height):
                xl, yt = floor(x_ratio * x), floor(y_ratio * y)
                xr, yb = ceil(x_ratio * x), ceil(y_ratio * y)

                x_weight = (x_ratio * x) - xl
                y_weight = (y_ratio * y) - yt

                tl = img[yt, xl]
                tr = img[yt, xr]
                bl = img[yb, xl]
                br = img[yb, xr]

                pixel = tl * (1-x_weight) * (1-y_weight) + \
                    tr * x_weight * (1-y_weight) + \
                    bl * y_weight * (1-x_weight) + \
                    br * x_weight * y_weight

                scaled_img[y][x] = pixel

        return scaled_img
    else:
        return "Select either nearest neighbor (1) or bilinear (2)!"


# 2.
plt.imshow(scale(2, tv, 2), cmap="gray")
# plt.imshow(zoom(tv, 2, order=1), cmap="gray")
plt.show()
