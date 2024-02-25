import cv2
from matplotlib import pyplot as plt

# Load the video
video_path = 'Lab.mp4'
cap = cv2.VideoCapture(video_path)

# Check if the video opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Create a Matplotlib figure
fig = plt.figure(figsize=(10, 12))

# Loop through the video frames
while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    # Apply Gaussian blur
    blur_img = cv2.GaussianBlur(frame, (5, 5), 0)

    # Sobel edge detection in both x and y directions with Gaussian Blur
    sobel_xy = cv2.Sobel(src=blur_img, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5)
    filtered_image_xy = cv2.convertScaleAbs(sobel_xy)

    # Canny Edge Detection with Median Blur
    edges = cv2.Canny(frame, 100, 200)
    median_blur = cv2.medianBlur(edges, 5)

    # Laplacian Edge Detection with Bilateral Filter
    laplacian = cv2.Laplacian(blur_img, cv2.CV_64F)
    filtered_image_laplacian = cv2.convertScaleAbs(laplacian)
    bilateral_blur = cv2.bilateralFilter(filtered_image_laplacian, 9, 75, 75)

    # Plotting
    plt.clf()

    plt.subplot(331)
    plt.imshow(frame[:, :, ::-1])
    plt.title('Original Frame')
    plt.axis("off")

    plt.subplot(332)
    plt.imshow(filtered_image_xy, cmap='gray')
    plt.title('Sobel XY with Gaussian Blur')
    plt.axis("off")

    plt.subplot(333)
    plt.imshow(edges)
    plt.title('Canny Edge Detection')
    plt.axis("off")

    plt.subplot(334)
    plt.imshow(median_blur)
    plt.title('Canny Edge Detection with Median Blur')
    plt.axis("off")

    plt.subplot(335)
    plt.imshow(filtered_image_laplacian)
    plt.title('Laplacian Edge Detection')
    plt.axis("off")

    plt.subplot(336)
    plt.imshow(bilateral_blur)
    plt.title('Laplacian Edge Detection with Bilateral Blur')
    plt.axis("off")

    plt.tight_layout()
    plt.pause(0.05)  # Adjust the pause duration if needed

plt.show()

# Release the video capture object
cap.release()
cv2.destroyAllWindows()

