import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import convolve
from skimage.io import imread
from skimage.filters import gaussian
from skimage.util import random_noise


# 1.
einstein = np.divide(imread("einstein.png"), 255)
einstein_gauss = random_noise(einstein, mode="gaussian", var=0.01)
plt.imshow(einstein_gauss, cmap="gray")
plt.show()


# 2.
def mean_abs_diff(img1, img2):
    return np.mean(np.abs(img1 - img2))


diff_gauss = mean_abs_diff(einstein, einstein_gauss)
print("Mean abs diff original/gauss:", diff_gauss)


# 3.
min_diff = np.inf
best = 0
n_vals = [3, 5, 7, 9, 11]
for n in n_vals:
    k = (1 / (n * n)) * np.ones((n, n))
    einstein_gauss_box = convolve(einstein_gauss, k)
    diff = mean_abs_diff(einstein, einstein_gauss_box)
    if diff < min_diff:
        min_diff = diff
        best = einstein_gauss_box

print("Min mean abs diff original/gauss/box:", min_diff)
plt.imshow(best, cmap="gray")
plt.show()

# 4.
min_diff = np.inf
best = 0
var = 0.1
while var < 2:
    einstein_gauss_gauss = gaussian(einstein_gauss, sigma=var)
    diff = mean_abs_diff(einstein, einstein_gauss_gauss)
    if diff < min_diff:
        min_diff = diff
        best = einstein_gauss_gauss
    var += 0.1

print("Min mean abs diff original/gauss/gauss:", min_diff)
plt.imshow(best, cmap="gray")
plt.show()

# Nein, man erkennt kaum bis keinen Unterschied zwischen Gauss- und Box-Filter.


# 5.
einstein_snp = random_noise(einstein, mode="s&p", amount=0.1)
min_diff = np.inf
best = 0
var = 0.1
while var < 2:
    einstein_snp_gauss = gaussian(einstein_snp, sigma=var)
    diff = mean_abs_diff(einstein, einstein_snp_gauss)
    if diff < min_diff:
        min_diff = diff
        best = einstein_snp_gauss
    var += 0.1

print("Min mean abs diff original/snp/gauss:", min_diff)
plt.imshow(best, cmap="gray")
plt.show()


# 6.
def median_filter(img):
    height, width = img.shape[:2]
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]

    for x in range(width):
        for y in range(height):
            n_values = [img[y, x] + n for n in neighbors]
            img[y, x] = np.median(n_values)

    return img


einstein_snp_median = median_filter(einstein_snp)
diff_snp_median = mean_abs_diff(einstein, einstein_snp_median)
print("Mean abs diff original/snp/median:", diff_snp_median)
plt.imshow(einstein_snp_median, cmap="gray")
plt.show()
