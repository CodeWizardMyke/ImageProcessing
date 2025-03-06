import cv2

image = cv2.imread('./images/test.jpeg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
