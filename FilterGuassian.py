import cv2
image = cv2.imread('./images/test.jpeg')
 
gaussian_blur = cv2.GaussianBlur(image,(11,11),sigmaX=0)
 
cv2.imshow('Original image', image)
cv2.imshow('Guassian image', gaussian_blur)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
