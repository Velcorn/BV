import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

mandrill = imread("mandrill.png")


# Creates a noisy mandrill by making a noise with the provided standard deviation,
# adding it to the original mandrill and clipping the result.
def gaussian_noise(img, std):
    mean = 0.0
    noisy_img = np.clip((img + np.random.normal(mean, std, img.shape)), 0, 255)
    return noisy_img


plt.imshow(gaussian_noise(mandrill, 100), cmap="gray")
plt.show()


# Creates a new image in mandrill shape, iterates over every pixel,
# setting it to either white (salt) or black (pepper) or mandrill based on the set probability.
def salt_and_pepper_noise(img, prob):
    noisy_img = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            random = np.random.random()
            if random < prob:
                noisy_img[i][j] = np.random.choice([0, 255])
            else:
                noisy_img[i][j] = img[i][j]
    return noisy_img


plt.imshow(salt_and_pepper_noise(mandrill, 0.5), cmap="gray")
plt.show()
