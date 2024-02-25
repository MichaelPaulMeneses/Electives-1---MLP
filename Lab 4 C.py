import cv2
from matplotlib import pyplot as plt

# Second code block with Laplacian edge detection
img = cv2.imread('Stop Sign.jpg')
blur_img = cv2.GaussianBlur(img, (5, 5), 0)
laplacian = cv2.Laplacian(blur_img, 5 , cv2.CV_64F)
filtered_image_laplacian = cv2.convertScaleAbs(laplacian)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(img[:, :, ::-1])
plt.title('Original')
plt.axis("off")

plt.subplot(222)
plt.imshow(filtered_image_laplacian, cmap='gray')
plt.title('Laplacian Edge Detection')
plt.axis("off")

plt.show()