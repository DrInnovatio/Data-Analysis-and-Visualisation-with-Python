import cv2
import matplotlib as plt
import numpy as np


image_1 = cv2.imread('hair.jpg')
image_2 = cv2.imread('hair2.jpg')

result = cv2.add(image_1, image_2)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()

result_2 = image_1 + image_2
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.show()