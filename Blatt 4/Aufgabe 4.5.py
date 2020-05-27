import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

tv = imread("tv.png")


# 1.
def scale(mode, img, factor):
    if mode == 1:
        # Get new height and new width.
        new_height, new_width = img.shape[0] * factor, img.shape[1] * factor

        # Divide indices of scaled image by factor and unite them with input image.
        x_indices = (np.arange(new_width) / factor).astype(int)
        y_indices = (np.arange(new_height) / factor).astype(int)

        return img[np.ix_(y_indices, x_indices)]
    elif mode == 2:
        # Get new height/width and create "blank" image with it.
        height, width = img.shape[0], img.shape[1]
        new_height, new_width = height * factor, width * factor
        scaled_img = np.zeros((new_height, new_width))

        # Get neighboring pixels, their value and x/y weight, and calculate interpolation.
        for x in range(new_width):
            for y in range(new_height):
                # x/y coordinate in input image.
                x_coord = x / factor
                y_coord = y / factor

                # Neighboring pixels.
                x1 = (np.floor(x_coord)).astype(int) if x_coord > 0 else 0
                y1 = (np.floor(y_coord)).astype(int) if y_coord > 0 else 0
                x2 = (np.ceil(x_coord)).astype(int) if x_coord < width-1 else width-1
                y2 = (np.ceil(y_coord)).astype(int) if y_coord < height-1 else height-1

                # Value of (top left, top right, bottom left, bottom right) pixels.
                tl = img[y1, x1]
                tr = img[y1, x2]
                bl = img[y2, x1]
                br = img[y2, x2]

                # Weight of neighbors.
                xw = x_coord - x1
                yw = y_coord - y1

                # Using interpolation formula to calculate pixel value.
                scaled_img[y][x] = tl * (1 - xw) * (1 - yw) + tr * xw * (1 - yw) + bl * (1 - xw) * yw + br * xw * yw

        return scaled_img
    else:
        return "Select either nearest neighbor (1) or bilinear (2)!"


# 2.
plt.imshow(scale(2, tv, 2), cmap="gray")
plt.show()
# Bilineare Interpolation liefert deutlich sanftere Übergänge zwischen den Graustufen.
