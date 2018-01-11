from skimage.data import camera
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import uniform_filter,gaussian_filter, sobel

             
img = camera()

'''
plt.imshow(img, cmap='gray')
plt.figure()
img2 = uniform_filter(img, 5)
plt.imshow(img2, cmap='gray')
plt.show()
'''
'''
plt.imshow(img, cmap='gray')
plt.figure()
img2 = gaussian_filter(img, 30)
plt.imshow(img2, cmap='gray')
plt.show()
'''
img = img.astype(np.int16)
plt.imshow(img, cmap='gray')
plt.figure()
imgx = np.abs(sobel(img, axis=1))
imgy = np.abs(sobel(img, axis=1))
img=imgx+imgy
plt.imshow(img, cmap='gray')
plt.show()
