import cv2
img = cv2.imread("Mei Mei.jpg", cv2.IMREAD_COLOR)

cv2.imshow("Mei Mei.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()