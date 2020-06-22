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

# Das zero-padding sorgt dafür, dass sich die Randbereiche 0 annähern/nach unten gestreckt werden.


# 3.
nine_pad_row = [9] * 3 + row + [9] * 3
conv = np.convolve(nine_pad_row, k)
plt.plot(range(len(conv)), conv, label="nine_pad")

# Das nine-padding sorgt dafür, dass sich die Randbereiche 9 annähern/nach oben gestreckt werden.


# 4.
replicate_pad_row = [row[0]] * 3 + row + [row[-1]] * 3
conv = np.convolve(replicate_pad_row, k)
plt.plot(range(len(conv)), conv, label="replicate_pad")

# Das replicate-padding sorgt dafür, dass sich die Randbereiche dem letzten Listenelement annähern.


# 5.
mirror_pad_row = row[:3][::-1] + row + row[-3:][::-1]
conv = np.convolve(mirror_pad_row, k)
plt.plot(range(len(conv)), conv, label="mirror_pad")

# Das mirror-padding sorgt dafür, dass sich die Randbereiche den letzten 3 Listenelementen
# einschließlich des Randelements annähern.


# 6.
reflection_pad_row = row[1:4][::-1] + row + row[-4:-1][::-1]
conv = np.convolve(reflection_pad_row, k)
plt.plot(range(len(conv)), conv, label="reflection_pad")
plt.legend()
plt.show()

# Das reflection-padding sorgt dafür, dass sich die Randbereiche den letzten 3 Listenelementen
# ausschließlich des Randelements annähern.
