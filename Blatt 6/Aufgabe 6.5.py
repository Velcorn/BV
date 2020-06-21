import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt


def equalize_hist(img):
    hist = np.histogram(img.flatten(), 256, [0, 256], density=True)[0]
    tf = []
    tv = 0
    for v in hist:
        tv += 255 * v
        tf.append(int(tv))
    eq_hist = np.asarray(tf)
    he_img = np.reshape(eq_hist[img.flatten()], img.shape)
    return eq_hist, he_img


# 1.
moon = imread("moon.png")
plt.figure("Moon Original")
plt.imshow(moon, cmap="gray", vmin=0, vmax=255)
plt.show()

plt.figure("Histogram Equalization Moon")
plt.imshow(equalize_hist(moon)[1], cmap="gray", vmin=0, vmax=255)
plt.show()


# 2.
def eq_hist_tiles(img, tile_size):
    height, width = img.shape[:2]

    # Loop through every tile of the image,
    # apply the histogram equalization on each tile
    # and save the resulting tiles in a new array.
    tile_img = np.zeros(img.shape)
    for x in np.arange(width - tile_size + 1, step=tile_size):
        for y in np.arange(height - tile_size + 1, step=tile_size):
            tile_img[x:x+tile_size, y:y+tile_size] = equalize_hist(img[x:x+tile_size, y:y+tile_size])[1]

    return tile_img


plt.figure("64x64 Tiles")
plt.imshow(eq_hist_tiles(moon, 64), cmap="gray", vmin=0, vmax=255)
plt.show()

# Die einzelnen Kacheln werden detailreicher.

# 3.
plt.figure("32x32 Tiles")
plt.imshow(eq_hist_tiles(moon, 32), cmap="gray", vmin=0, vmax=255)
plt.show()

plt.figure("16x16 Tiles")
plt.imshow(eq_hist_tiles(moon, 16), cmap="gray", vmin=0, vmax=255)
plt.show()

plt.figure("8x8 Tiles")
plt.imshow(eq_hist_tiles(moon, 8), cmap="gray", vmin=0, vmax=255)
plt.show()

plt.figure("4x4 Tiles")
plt.imshow(eq_hist_tiles(moon, 4), cmap="gray", vmin=0, vmax=255)
plt.show()

plt.figure("2x2 Tiles")
plt.imshow(eq_hist_tiles(moon, 2), cmap="gray", vmin=0, vmax=255)
plt.show()

# Noise erhöht sich bei jeder Verkleinerung der Kacheln.
