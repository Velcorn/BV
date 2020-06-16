import numpy as np
from skimage.io import imread
import time

mandrill = imread("mandrill.png")


# 1.
def var1(img):
    start = time.time()
    width, height = img.shape[:2]

    mu = 0
    for x in range(width):
        for y in range(height):
            px = img[y, x]
            mu += px
    mu /= (width * height)

    var = 0
    for x in range(width):
        for y in range(height):
            px = img[y, x]
            var += (px - mu) ** 2
    var /= (width * height)

    end = time.time()
    diff = end - start

    return [var, diff]


print("Var1 result:", var1(mandrill)[0])


# 2.
def var2(img):
    start = time.time()

    width, height = img.shape[:2]

    mu = 0
    var = 0
    for x in range(width):
        for y in range(height):
            px = img[y, x]
            mu += px
            var += px ** 2 / (width * height)
    mu /= (width * height)
    var -= mu ** 2

    end = time.time()
    diff = end - start

    return [var, diff]


print("Var2 result:", var2(mandrill)[0])

# 3.
var1_time = 0
for i in range(10):
    var1_time += var1(mandrill)[1]

var2_time = 0
for i in range(10):
    var2_time += var2(mandrill)[1]

print("Var1 time:", var1_time)
print("Var2 time:", var2_time)

# Die Ergebnisse variieren leicht aufgrund von Rundungen bei unterschiedlichen Rechnungen -
# bei Variante 1 wird in jedem Schleifendurchlauf subtrahiert und am Ende dividiert, bei Variante 2 ist es andersrum.
# Variante 2 sollte schneller sein, da nur 1 Durchlauf benötigt wird.
