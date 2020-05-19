import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

# TODO: Ist nicht gerade schön (Zeitkomplexität), aber funktioniert ^^

# 1.
w_error = imread("mitFehler.png")
wo_error = imread("ohneFehler.png")
error = wo_error - w_error


# 2.
binary = 1 * (error > 0)
plt.imshow(binary, cmap="gray")
# plt.show()


# 3.
# a)
coords = list(map(list, zip(*np.nonzero(binary))))


# b)
# Initialize count of errors and a list of visited pixels.
count = 0
visited = []


# Get the neighbors of a pixel.
def get_neighbors(coord):
    # x, y coordinates of potential neighbors.
    potential_neighbors = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]

    # Initialize reachable neighbor list.
    reachable_neighbors = []

    # Check if potential neighbors are in bounds and not already visited.
    for pn in potential_neighbors:
        new_coord = [coord[0] + pn[0], coord[1] + pn[1]]
        if new_coord[0] in range(binary.shape[0]) and new_coord[1] in range(binary.shape[1]):
            reachable_neighbors += [new_coord]

    return reachable_neighbors


# Main function to count the number of errors in an image using BFS to traverse pixels in an error.
def count_errors(count, coords, visited):
    # Increase count on each recursive call and initialize queue (again).
    count += 1
    queue = [coords[0]]

    # While queue is not empty, get first element, add all neighbors that belong to the error,
    # are not already in queue and are not already visited.
    while queue:
        pixel = queue[0]
        del(queue[0])
        index = coords.index(pixel)
        del(coords[index])
        for n in get_neighbors(pixel):
            if n in coords and n not in queue and [n, count] not in visited:
                queue.append(n)
        visited.append([pixel, count])

    # Exit condition if all coordinates are investigated. Else recursively call with increasing count.
    if coords:
        count_errors(count, coords, visited)
    else:
        print("There is/are " + str(count) + " error(s) in the image!")
    return ""


# c.
print(count_errors(0, coords, visited))
# 8 Fehler werden ermittelt. (Dauert ein bisschen ^^)
