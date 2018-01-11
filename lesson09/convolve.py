import matplotlib.pyplot as plt
from scipy.ndimage import convolve1d
import numpy as np

arr = np.array([80,90,80,85,100,30,85,89,90,100])
newarr = convolve1d(arr, [1/3]*3)
print(arr.mean())

plt.plot(arr)
plt.plot(newarr)
plt.show()


tem = np.array([10,12,14,15,25,26,24,25,28,13,12,10])
newarr = convolve1d(tem, [1, -1])
print(np.where(np.abs(newarr)>5))
plt.plot(tem)
plt.plot(np.abs(newarr))
plt.show()
