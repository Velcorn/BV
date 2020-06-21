import numpy as np
from skimage.io import imread
from skimage.util import random_noise
import matplotlib.pyplot as plt


# 1.
einstein = np.divide(imread("einstein.png"), 255)
einstein_noise = random_noise(einstein, mode="gaussian", var=0.01)
plt.imshow(einstein_noise, cmap="gray")
plt.show()


# 2.
def mean_abs_diff(img1, img2):
    height, width = img1.shape[:2]
    return np.mean(np.abs(img1 - img2) / (height * width))


diff_einstein = mean_abs_diff(einstein, einstein_noise)
print(diff_einstein)
