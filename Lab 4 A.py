import cv2
from matplotlib import pyplot as plt

# Load the image
img = cv2.imread('Stop Sign.jpg')

# Apply Gaussian blur
blur_img = cv2.GaussianBlur(img, (5, 5), 0)

# Sobel edge detection in x direction
sobelx = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5)
filtered_image_x = cv2.convertScaleAbs(sobelx)

# Sobel edge detection in y direction
sobely = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5)
filtered_image_y = cv2.convertScaleAbs(sobely)

# Sobel edge detection in both directions combined
sobelxy = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
filtered_image_xy = cv2.convertScaleAbs(sobelxy)

# Plotting
plt.figure(figsize=(20, 20))

# Original image
plt.subplot(221)
plt.imshow(img[:,:,::-1])
plt.title('Original Image')
plt.axis("off")

plt.subplot(222)
plt.imshow(filtered_image_x, cmap='gray')
plt.title('Sobel X')
plt.axis("off")

plt.subplot(223)
plt.imshow(filtered_image_y, cmap='gray')
plt.title('Sobel Y')
plt.axis("off")

plt.subplot(224)
plt.imshow(filtered_image_xy, cmap='gray')
plt.title('Sobel XY')
plt.axis("off")

plt.show()