import numpy as np
import matplotlib.pyplot as plt


# 1.
row = [1, 2, 5, 9, 8, 3, 6, 7, 9, 9]
plt.plot(range(len(row)), row, label="row")


# 2.
k = [1, 1, 1, 1, 1]
k = [x / len(k) for x in k]
zero_pad_row = [0] * 3 + row + [0] * 3
conv = np.convolve(zero_pad_row, k)
plt.plot(range(len(conv)), conv, label="zero_pad")


# 3.
nine_pad_row = [9] * 3 + row + [9] * 3
conv = np.convolve(nine_pad_row, k)
plt.plot(range(len(conv)), conv, label="nine_pad")


# 4.
mirror_pad_row = row[:3][::-1] + row + row[-3:][::-1]
conv = np.convolve(mirror_pad_row, k)
plt.plot(range(len(conv)), conv, label="mirror_pad")


# 5.
reflection_pad_row = row[1:4][::-1] + row + row[-4:-1][::-1]
conv = np.convolve(reflection_pad_row, k)
plt.plot(range(len(conv)), conv, label="reflection_pad")
plt.legend()
plt.show()
