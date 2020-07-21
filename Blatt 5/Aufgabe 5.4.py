import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2hsv, hsv2rgb

# 1.
mandrill = imread("mandrillFarbe.png")
plt.imshow(mandrill)
plt.show()


# 2.
mandrill_inverted = 255 - mandrill
plt.imshow(mandrill_inverted)
plt.show()


# 3.
r = mandrill[:, :, 0]
g = mandrill[:, :, 1]
b = mandrill[:, :, 2]
plt.imshow(r, cmap="gray")
plt.show()
plt.imshow(g, cmap="gray")
plt.show()
plt.imshow(b, cmap="gray")
plt.show()
# Helligkeitswerte sind die Werte der Pixel der eigentlichen Kanäle (RGB)?!


# 4.
mandrill_bgr = np.dstack((b, g, r))
plt.imshow(mandrill_bgr)
plt.show()
# Rote und blaue Farbtöne werden getauscht, duh :P


# 5.
mandrill_gray = np.zeros((mandrill.shape[0], mandrill.shape[1]))
for x in range(mandrill.shape[1]-1):
    for y in range(mandrill.shape[0]-1):
        px = mandrill[y, x]
        r = int(px[0])
        g = int(px[1])
        b = int(px[2])
        gray = round((r + g + b) / 3)
        mandrill_gray[y, x] = gray
plt.imshow(mandrill_gray, cmap="gray")
plt.show()


# 6.
mandrill_sat1 = rgb2hsv(mandrill)
mandrill_sat1[:, :, 1] = 1
mandrill_sat0 = rgb2hsv(mandrill)
mandrill_sat0[:, :, 1] = 0
plt.imshow(hsv2rgb(mandrill_sat1))
plt.show()
plt.imshow(hsv2rgb(mandrill_sat0))
plt.show()

# Bei einer erhöhten Sättigung wirken die Farben intensiver,
# bei einer erniedrigten Sättigung wirken die Farben blasser oder gar grau (0)


# 7.
mandrill_60 = rgb2hsv(mandrill)
mandrill_60[:, :, 0] += 1/6
mandrill_120 = rgb2hsv(mandrill)
mandrill_120[:, :, 0] += 1/3
mandrill_240 = rgb2hsv(mandrill)
mandrill_240[:, :, 0] += 2/3
plt.imshow(hsv2rgb(mandrill_60))
plt.show()
plt.imshow(hsv2rgb(mandrill_120))
plt.show()
plt.imshow(hsv2rgb(mandrill_240))
plt.show()

# Drehen der Farbtöne verändert die Farbtöne des Bildes im HSI-Farbkreis?!
