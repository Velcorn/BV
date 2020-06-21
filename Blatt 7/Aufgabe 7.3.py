import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import convolve
from skimage.io import imread
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
min_diff_gauss_box = np.inf
best_gauss_box = 0
n_vals = [3, 5, 7, 9, 11]
for n in n_vals:
    kernel = (1 / (n * n)) * np.ones((n, n))
    einstein_gauss_box = convolve(einstein_gauss, kernel)
    diff = mean_abs_diff(einstein_gauss, einstein_gauss_box)
    if diff < min_diff_gauss_box:
        min_diff_gauss_box = diff
        best_gauss_box = einstein_gauss_box

print("Min mean abs diff gauss/box:", min_diff_gauss_box)
plt.imshow(best_gauss_box, cmap="gray")
plt.show()

# 4.
min_diff_gauss_gauss = np.inf
best_gauss_gauss = 0
var = 0.1
while var < 2:
    einstein_gauss_gauss = random_noise(einstein, mode="gaussian", var=0.01)
    diff = mean_abs_diff(einstein, einstein_gauss_gauss)
    if diff < min_diff_gauss_gauss:
        min_diff_gauss_gauss = diff
        best_gauss_gauss = einstein_gauss_gauss
    var += 0.1

print("Min mean abs diff gauss/gauss:", min_diff_gauss_gauss)
plt.imshow(best_gauss_gauss, cmap="gray")
plt.show()


# 5.
einstein_snp = random_noise(einstein, mode="s&p", amount=0.1)
min_diff_snp_gauss = np.inf
best_snp_gauss = 0
var = 0.1
while var < 2:
    einstein_snp_gauss = random_noise(einstein, mode="gaussian", var=0.01)
    diff = mean_abs_diff(einstein, einstein_snp_gauss)
    if diff < min_diff_snp_gauss:
        min_diff_snp_gauss = diff
        best_snp_gauss = einstein_snp_gauss
    var += 0.1

print("Min mean abs diff snp/gauss:", min_diff_snp_gauss)
plt.imshow(best_snp_gauss, cmap="gray")
plt.show()


# 6.
def median_filter(img):
    height, width = img.shape[:2]
    neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

    for x in range(width):
        for y in range(height):
            n_values = [img[y, x] + n for n in neighbors]
            img[y, x] = np.median(n_values)

    return img


einstein_snp_median_filter = median_filter(einstein_snp)
diff_snp_median_filter = mean_abs_diff(einstein, einstein_snp_median_filter)
print("Mean abs diff snp/median_filter:", diff_snp_median_filter)
plt.imshow(einstein_snp_median_filter, cmap="gray")
plt.show()
