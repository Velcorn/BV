import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import sobel
from skimage.color import rgb2gray


# 1.
opera_rgb = imread("opera.png")
opera_gray = rgb2gray(opera_rgb)
opera_gray_sobel = sobel(opera_gray)
degrees = np.degrees(opera_gray_sobel)
plt.imshow(opera_gray_sobel)
plt.show()

# Es werden quasi alle wichtigen Konturen des Gebäudes gefunden;
# besonders stark sind dabei die Kanten, die im Bild besonders hell sind.
# Es werden allerdings Spiegelungen fälschlicherweise als Kanten erkannt.


# 2.
# Create a zero-filled image in the shape of the gray-scaled image,
# iterate over the rgb image and calculate the Euclidian distance between the rgb pixel and a blue pixel,
# set it in the newly created image and subtract the normalized array from 255, so blue is 255 and yellow is 0.
blueness = np.zeros(opera_gray.shape)
for x in range(blueness.shape[1]):
    for y in range(blueness.shape[0]):
        px = opera_rgb[y, x]
        euclidian_distance = np.linalg.norm(px - np.asarray([0, 0, 255]))
        blueness[y, x] = euclidian_distance
blueness = 255 - (blueness * (255.0 / np.max(blueness))).astype(np.uint8)

# 3.
blueness_sobel = sobel(blueness)
plt.imshow(blueness_sobel)
plt.show()

# Es werden nun hauptsächlich die Kanten zwischen Gebäude und Himmel gefunden.
