import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.filters import gaussian


# 1.
def white_rectangle(x, y, w, h):
    black = np.zeros((256, 256))
    # Make white rectangle with given dimensions around given center.
    black[int(x-w/2):int(x+w/2), int(y-h/2):int(y+h/2)] = 1
    return black


rect5x10 = white_rectangle(128, 128, 10, 5)
plt.figure("Rectangle 5x10")
plt.imshow(rect5x10, cmap="gray")
plt.show()


# 2.
F = np.fft.fft2(rect5x10)
print("Fourier-Transformierte F(0,0):", F[0, 0])

# 50 ist der reelle, 0j der imaginäre Teil.


# 3.
F_shifted = np.fft.fftshift(F)
magnitude = np.abs(F_shifted)
phase = np.angle(F_shifted)
plt.figure("Magnitude Rect 5x10")
plt.imshow(magnitude, cmap="gray")
plt.show()
plt.figure("Phase Rect 5x10")
plt.imshow(phase, cmap="gray")
plt.show()


#


# 4.
rect10x5 = white_rectangle(128, 128, 5, 10)
F = np.fft.fft2(rect10x5)
F_shifted = np.fft.fftshift(F)
magnitude = np.abs(F_shifted)
phase = np.angle(F_shifted)
plt.figure("Magnitude Rect 10x5")
plt.imshow(magnitude, cmap="gray")
plt.show()
plt.figure("Phase Rect 10x5")
plt.imshow(phase, cmap="gray")
plt.show()

rect20x20 = white_rectangle(128, 128, 20, 20)
F = np.fft.fft2(rect20x20)
F_shifted = np.fft.fftshift(F)
magnitude = np.abs(F_shifted)
phase = np.angle(F_shifted)
plt.figure("Magnitude Rect 20x20")
plt.imshow(magnitude, cmap="gray")
plt.show()
plt.figure("Phase Rect 20x20")
plt.imshow(phase, cmap="gray")
plt.show()

#


# 5.
def white_circle(cx, cy, r):
    black = np.zeros((256, 256))
    # Create mgrid.
    x, y = np.mgrid[:256, :256]
    # Make a circle mask.
    mask = np.sqrt((x - cx) ** 2 + (y - cy) ** 2) <= r
    # Apply mask to img.
    black[mask] = 1
    return black


circle = white_circle(128, 128, 10)
F = np.fft.fft2(circle)
F_shifted = np.fft.fftshift(F)
magnitude = np.abs(F_shifted)
phase = np.angle(F_shifted)
plt.figure("Magnitude Circle 10")
plt.imshow(magnitude, cmap="gray")
plt.show()
plt.figure("Phase Circle 10")
plt.imshow(phase, cmap="gray")
plt.show()

circle_gauss = gaussian(circle, sigma=10)
F = np.fft.fft2(circle_gauss)
F_shifted = np.fft.fftshift(F)
magnitude = np.abs(F_shifted)
phase = np.angle(F_shifted)
plt.figure("Magnitude Circle Gauss")
plt.imshow(magnitude, cmap="gray")
plt.show()
plt.figure("Phase Circle Gauss")
plt.imshow(phase, cmap="gray")
plt.show()

#
