import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

mandrill = imread("mandrill.png")


# Creates a noisy mandrill by making a noise with the provided standard deviation,
# adding it to the original mandrill and clipping the result.
def gaussian_noise(std):
    mean = 0.0
    noisy_img = np.clip((mandrill + np.random.normal(mean, std, mandrill.shape)), 0, 255)
    plt.imshow(noisy_img, cmap="gray")
    plt.show()
    return ""


# Creates a new image in mandrill shape, iterates over every pixel,
# setting it to either white (salt) or black (pepper) or mandrill based on the set probability.
def salt_and_pepper_noise(prob):
    noisy_img = np.zeros(mandrill.shape)
    for i in range(mandrill.shape[0]):
        for j in range(mandrill.shape[1]):
            random = np.random.random()
            if random < prob:
                noisy_img[i][j] = np.random.choice([0, 255])
            else:
                noisy_img[i][j] = mandrill[i][j]
    plt.imshow(noisy_img, cmap="gray")
    plt.show()
    return ""


print(gaussian_noise(100))
print(salt_and_pepper_noise(0.5))
