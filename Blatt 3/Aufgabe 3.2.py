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
img_stack = np.stack(imgs, axis=0)
img_median = np.median(img_stack, axis=0)
plt.imshow(img_median, cmap="gray")
# plt.show()


# 3.
# Calculate differences between background and foreground
imgs_diff = []
for i in range(len(imgs)):
    imgs_diff.append((imgs[i] - img_median))


# 4.
# Add difference to background.
comb_img = img_median + sum(imgs_diff)
plt.imshow(comb_img, cmap="gray")
plt.show()


# 5.
imsave("comb_img.png", comb_img)
