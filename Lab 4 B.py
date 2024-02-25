import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Stop Sign.jpg',0)
edges = cv2.Canny(img, 100, 200)

plt.figure(figsize=(20, 20))

plt.subplot(221)
plt.imshow(img)
plt.title('Original')
plt.axis("off")

plt.subplot(222)
plt.imshow(edges, cmap='gray')
plt.title('Canny Edge Detection')
plt.axis("off")

plt.show()