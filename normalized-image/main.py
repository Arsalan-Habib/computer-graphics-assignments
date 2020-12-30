import cv2 as cv
import numpy as np

# Reading the image
image = cv.imread('../sample-images/square.jpg')

# Resizing the image
image = cv.resize(image,(250,250))

# Converting to grayscale
GrayScale_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# Converting to Binary, The threshold we use is 127.
(thresh, BnW_Image) = cv.threshold(GrayScale_image, 127, 255, cv.THRESH_BINARY)

# Creating a empty black array for destination of normalized image.
normalizedImg = np.zeros((250, 250))
# Saving the normalized image to the black image.
normalizedImg = cv.normalize(image,  normalizedImg, 0, 1, cv.NORM_MINMAX, dtype=cv.CV_32F)

# Displaying all the various images.
cv.imshow('Normalized Image',normalizedImg)
cv.imshow('RGB image',image)
cv.imshow('Binary Image',BnW_Image)
cv.imshow('GrayScale image', GrayScale_image)

print(image[50,50], normalizedImg[50,50])

# Closing the window.
cv.waitKey(0)
cv.destroyAllWindows()