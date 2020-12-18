import cv2


img_basic = cv2.imread('hair.jpg', cv2.IMREAD_COLOR)
cv2.imshow('Image Basic', img_basic)
cv2.waitKey(0)
cv2.imwrite('result1.png', img_basic)

cv2.destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Gray', img_gray)
cv2.waitKey(0)
cv2.imwrite('result2.png', img_gray)


#img = cv2.imread('hair.jpg')

'''
if img is None:
    print("Loading the image failed.")
    sys.exit()


cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()


print(type(img))
print(img.shape)
print(img.dtype)


img2 = cv2.imread('hair.jpg',0)
plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
'''