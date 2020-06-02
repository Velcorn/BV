import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt
from math import acos, cos, sqrt

mandrill = imread("mandrillFarbe.png")


def rgb_to_cmy(img):
    return np.subtract(1, np.divide(img, 255))


def cmy_to_rgb(img):
    return np.multiply(np.subtract(1, img), 255).astype(int)


def rgb_to_hsi(img):
    # Normalize RGB values.
    img = np.divide(img, 255)

    # Calculate HSI values for each pixel based on the formulas.
    for x in range(img.shape[1]-1):
        for y in range(img.shape[0]-1):
            px = img[y, x]
            r = px[0]
            g = px[1]
            b = px[2]

            theta = acos(0.5 * ((r - g) + (r - b)) / (sqrt((r - g) ** 2 + (r - b) * (g - b)) + 0.0001))
            if b <= g:
                h = theta
            else:
                h = 360 - theta
            h /= 360
            s = 1 - 3 / (r + b + g) * min(r, g, b)
            i = 1 / 3 * (r + g + b)

            img[y, x] = h, s, i

    return img


def hsi_to_rgb(img):
    # Calculate RGB values for each pixel based on the formulas.
    for x in range(img.shape[1]-1):
        for y in range(img.shape[0]-1):
            px = img[y, x]
            h = px[0]
            h *= 360
            s = px[1]
            i = px[2]

            if 0 <= h <= 120:
                b = i * (1 - s)
                r = i * (1 + s * cos(h) / cos(60 - h))
                g = 3 * i - (r + b)
            elif 120 <= h <= 240:
                h -= 120
                r = i * (1 - s)
                g = (1 + s * cos(h) / cos(60 - h))
                b = 3 * i - (r + g)
            else:
                h -= 240
                g = i * (1 - s)
                b = (1 + s * cos(h) / cos(60 - h))
                r = 3 * i - (g + b)

            img[y, x] = r, g, b

    return img


# RGB to CMY
plt.imshow(rgb_to_cmy(mandrill))
# plt.show()

# CMY to RGB
plt.imshow(cmy_to_rgb(rgb_to_cmy(mandrill)))
# plt.show()

# RGB to HSI
# plt.imshow(rgb_to_hsi(mandrill))
# plt.show()

# HSI to RGB
plt.imshow(hsi_to_rgb(rgb_to_hsi(mandrill)))
plt.show()
