import matplotlib.pyplot as plt
from skimage.io import imread, imsave

# 1.
mandrill = imread("mandrill.png")

# 2.
plt.imshow(mandrill, cmap="gray")
plt.show()

# 3.
nose = mandrill[330:460, 150:330]
plt.imshow(nose, cmap="gray")
plt.show()

# 4.
imsave("nose.png", nose)

# 5.
mandrill_copy = mandrill.copy()
mandrill_copy[0, 0] = 0
plt.imshow(mandrill_copy, cmap="gray")
plt.show()

# Man sieht keinen Unterschied, außer man zoomt auf den Pixel drauf.


# 6.
mandrill_copy_copy = mandrill_copy.copy()
for x in range(50, 85):
    for y in range(145, 365):
        mandrill_copy_copy[x, y] = 0
plt.imshow(mandrill_copy_copy, cmap="gray")
plt.show()

# Man sieht den Unterschied.
