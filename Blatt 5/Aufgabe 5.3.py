import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
import math

mandrill = imread("mandrillFarbe.png")


def rgb_to_cmy(img):
    return 1 - img / 255


def cmy_to_rgb(img):
    return (255 * (1 - img)).astype(int)


def rgb_to_hsi(img):
    img = img / 255

    r = img[:, :, 0]
    g = img[:, :, 1]
    b = img[:, :, 2]

    i = np.divide(r + g + b, 3)
    s = 1 - np.multiply(np.divide(3, r + g + b), np.minimum(r, g, b))
    # h = math.pow(math.cos, 2)


print(rgb_to_hsi(mandrill))


def hsi_to_rgb(img):
    return ""


# RGB to CMY
plt.imshow(rgb_to_cmy(mandrill))
# plt.show()

# CMY to RGB
plt.imshow(cmy_to_rgb(rgb_to_cmy(mandrill)))
# plt.show()

# RGB to HSI
'''plt.imshow(rgb_to_hsi(mandrill))
plt.show()

# HSI to RGB
plt.imshow(hsi_to_rgb(rgb_to_hsi(mandrill)))
plt.show()
'''