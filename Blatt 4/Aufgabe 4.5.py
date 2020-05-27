import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

tv = imread("tv.png")


# 1.
def scale(mode, img, factor):
    if mode == 1:
        # Get new height and new width.
        height, width = img.shape[0], img.shape[1]
        new_height, new_width = (np.round(height * factor)).astype(int), (np.round(width * factor)).astype(int)

        # Divide indices of scaled image by factor and unite them with input image.
        x_indices = (np.arange(new_width) / factor).astype(int)
        y_indices = (np.arange(new_height) / factor).astype(int)

        return img[np.ix_(y_indices, x_indices)]
    elif mode == 2:
        # Get new height/width and create "blank" image with it.
        height, width = img.shape[0], img.shape[1]
        new_height, new_width = (np.round(height * factor)).astype(int), (np.round(width * factor)).astype(int)
        scaled_img = np.zeros((new_height, new_width))

        # Calculate scalin ratios.
        x_ratio = (width - 1) / (new_width - 1)
        y_ratio = (height - 1) / (new_height - 1)

        # Get neighboring pixels, their value and x/y weight and calculate interpolation.
        for x in range(new_width):
            for y in range(new_height):
                x1 = (np.floor(x * x_ratio)).astype(int)
                y1 = (np.floor(y * y_ratio)).astype(int)
                x2 = (np.ceil(x * x_ratio)).astype(int)
                y2 = (np.ceil(y * y_ratio)).astype(int)

                tl = img[y1, x1]
                tr = img[y1, x2]
                bl = img[y2, x1]
                br = img[y2, x2]

                xw = (x_ratio * x) - x1
                yw = (y_ratio * y) - y1

                scaled_img[y][x] = tl * (1 - xw) * (1 - yw) + tr * xw * (1 - yw) + bl * (1 - xw) * yw + br * xw * yw

        return scaled_img
    else:
        return "Select either nearest neighbor (1) or bilinear (2)!"


# 2.
plt.imshow(scale(2, tv, 2), cmap="gray")
plt.show()
# Bilineare Interpolation liefert deutlich sanftere Übergänge zwischen den Graustufen.
