import cv2
import matplotlib.pyplot as plt
import time

'''
image = cv2.imread('hair.jpg')

start_time = time.time()
for i in range(0, 100):
    for j in range(0, 100):
        image[i, j] = [255, 255, 255]

start_time = time.time()
image[0:100, 0:100] = [0, 0, 0]
print("--- %s seconds ---" % (time.time() - start_time))

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()
'''
'''
image2 = cv2.imread('hair2.jpg')

roi = image2[200:350, 50:200]
image2[0:150, 0:150] = roi

plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
plt.show()
'''

image3 = cv2.imread('hair2.jpg')
image3[:, :, 2] = 0

plt.imshow(cv2.cvtColor(image3,cv2.COLOR_BGR2RGB))
plt.show()

'''
print(image.shape)
print(image.size)

px = image[100, 100]

print(px)

print(px[2])
'''
