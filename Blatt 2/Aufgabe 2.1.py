import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread

# Reads in Red and NIR band as float, calculates the NDVI from the formula and shows the image.
Red = imread("band3.png").astype(float)
NIR = imread("band4.png").astype(float)
NDVI = np.divide(np.subtract(NIR, Red), np.add(NIR, Red))
plt.imshow(NDVI, cmap="gray")
plt.show()

# Ein NDVI von ~0,5 an den grünen Punkten deutet auf eine Vegetationsbedeckung mit grünen Pflanzen hin.
# Die Abstufungen der Grautöne lassen uns auf die Dichte der Vegatation schließen.
