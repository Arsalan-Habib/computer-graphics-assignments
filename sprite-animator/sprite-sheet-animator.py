import cv2 
import time

# Reading the sprite sheet
sprite_sheet = cv2.imread('fire-sprite-sheet.jpg')

# Storing the sprite sheet height and width in respective variables.
sheet_height=sprite_sheet.shape[0]
sheet_width=sprite_sheet.shape[1] 

# Calculating the singular width and height of a single frame 
frame_height = sheet_height // 3 
frame_width = sheet_width // 5 

# Tokenizes the sprite sheet into single frames and stores them in the Frames folder ordered by number(Starting from top left - Ending on bottom right).
def tokenize_image():
    for x in range(3):
        for y in range(5):
            frame = sprite_sheet[frame_height*x:frame_height*(x+1),frame_width*y:frame_width*(y+1)]
            cv2.imwrite('frames/'+'Frame'+str((5*x)+(y+1))+'.jpg',frame)
            print((5*x)+(y+1))
        

tokenize_image()

# loop variables(i for rows, j for columns)
i=0
j=0

while True:
    # Setting the frame rate to 15fps
    time.sleep(1/15)

    # Generating and displaying the individual frames 
    frame = sprite_sheet[frame_height*i:frame_height*(i+1),frame_width*j:frame_width*(j+1)]    
    cv2.imshow('sprite-animation',frame)
    
    # incrementing the column, using the modulo operator to ensure the value doesnt exceed the number of columns.
    j+=1
    j = j%5

    # incrementing the row, only if j=0(after modulus, meaning j=5 which is the max number of columns in concerned sprite sheet.) 
    if j == 0:
        i+=1
        i = i%3
   

    # Stop the animation on entry of character 'q'.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

