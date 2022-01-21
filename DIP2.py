# Conversion of RGB to Gray Image and subtraction of some black part of image

import numpy as np 
import cv2

# reading the images
img1 = cv2.imread('Tanjiro.jpg')

#Convert into grayscale
gray_image = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

cv2.imwrite('DIP2_Gray.jpg', gray_image)
# TO show the output
cv2.imshow('DIP2_Gray', gray_image) 
# subtract the images
img2 = cv2.imread('DIP2_Gray.jpg')
img3 = cv2.imread('DIP2_Gray_Black.jpg')
subtracted = cv2.subtract(img2, img3)
# TO show the output
cv2.imwrite('subtracted.jpg', subtracted)
cv2.imshow('image', subtracted)

 
# To close the window
cv2.waitKey(0)
cv2.destroyAllWindows()