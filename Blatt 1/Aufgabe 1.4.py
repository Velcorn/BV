import numpy as np
from skimage.io import imread, imsave
import matplotlib.pyplot as plt

# 1.a
mandrill = imread("mandrill.png")

# 1.b
mandrill_flipud = np.flipud(mandrill)
plt.imshow(mandrill_flipud, cmap="gray")
plt.show()

# 1.c
mandrill_fliplr = np.fliplr(mandrill)
plt.imshow(mandrill_fliplr, cmap="gray")
plt.show()

# 1.d
mandrill_flipudlr = np.fliplr(mandrill_flipud)
plt.imshow(mandrill_flipudlr, cmap="gray")
plt.show()

# 1.e
mandrill_left = np.concatenate((mandrill, mandrill_flipud), axis=0)
mandrill_right = np.concatenate((mandrill_fliplr, mandrill_flipudlr), axis=0)
mandrill_art = np.concatenate((mandrill_left, mandrill_right), axis=1)
plt.imshow(mandrill_art, cmap="gray")
plt.show()

# 2.
mandrill_negative = np.negative(mandrill)
plt.imshow(mandrill_negative, cmap="gray")
plt.show()

# 3.
nose = mandrill[330:460, 150:330]
nose[0, 0] = 0
plt.imshow(mandrill, cmap="gray")
plt.show()
# Die Änderung wird auch im Original durchgeführt.

# 4.a
mask = np.zeros([512, 512])

# 4.b
for x in range(330, 460):
    for y in range(150, 330):
        mask[x, y] = 1

# 4.c
masked = mandrill * mask
plt.imshow(masked, cmap="gray")
plt.show()
