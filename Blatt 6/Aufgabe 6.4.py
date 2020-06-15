import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
import time

# 1.
bild1 = imread("bild1.png")
bild2 = imread("bild2.png")

hist1 = np.histogram(bild1, bins=256, range=(0, 256), density=True)
hist2 = np.histogram(bild2, bins=256, range=(0, 256), density=True)

'''plt.figure(1)
plt.hist(bild1.flatten(), bins=256, range=(0, 256), density=True)
plt.show()
plt.figure(2)
plt.hist(bild2.flatten(), bins=256, range=(0, 256), density=True)
plt.show()'''


# 2.
def equalize_hist(hist):
    print(hist[0])
    t = []
    val = 0
    for x in range(len(hist[0])):
        val += 255 * hist[0][x]
        t.append(int(val))

    a = np.asarray(t)

    return a


plt.figure(3)
plt.hist(equalize_hist(hist1), bins=256, range=(0, 256), density=True)
plt.show()

plt.imshow(equalize_hist(hist1), vmin=0, vmax=255)
plt.show()
