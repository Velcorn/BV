import numpy as np
from skimage.io import imread
import matplotlib.pyplot as plt

# 1.
bild1 = imread("bild1.png")
bild2 = imread("bild2.png")

hist1 = np.histogram(bild1.flatten(), 256, [0, 256], density=True)
hist2 = np.histogram(bild2.flatten(), 256, [0, 256], density=True)

'''plt.figure("Histogramm 1")
plt.hist(bild1.flatten(), 256, [0, 256], density=True)
plt.show()
plt.figure("Histogramm 2")
plt.hist(bild2.flatten(), 256, [0, 256], density=True)
plt.show()'''


# 2.
def equalize_hist(img):
    # Create normalized histogram from img.
    hist, bins = np.histogram(img.flatten(), 256, [0, 256], density=True)

    # Calculate T(rk) according to the formula.
    t = []
    val = 0
    for x in range(len(hist)):
        val += 255 * hist[x]
        t.append(int(val))
    eq_hist = np.asarray(t)

    # Apply equalized histogram to image.
    he_img = np.reshape(eq_hist[img.flatten()], img.shape)

    return eq_hist, he_img


'''plt.figure("Equalized Histogramm 1")
plt.hist(equalize_hist(bild1)[0], bins=256, range=(0, 256), density=True)
plt.show()
plt.figure("Histogram Equalization Bild 1")
plt.imshow(equalize_hist(bild1)[1], cmap="gray", vmin=0, vmax=255)
plt.show()

plt.figure("Equalized Histogramm 2")
plt.hist(equalize_hist(bild2)[0], bins=256, range=(0, 256), density=True)
plt.show()
plt.figure("Histogram Equalization Bild 2")
plt.imshow(equalize_hist(bild2)[1], cmap="gray", vmin=0, vmax=255)
plt.show()'''


# 3.
plt.figure("Transformationsfunktion 1")
plt.plot(range(len(equalize_hist(bild1)[0])), equalize_hist(bild1)[0])
plt.show()

plt.figure("Transformationsfunktion 2")
plt.plot(range(len(equalize_hist(bild2)[0])), equalize_hist(bild2)[0])
plt.show()
