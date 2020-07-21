import numpy as np
from skimage.io import ImageCollection
from skimage.color import rgb2gray, rgb2hsv

imgs = ImageCollection("image*.jpg")
msks = ImageCollection("image*.png")

# 1.
# Flowers in grayscale.
fg11 = rgb2gray(imgs[0])
fg12 = rgb2gray(imgs[1])
fg21 = rgb2gray(imgs[2])
fg22 = rgb2gray(imgs[3])

# Masks.
m11 = msks[0]
m12 = msks[1]
m21 = msks[2]
m22 = msks[3]

# Mean grayscale value.
gmean11 = np.ma.mean(np.ma.array(fg11, mask=1 - m11))
gmean12 = np.ma.mean(np.ma.array(fg12, mask=1 - m12))
gmean21 = np.ma.mean(np.ma.array(fg21, mask=1 - m21))
gmean22 = np.ma.mean(np.ma.array(fg22, mask=1 - m22))


# 2.
fc11 = rgb2hsv(imgs[0])[:, :, 0]
fc12 = rgb2hsv(imgs[1])[:, :, 0]
fc21 = rgb2hsv(imgs[2])[:, :, 0]
fc22 = rgb2hsv(imgs[3])[:, :, 0]

# Mean color value.
cmean11 = np.ma.mean(np.ma.array(fc11, mask=1 - m11))
cmean12 = np.ma.mean(np.ma.array(fc12, mask=1 - m12))
cmean21 = np.ma.mean(np.ma.array(fc21, mask=1 - m21))
cmean22 = np.ma.mean(np.ma.array(fc22, mask=1 - m22))


# 3.
print(f"Flower 1 gray means: {round(gmean11, 4)}, {round(gmean12, 4)}")
print(f"Flower 2 gray means: {round(gmean21, 4)}, {round(gmean22, 4)}")
print(f"Average gray mean difference: {round(abs(((gmean11 + gmean12) - (gmean21 + gmean22)) / 2), 4)}\n")
print(f"Flower 1 color means: {round(cmean11, 4)}, {round(cmean12, 4)}")
print(f"Flower 2 color means: {round(cmean21, 4)}, {round(cmean22, 4)}")
print(f"Average color mean difference: {round(abs(((cmean11 + cmean12) - (cmean21 + cmean22)) / 2), 4)}")

# Tendenziell eignen sich beide mittleren Werte ziemlich gut zum Unterscheiden der beiden Blumenarten.
# Allerdings scheint der mittlere Farbton etwas besser geeignet, da er jeweils bei beiden Bildern einer
# Blumenart sehr ähnlich ist, wobei der mittlere Grauwert bei der zweiten Blumenart etwas unterschiedlicher ist.
# Außerdem ist der Unterschied der mittleren Farbtöne deutlich höher zwischen den beiden Blumenarten.
