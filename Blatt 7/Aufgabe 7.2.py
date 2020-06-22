import numpy as np
import matplotlib.pyplot as plt


row = [5] * 10
k05 = [0.1] * 5
conv = np.convolve(row, k05)
plt.plot(range(len(conv)), conv, label="Sum 0.5")

k1 = [1] * 5
k1 = [x / len(k1) for x in k1]
conv = np.convolve(row, k1)
plt.plot(range(len(conv)), conv, label="Sum 1")

k2 = [0.4] * 5
conv = np.convolve(row, k2)
plt.plot(range(len(conv)), conv, label="Sum 2")
plt.legend()
plt.show()
