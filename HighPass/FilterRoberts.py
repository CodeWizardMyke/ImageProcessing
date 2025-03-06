import cv2 
import numpy as np
image = cv2.imread('../images/test.jpeg')

kernel_Roberts_x = np.array([
    [1, 0],
    [0, -1]
    ])

dst = cv2.filter2D(image,-1,kernel_Roberts_x)

imgs_concat = np.concatenate((image, dst), axis=1)

cv2.imshow('Result',imgs_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()
