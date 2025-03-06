import cv2
import numpy as np

img = cv2.imread('brain.png')

kernel = np.array(
    [
        [1/5, 1/5, 1/5, 1/5, 1/5],
        [1/5, 1/5, 1/5, 1/5, 1/5],
        [1/5, 1/5, 1/5, 1/5, 1/5],
        [1/5, 1/5, 1/5, 1/5, 1/5],
        [1/5, 1/5, 1/5, 1/5, 1/5]
    ]
)
#kernel = np.ones((5,5),np.float32)/25

dst = cv2.filter2D(img, -1, kernel)

imgConcat = np.concatenate((img, dst), axis = 1)

cv2.imshow('Result',imgConcat)
cv2.waitKey(0)
cv2.destroyAllWindows()
