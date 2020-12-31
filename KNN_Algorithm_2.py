import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('digits.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cells = [np.hsplit(row, 100) for row in np.vsplit(gray, 50)]
x = np.array(cells)
print(x.shape)

train = x[:, :].reshape(-1, 400).astype(np.float32)

k = np.arange(10)
train_labels = np.repeat(k, 500)[:, np.newaxis]

print(train_labels.shape)
np.savez("trained.npz", train=train, train_labels=train_labels)

plt.imshow(cv2.cvtColor(x[0, 0], cv2.COLOR_BGR2RGB))

cv2.imwrite('test_0.png', x[0, 0])
cv2.imwrite('test_1.png', x[5, 0])
cv2.imwrite('test_2.png', x[10, 0])
cv2.imwrite('test_3.png', x[15, 0])
cv2.imwrite('test_4.png', x[20, 0])
cv2.imwrite('test_5.png', x[25, 0])
cv2.imwrite('test_6.png', x[30, 0])
cv2.imwrite('test_7.png', x[35, 0])
cv2.imwrite('test_8.png', x[40, 0])
cv2.imwrite('test_9.png', x[45, 0])

