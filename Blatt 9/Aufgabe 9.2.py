import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import gaussian, laplace, sobel
from skimage.util import random_noise


# 1.
mandrill = imread("mandrill.png")
mandrill_gf = gaussian(mandrill, sigma=3)
mandrill_gn = random_noise(mandrill, mode="gaussian", var=0.01)
plt.figure("Variante 1")
plt.imshow(mandrill, cmap="gray")
plt.show()
plt.figure("Variante 2")
plt.imshow(mandrill_gf, cmap="gray")
plt.show()
plt.figure("Variante 3")
plt.imshow(mandrill_gn, cmap="gray")
plt.show()


# 2.
mandrill_l = laplace(mandrill)
mandrill_gfl = laplace(mandrill_gf)
mandrill_gnl = laplace(mandrill_gn)
plt.figure("Variante 1 Laplace")
plt.imshow(mandrill_l, cmap="gray")
plt.show()
plt.figure("Variante 2 Laplace")
plt.imshow(mandrill_gfl, cmap="gray")
plt.show()
plt.figure("Variante 3 Laplace")
plt.imshow(mandrill_gnl, cmap="gray")
plt.show()


# 3.
mandrill_gngf = gaussian(mandrill_gn, sigma=2)
mandrill_gngfl = laplace(mandrill_gngf)
plt.figure("Variante 3 Gauss Laplace")
plt.imshow(mandrill_gngfl, cmap="gray")
plt.show()


# 4.
def extract_edges(img, threshold):
    edges = np.zeros(img.shape)
    height, width = img.shape[:2]
    for x in range(1, width - 1):
        for y in range(1, height - 1):
            # Get neighbors, top, bottom, top right, bottom left, top left, bottom left.
            nt = img[y - 1, x]
            nb = img[y + 1, x]
            ntr = img[y - 1, x + 1]
            nbl = img[y + 1, x - 1]
            ntl = img[y - 1, x - 1]
            nbr = img[y + 1, x + 1]

            # Check if opposing neighbors have different sign and if their difference is above threshold
            th = threshold
            if nt * nb < 0 and abs(nt - nb) > th or \
                    ntr * nbl < 0 and abs(ntr - nbl) > th or ntl * nbr < 0 and abs(ntl - nbr) > th:
                edges[y, x] = 1
            else:
                edges[y, x] = 0
    return edges


mandrill_gfle = extract_edges(mandrill_gfl, 0.007)
plt.figure("Variante 2 Laplace Edges Sigma 3")
plt.imshow(mandrill_gfle, cmap="gray")
plt.show()

mandrill_gfle = extract_edges(laplace(gaussian(mandrill, sigma=6)), 0.001)
plt.figure("Variante 2 Laplace Edges Sigma 6")
plt.imshow(mandrill_gfle, cmap="gray")
plt.show()

# Sigma 3 und Threshold 0.007 liefern halbwegs vernünftige Ergebnisse.
# Nach Ausprobieren liefern Sigma 6 und Threshold 0.01 einen guten Kompromiss
# zwischen wichtigen und unwichtigen Kanten.


# 5.
mandrill_gfs = sobel(mandrill_gf)
threshold = 0.033
mandrill_gfs[mandrill_gfs > threshold] = 1
mandrill_gfs[mandrill_gfs < threshold] = 0
plt.figure("Variante 2 Sobel Sigma 3")
plt.imshow(mandrill_gfs)
plt.show()

mandrill_gfs = sobel(gaussian(mandrill, sigma=6))
threshold = 0.015
mandrill_gfs[mandrill_gfs > threshold] = 1
mandrill_gfs[mandrill_gfs < threshold] = 0
plt.figure("Variante 2 Sobel Sigma 6")
plt.imshow(mandrill_gfs)
plt.show()

# Die mit dem Laplace-Filter gefundenen Kanten sind schmaler und wirken genauer,
# allerdings sind die Unterschiede natürlich auch stark vom gewählten Sigma und Threshold abhängig.
