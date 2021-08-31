'''
import cv2
import numpy as np

image = cv2.imread('C:/Users\/JunJe Hur/Desktop/picture/0/001.png')

sharpening_1 = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])


cv2.imshow('before',image)
dst = cv2.filter2D(image, -1, sharpening_1)
cv2.imshow('Sharpening1', dst)


cv2.waitKey()
'''

import numpy as np
import cv2

im = cv2.imread('C:/Users\/JunJe Hur/Desktop/picture/0/001.png')
row, col = im.shape[:2]
bottom = im[row-2:row, 0:col]
mean = cv2.mean(bottom)[0]

bordersize = 10
border = cv2.copyMakeBorder(
    im,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=[mean, mean, mean]
)

cv2.imshow('image', im)
cv2.imshow('bottom', bottom)
cv2.imshow('border', border)
cv2.waitKey(0)
cv2.destroyAllWindows()