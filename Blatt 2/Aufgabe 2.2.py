import numpy as np
import math
import matplotlib.pyplot as plt

# TODO: Ich weiß zwar nicht, ob die Funktion jetzt wenigstens halbwegs das tut, was die Aufgabe haben will, aber hier.

img = []
row = []
mu, sigma = 0.0, 1.0

# Creates a row with 51 elements using the Gaussian function.
x = -5
for i in range(51):
    f = round((1 / math.sqrt(2 * math.pi * sigma ** 2)) ** ((-(x - mu) ** 2) / 2 * sigma ** 2))
    row.append(f)
    if x < 5:
        x += 10 / 51
    else:
        x = -5

# Creates an image with 100 of the previously created rows.
for i in range(100):
    img.append(row)

plt.imshow(np.clip(img, 0, 255), cmap="gray")
plt.show()

# Eine Änderung von mu bewirkt eine Verschiebung auf der x-Achse,
# eine Änderung von sigma bewirkt eine Stauchung.
