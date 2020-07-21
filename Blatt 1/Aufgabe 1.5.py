import time
import numpy as np
from skimage.io import imread

mandrill = "mandrill.png"


# 1.
def for_loops(image):
    start = time.time()
    img = imread(image)
    a = []
    for part in img:
        for pixel in part:
            if pixel in range(99, 201):
                a.append(True)
            a.append(False)
    end = time.time()
    return end-start


# 2.
def broadcasting(image):
    start = time.time()
    img = imread(image)
    np.logical_and(img > 98, img < 201)
    end = time.time()
    return end-start


# 3.
for_loops_time = for_loops(mandrill) * 100
broadcasting_time = broadcasting(mandrill) * 100
print(f"100 calls with for loops: {for_loops_time}")
print(f"100 calls with broadcasting: {broadcasting_time}")
print(f"Broadcasting is {round(for_loops_time / broadcasting_time)} times faster.")
