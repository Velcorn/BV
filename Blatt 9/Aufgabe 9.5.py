import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


# 1.
mandrill_hBars = imread("mandrill_hBars.png")
F = np.fft.fft2(mandrill_hBars)
F_shifted = np.fft.fftshift(F)
magnitude = np.abs(F_shifted)
phase = np.angle(F_shifted)
plt.figure("Magnitude")
plt.imshow(np.log(magnitude), cmap="gray")
plt.show()
plt.figure("Phase")
plt.imshow(phase, cmap="gray")
plt.show()

# Die vier Punkte sind: (256,51), (256,154), (256,358), (256, 461).
min_dist = 102
r = min_dist - 10
cx, cy = 256, 256

# Create and use reverse of circular mask on image.
x, y = np.mgrid[:512, :512]
i = np.sqrt((x - cx) ** 2 + (y - cy) ** 2) <= r
magnitude_new = np.copy(magnitude)
magnitude_new[~i] = 0
F_shifted_new = magnitude_new * np.exp(1j * phase)
F_new = np.fft.ifftshift(F_shifted_new)
mandrill_hBars_new = np.real(np.fft.ifft2(F_new))
plt.figure("Circle Result")
plt.imshow(mandrill_hBars_new, cmap="gray")
plt.show()

# Die Streifen sind weg, das Bild ist insgesamt etwas heller und etwas unschärfer geworden.


# 2.
def gauss2d(x, y, mx, my, s):
    return 1. / (2. * np.pi * s * s) * np.exp(-((x - mx)**2. / (2. * s**2.) + (y - my)**2. / (2. * s**2.)))


weights = np.zeros(mandrill_hBars.shape).astype(np.float)
for x in range(weights.shape[1]):
    for y in range(weights.shape[0]):
        weights[y, x] = gauss2d(x, y, 256, 256, 30)
magnitude_new = np.multiply(magnitude, weights)
F_shifted_new = magnitude_new * np.exp(1j * phase)
F_new = np.fft.ifftshift(F_shifted_new)
mandrill_hBars_new = np.real(np.fft.ifft2(F_new))
plt.figure("Weights Result")
plt.imshow(mandrill_hBars_new, cmap="gray")
plt.show()

# Die Streifen sind weg, aber das Bild ist heller und deutlich unschärfer.


# 3.
magnitude_new = np.copy(magnitude)
points_x = [51, 154, 358, 461]
for p in points_x:
    magnitude_new[p - 15: p + 15, 256 - 15: 256 + 15] = 0
F_shifted_new = magnitude_new * np.exp(1j * phase)
F_new = np.fft.ifftshift(F_shifted_new)
mandrill_hBars_new = np.real(np.fft.ifft2(F_new))
plt.figure("Square Result")
plt.imshow(mandrill_hBars_new, cmap="gray")
plt.show()

# Das Ergebnis sieht quasi aus wie der normale Mandrill ohne Streifen.
