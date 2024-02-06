import cv2
path = r'monk.jpg'

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

cv2.imshow('monk.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()