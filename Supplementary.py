import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('Warning.jpg')

blur = cv.blur(img, (5,5))
Gaussian_blur = cv.GaussianBlur(img, (15,15), 0)
Median_blur = cv.medianBlur(img, 15)
Bilateral_blur = cv.bilateralFilter(img, 100, 500, 400)


text_Original = "Original"
cv.putText(img, text_Original, (20, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (139, 0, 0), 2, cv.LINE_AA)

text_blur = "Averaging"
cv.putText(blur, text_blur, (20, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (139, 0, 0), 2, cv.LINE_AA)

text_Gaussian = "Gaussian"
cv.putText(Gaussian_blur, text_Gaussian, (20, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (139, 0, 0), 2, cv.LINE_AA)

text_Median = "Median"
cv.putText(Median_blur, text_Median, (20, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (139, 0, 0), 2, cv.LINE_AA)

text_Bilateral = "Bilateral"
cv.putText(Bilateral_blur, text_Bilateral, (20, 45), cv.FONT_HERSHEY_SIMPLEX, 1, (139, 0, 0), 2, cv.LINE_AA)



plt.subplot(3, 3, 5), plt.imshow(img[:,:,::-1])
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 1), plt.imshow(blur)
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 3), plt.imshow(Median_blur)
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 7), plt.imshow(Gaussian_blur)
plt.xticks([]), plt.yticks([])

plt.subplot(3, 3, 9), plt.imshow(Bilateral_blur)
plt.xticks([]), plt.yticks([])

plt.show()
