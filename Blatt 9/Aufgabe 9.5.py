import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread


# 1.
mandrill_hBars = imread("mandrill_hBars.png")
F = np.fft.fft2(mandrill_hBars)
F_shifted = np.fft.fftshift(F)
magnitude = np.abs(F_shifted)
phase = np.angle(F_shifted)
'''plt.figure("Magnitude")
plt.imshow(np.log(magnitude), cmap="gray")
plt.show()
plt.figure("Phase")
plt.imshow(phase, cmap="gray")
plt.show()'''

# Die vier Punkte sind: (256,51), (256,154), (256,358), (256, 461).
min_dist = 102
r = min_dist - 10
cx, cy = 256, 256

# Create and use reverse of circular mask on image.
x, y = np.mgrid[:512, :512]
i = np.sqrt((x - cx) ** 2 + (y - cy) ** 2) <= r
F_shifted[~i] = 0

# Transform altered F_shifted back and visualize result.
magnitude = np.abs(F_shifted)
F_shifted_new = magnitude * np.exp(1j * phase)
F_new = np.fft.ifftshift(F_shifted_new)
mandrill_hBars_new = np.real(np.fft.ifft2(F_new))
plt.imshow(mandrill_hBars_new, cmap="gray")
plt.show()
