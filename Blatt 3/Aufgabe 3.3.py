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
visited = set()


# Get the neighbors of a pixel.
def get_neighbors(coord):
    neighbors = [[0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1]]
    for n in neighbors:
        n[0] += coord[0]
        n[1] += coord[1]
    return neighbors


# Main function to count the number of errors in an image using BFS to traverse pixels in an error.
def count_errors(count, coords, visited):
    # Increase count on each (recursive) call and initialize queue (again).
    count += 1
    queue = [coords[0]]

    # While queue is not empty, get first element and add all neighbors that belong to the error,
    # are not already in queue and are not already visited.
    while queue:
        pixel = queue.pop()
        del(coords[coords.index(pixel)])
        for n in get_neighbors(pixel):
            if n in coords and n not in queue and (n[0], n[1]) not in visited:
                queue.append(n)
        visited.add((pixel[0], pixel[1]))

    # If all coordinates are investigated, return the count. Else recursively call the function.
    if coords:
        return count_errors(count, coords, visited)
    return "There are " + str(count) + " errors in the image!"


# c.
print(count_errors(0, coords, visited))
# 8 Fehler werden ermittelt. (Dauert ein bisschen ^^)
