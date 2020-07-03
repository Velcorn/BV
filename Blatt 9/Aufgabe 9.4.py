import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import gaussian


# 1.
def white_rectangle(x, y, w, h):
    black = np.zeros((256, 256))
    # Make white rectangle with given dimensions around given center.
    black[int(x-w/2):int(x+w/2), int(y-h/2):int(y+h/2)] = 1
    return black


rectangle = white_rectangle(128, 128, 10, 5)
plt.imshow(rectangle, cmap="gray")
plt.show()


# 2.


# 3.


# 4.
reverse = white_rectangle(128, 128, 5, 10)
rec2020 = white_rectangle(128, 128, 20, 20)


# 5.
def white_circle(x, y, r):
    black = np.zeros((256, 256))
    # Create mgrid of radius.
    xx, yy = np.mgrid[-r:r, -r:r]
    # Use circle forumale to calculate index.
    i = xx ** 2 + yy ** 2 <= r ** 2
    # Make white circle with given radius around given center.
    black[y-r:y+r, x-r:x+r][i] = 1
    return black


circle = white_circle(128, 128, 10)
plt.imshow(circle, cmap="gray")
plt.show()
