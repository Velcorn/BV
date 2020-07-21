import time
from skimage.io import imread

mandrill = imread("mandrill.png")


# 1.
def var1(img):
    height, width = img.shape[:2]

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

    return var


print(f"Var1 result: {var1(mandrill)}")


# 2.
def var2(img):
    height, width = img.shape[:2]

    mu = 0
    var = 0
    for x in range(width):
        for y in range(height):
            px = img[y, x]
            mu += px
            var += px ** 2 / (width * height)
    mu /= (width * height)
    var -= mu ** 2

    return var


print(f"Var2 result: {var2(mandrill)}")

# 3.
start = time.time()
for i in range(10):
    var1(mandrill)
end = time.time()
var1_time = end - start
print(f"Var1 time: {var1_time}")

start = time.time()
for i in range(10):
    var2(mandrill)
end = time.time()
var2_time = end - start
print(f"Var2 time: {var2_time}")

# Die Ergebnisse variieren leicht aufgrund von Rundungen bei unterschiedlichen Rechnungen.
# Variante 2 sollte schneller sein, da nur 1 Durchlauf benötigt wird.
