import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import gaussian, laplace, sobel
from skimage.util import random_noise


# 1.
mandrill = imread("mandrill.png")
mandrill_gf = gaussian(mandrill, sigma=3)
mandrill_gn = random_noise(mandrill, mode="gaussian", var=0.01)
'''plt.imshow(mandrill, cmap="gray")
plt.show()
plt.imshow(mandrill_gf, cmap="gray")
plt.show()
plt.imshow(mandrill_gn, cmap="gray")
plt.show()'''


# 2.
mandrill_l = laplace(mandrill)
mandrill_gfl = laplace(mandrill_gf)
mandrill_gnl = laplace(mandrill_gn)
'''plt.imshow(mandrill_l, cmap="gray")
plt.show()
plt.imshow(mandrill_gfl, cmap="gray")
plt.show()
plt.imshow(mandrill_gnl, cmap="gray")
plt.show()


# 3.
mandrill_gngf = gaussian(mandrill_gn, sigma=2)
mandrill_gngfl = laplace(mandrill_gngf)
plt.imshow(mandrill_gngfl, cmap="gray")
plt.show()'''


# 4.
mandrill_gfle = np.zeros(mandrill.shape)
height, width = mandrill.shape[:2]
for x in range(1, width-1):
    for y in range(1, height-1):
        # Get neighbors, top, bottom, top right, bottom left, top left, bottom left.
        nt = mandrill_gfl[y-1, x]
        nb = mandrill_gfl[y+1, x]
        ntr = mandrill_gfl[y-1, x+1]
        nbl = mandrill_gfl[y+1, x-1]
        ntl = mandrill_gfl[y-1, x-1]
        nbr = mandrill_gfl[y+1, x+1]

        # Check if opposing neighbors have different sign and if their difference is above threshold
        th = 0.007
        if nt * nb < 0 and abs(nt - nb) > th or \
                ntr * nbl < 0 and abs(ntr - nbl) > th or ntl * nbr < 0 and abs(ntl - nbr) > th:
            mandrill_gfle[y, x] = 1
        else:
            mandrill_gfle[y, x] = 0
plt.imshow(mandrill_gfle, cmap="gray")
plt.show()


# 5.
mandrill_sobel = sobel(mandrill)
threshold = 0.15
mandrill_sobel[mandrill_sobel > threshold] = 1
mandrill_sobel[mandrill_sobel < threshold] = 0
plt.imshow(mandrill_sobel)
plt.show()
