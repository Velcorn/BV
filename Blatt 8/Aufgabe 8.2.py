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
mandrill_gauss = gaussian(mandrill, sigma=4)
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
mandrill_gauss_high = gaussian(mandrill, sigma=20)

# Extracted rows
row_origin = mandrill[150]
row_gauss = mandrill_gauss[150]
row_gauss_high = mandrill_gauss_high[150]

# Extracted rows after applying sobel_v
row_origin_sobelv = sobel_v(mandrill)[150]
row_gauss_sobelv = sobel_v(mandrill_gauss)[150]
row_gauss_high_sobelv = sobel_v(mandrill_gauss_high)[150]

plt.figure("Original")
plt.plot(range(len(row_origin)), row_origin, label="Origin")
plt.plot(row_origin_sobelv, label="SobelV")
plt.legend()
plt.show()

plt.figure("Gauss")
plt.plot(range(len(row_gauss)), row_gauss, label="Gauss")
plt.plot(row_gauss_sobelv, label="SobelV")
plt.legend()
plt.show()

plt.figure("Gauss High Sigma")
plt.plot(range(len(row_gauss_high)), row_gauss_high, label="Gauss High Sigma")
plt.plot(row_gauss_high_sobelv, label="SobelV")
plt.legend()
plt.show()

# Original wird komplett geglättet (flatline), Gauss wird ebenfalls deutlich geglättet (gestauchte Kurven).


# 4.
degrees_origin = np.degrees(np.arctan(np.divide(sobel_v(mandrill), sobel_h(mandrill) + 0.0001)))
degrees_gauss = np.degrees(np.arctan(np.divide(sobel_v(mandrill_gauss), sobel_h(mandrill_gauss) + 0.0001)))

plt.figure("Histogramm Origin")
plt.hist(degrees_origin.flatten(), 9, [0, 9])
plt.show()

plt.figure("Histogramm Gauss")
plt.hist(degrees_gauss.flatten(), 9, [0, 9])
plt.show()

# Bei dem Histogramm des Originalbildes liegen deutlich mehr Werte im ersten Bucket,
# bei dem Histogramm des Gaussbildes ist die Verteilung ausgeglichener.


plt.figure("Histogramm Origin Weight")
plt.hist(degrees_origin.flatten(), 9, [0, 9], weights=degrees_origin.flatten())
plt.show()

plt.figure("Histogramm Gauss Weight")
plt.hist(degrees_gauss.flatten(), 9, [0, 9], weights=degrees_gauss.flatten())
plt.show()

# Mit gesetztem Weightparameter ist die Verteilung bei beiden Histogrammen aufsteigend mit den Buckets.
