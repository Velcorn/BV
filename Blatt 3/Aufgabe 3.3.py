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
coords = list(map(list, zip(*np.nonzero(binary))))
print(coords)

# b)
count = 0
visited = []


# Get the neighboring pixels of a pixel.
def get_neighbors(coord):
    potential_neighbors = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    reachable_neighbors = []
    for pn in potential_neighbors:
        new_coord = [coord[0] + pn[0], coord[1] + pn[1]]
        if new_coord not in visited:
            reachable_neighbors += [new_coord]

    return reachable_neighbors


# Main function to count the number of errors in an image.
def count_errors(count, coords, visited):
    queue = [coords[0]]
    while queue:
        pixel = queue[0]
        print(pixel)
        for n in get_neighbors(pixel):
            print(n)
            if n in coords and n not in visited:
                queue.append(n)
                # print(queue)
        visited.append([pixel, count])
        del(queue[0])
        index = coords.index(pixel)
        del(coords[index])
    count += 1
    print(count)

    count_errors(count, coords, visited)
    return count


print(count_errors(0, coords, visited))
