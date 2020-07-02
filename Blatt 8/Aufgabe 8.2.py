import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import gaussian, sobel, sobel_h, sobel_v


# 1.
mandrill = imread("mandrill.png")
mandrill_sobel = sobel(mandrill)
plt.imshow(mandrill_sobel)
plt.show()

threshold = 0.15
mandrill_sobel[mandrill_sobel > threshold] = 1
mandrill_sobel[mandrill_sobel < threshold] = 0
plt.imshow(mandrill_sobel)
plt.show()

# Die wichtigsten Kanten wurden gefunden,
# es werden allerdings auch das Fell um den Kopf herum sowie die Barthaare erkannt.


# 2.
mandrill_gauss = gaussian(mandrill, sigma=4, preserve_range=True).astype(np.uint8)
mandrill_gauss_sobel = sobel(mandrill_gauss)

threshold = 0.022
mandrill_gauss_sobel[mandrill_gauss_sobel > threshold] = 1
mandrill_gauss_sobel[mandrill_gauss_sobel < threshold] = 0
plt.imshow(mandrill_gauss_sobel)
plt.show()

# Das Fell um den Kopf herum wird durch das Weichzeichnen deutlich weniger erkannt, sondern nur noch stärkere Kanten.
# Je höher Sigma gesetzt wird, desto niedriger muss der Threshold gesetzt werden,
# da durch das Weichzeichnen die Werte schneller verschwimmen.


# 3.
mandrill_gauss_high = gaussian(mandrill, sigma=20, preserve_range=True)

# Extracted rows
row_origin = mandrill[150]
row_gauss = mandrill_gauss[150]
row_gauss_high = mandrill_gauss_high[150]

# Extracted rows after applying sobel_v
row_origin_sobelv = sobel_v(mandrill)[150]
row_gauss_sobelv = sobel_v(mandrill_gauss)[150]
row_gauss_high_sobelv = sobel_v(mandrill_gauss_high)[150]

plt.figure("Original")
plt.plot(range(len(row_origin)), row_origin / 255, label="Origin")
plt.plot(row_origin_sobelv, label="Origin SobelV")
plt.legend()
plt.show()

plt.figure("Gauss")
plt.plot(range(len(row_gauss)), row_gauss / 255, label="Gauss")
plt.plot(row_gauss_sobelv, label="Gauss SobelV")
plt.legend()
plt.show()

plt.figure("Gauss High Sigma")
plt.plot(range(len(row_gauss_high)), row_gauss_high / 255, label="Gauss High Sigma")
plt.plot(row_gauss_high_sobelv, label="Gauss High Sigma SobelV")
plt.legend()
plt.show()

# Beim Originalbilde schwankt die Kurve sehr stark, beim Gaussbild ist sie etwas glatter,
# beim Gaussbild mit einem hohen Sigmawert ist sie sehr glatt -
# hier schwankt die Kurve des Ergebnisses der SobelV-Operation mehr.


# 4.
degrees_origin = np.degrees(np.arctan(np.divide(sobel_v(mandrill), sobel_h(mandrill) + 0.0001)))
degrees_gauss = np.degrees(np.arctan(np.divide(sobel_v(mandrill_gauss), sobel_h(mandrill_gauss) + 0.0001)))

plt.figure("Histogramm Origin")
plt.hist(degrees_origin.flatten(), 9, [-90, 90], density=True)
plt.show()

plt.figure("Histogramm Gauss")
plt.hist(degrees_gauss.flatten(), 9, [-90, 90], density=True)
plt.show()

# Bei dem Histogramm des Originalbildes ist die Verteilung relativ symmetrisch um die 0° gespiegelt.
# Bei dem Histogramm des Gaussfilters ist die Verteilung bei -90°, 0° und 90° höher als beim Rest.

plt.figure("Histogramm Origin Weight")
plt.hist(degrees_origin.flatten(), 9, [-90, 90], density=True, weights=mandrill_sobel.flatten())
plt.show()

counts, bins = np.histogram(degrees_gauss, 9, [-90, 90])
plt.figure("Histogramm Gauss Weight")
plt.hist(degrees_gauss.flatten(), 9, [-90, 90], density=True, weights=mandrill_gauss_sobel.flatten())
plt.show()

# Mit gesetztem Weightparameter verdeutlichen sich die Diskrepanzen.
