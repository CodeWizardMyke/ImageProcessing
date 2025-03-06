import cv2 
import numpy as np

image = cv2.imread('../images/test.jpeg')

kernel_Sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
	
kernel_Sobel_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]
])

dst = cv2.filter2D(image,-1,kernel_Sobel_y)

imgConcat = np.concatenate((image, dst), axis=1)

cv2.imshow('Result',imgConcat)
cv2.waitKey(0)
cv2.destroyAllWindows()
