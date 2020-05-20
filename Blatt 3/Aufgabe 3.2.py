import numpy as np
from skimage.io import ImageCollection, imsave
import matplotlib.pyplot as plt

# 1.
# Load images and calculate an average.
imgs = ImageCollection("bild*.png")
imgs_avg = sum(imgs)/len(imgs)
plt.imshow(imgs_avg, cmap="gray")
# plt.show()
# Nein, 5 Bilder sind definitiv zu wenig.


# 2.
# Stack images and calculate the median.
imgs_stack = np.stack(imgs, axis=0)
imgs_median = np.median(imgs_stack, axis=0)
plt.imshow(imgs_median, cmap="gray")
# plt.show()


# 3.
# Calculate differences between background and foreground.
imgs_diff = []
threshold = 15
for i in range(len(imgs)):
    imgs_diff.append(abs(imgs[i] - imgs_median) > threshold)


# 4.
# Add differences to background.
comb_img = np.copy(imgs_median)
for i in range(len(imgs_diff)):
    comb_img[imgs_diff[i]] = imgs[i][imgs_diff[i]]


# 5.
plt.imshow(comb_img, cmap="gray")
# plt.show()
imsave("comb_img.png", comb_img.astype(np.uint8))
