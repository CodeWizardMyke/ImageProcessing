import cv2
 
image = cv2.imread('./images/test.jpeg')
gaussian_blur = cv2.GaussianBlur(image,(5,5),sigmaX=0)
edges = cv2.Canny(gaussian_blur,100,200)
 
cv2.imshow('Original image', image)
cv2.imshow('Canny image', edges)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
