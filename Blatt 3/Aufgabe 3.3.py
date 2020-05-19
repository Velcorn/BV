import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

w_error = imread("mitFehler.png")
wo_error = imread("ohneFehler.png")


# 1.
error = wo_error - w_error


# 2.
binary = 1 * (error > 0)
plt.imshow(binary, cmap="gray")
# plt.show()


# 3.
# a)
coords = np.argwhere(binary == 1)


# b)
# Get the neighboring pixels of a pixel.
def get_neighbors(coord):
    potential_neighbors = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    reachable_neighbors = []
    for pn in potential_neighbors:
        new_coord = [coord[0] + pn[0], coord[1] + pn[1]]
        if new_coord[0] in range(binary.shape[0]) and new_coord[1] in range(binary.shape[1]):
            reachable_neighbors += [new_coord]

    return reachable_neighbors


# Main function to count the number of errors in an image.
def count_errors(count):
    visited = {}
    queue = [[coords[0], coords[1]]]

    while queue:
        pixel = queue.pop()
        for n in get_neighbors(pixel):
            if [n[0], n[1]] not in visited:
                queue.append([n[0], n[1]])
        visited[x] = pixel

    count_errors(count)
    return count
