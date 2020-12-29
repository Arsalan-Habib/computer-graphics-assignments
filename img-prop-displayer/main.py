import cv2 as cv
import numpy as np

# Reading the image
image = cv.imread('../sample-images/boat-sailing.jpg')

# Getting the image properties
img_height = image.shape[0]
img_width = image.shape[1]
color_channels = image.shape[2]

# Setting variables for the text.
font_color = (20,20,20)
font = cv.FONT_HERSHEY_SIMPLEX
font_size = 1
font_thickness = 2

# Storing the property data into an array for iteration later.
text = ['Image Properties:','Image Width: '+str(img_width) + ' pixels' ,'Image Height: '+str(img_height) + ' pixels' , 'Color Channels: '+str(color_channels)]

# Add padding on the right of the image for displaying the properties.
new_image = cv.copyMakeBorder(image,0,0,0,500,cv.BORDER_CONSTANT,None,(240,240,240))

# Setting the initial pixel coordinates for text placement.
x,y= (img_width+50,80)

# Looping and adding text to the image.
for i in range(4):
    new_image = cv.putText(new_image, text[i], (x,y), font, font_size, font_color, font_thickness, cv.LINE_AA)
    y+=70

# Displaying the final image with the properties.
cv.imshow('Image-Properties',new_image)

# Closing the window.
cv.waitKey(0)
cv.destroyAllWindows()