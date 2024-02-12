import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('monk.jpg')

blur = cv.blur(img, (5,5))
blur = cv.GaussianBlur(img, (5,5), 200)
blur = cv.medianBlur(img, 25)
blur = cv.bilateralFilter(img, 12, 85, 85)



plt.subplot(3, 3, 5), plt.imshow(img), plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 1), plt.imshow(blur), plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 3), plt.imshow(blur), plt.title('Median')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 7), plt.imshow(blur), plt.title('Gaussian')
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 9), plt.imshow(blur), plt.title('Bilateral')
plt.xticks([]), plt.yticks([])

plt.show()