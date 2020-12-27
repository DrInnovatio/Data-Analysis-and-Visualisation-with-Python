# creating blur effect

import cv2
import matplotlib.pyplot as plt
import numpy as np

# image = cv2.imread('hair.jpg')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()

'''
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16 
'''

# size = 4
# kernel = np.ones((size, size), np.float32) / (size ** 2)
# print(kernel)
#
# dst = cv2.filter2D(image, -1, kernel)
# plt.show(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
# plt.show()

# image = cv2.imread('hair.jpg')
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.show()

'''
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16
1/16 1/16 1/16 1/16 
'''
# Basic Blurring

image = cv2.imread('hair.jpg')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()

dst = cv2.blur(image, (4, 4))
plt.imshow(cv2.cvtColor(dst, cv2.COLOR_BGR2RGB))
plt.show()
