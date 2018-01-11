from scipy.misc import imread, imsave
import matplotlib.pyplot as plt
import numpy as np


img = imread('img.png')
'''
w,h = img.shape[:2]
img[:w//2,:h//2,0] = 255

plt.imshow(img)
plt.show()

plt.imshow(img[::2,:,:])
plt.show()

plt.imshow(img[:,:,::-1])
plt.show()

plt.imshow(255-img)
plt.show()
'''
img = imread('lena.png', True)
img = (img>128)*255


imsave('lena2.png', img.astype(np.uint8))
