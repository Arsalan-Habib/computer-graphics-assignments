from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from functools import partial
import numpy as np


# initializing the main app
app = Tk()
app.title('Image Calculator')
app.geometry('1080x720')

image1 = []
image2 = []


def open_image(panel):
    # getting the path and opening the image
    x = filedialog.askopenfilename(title='Select Image')
    img = Image.open(x)

    # resizing
    img = img.resize((200, 200), Image.ANTIALIAS)

    if(panel == panel1):
        global image1
        image1 = list(img.getdata())
        image1 = [i for s in image1 for i in s]
    else:
        global image2
        image2 = list(img.getdata())
        image2 = [i for s in image2 for i in s]

    # converting to Photoimage
    img = ImageTk.PhotoImage(img)

    # displaying the image.
    panel.configure(image=img)
    panel.image = img


def add(panel):

    res_arr = [x+y for x, y in zip(image1, image2)]
    res_arr = np.array(res_arr, dtype=np.uint8).reshape(200, 200, 3)
    img = Image.fromarray(res_arr, 'RGB')
    img.save('result.jpg')

    # converting to Photoimage
    img = ImageTk.PhotoImage(img)

    # displaying the image.
    panel.configure(image=img)
    panel.image = img


# creating the mainframe for all the widgets
mainframe = ttk.Frame(app, padding='10')
mainframe.grid(row=0, column=0, sticky=(N, E, S, W))


# Label for photo1
panel1 = Label(mainframe)
panel1.grid(row=1, rowspan=20, columnspan=5)

# Add photo button 1
add_photo_1 = ttk.Button(mainframe, text='Add Photo',
                         padding='5 2', command=partial(open_image, panel1))
add_photo_1.grid(row=0, column=2, sticky=(N))


# Label for photo2
panel2 = Label(mainframe)
panel2.grid(row=30, rowspan=20, columnspan=5)

# Add photo button 1
add_photo_2 = ttk.Button(mainframe, text='Add Photo',
                         padding='5 2', command=partial(open_image, panel2))
add_photo_2.grid(row=22, column=2, sticky=(N))


# Label for result photo
res_panel = Label(mainframe)
res_panel.grid(row=10, column=10, rowspan=20)


# The plus button
add_photos = ttk.Button(mainframe, command=partial(add, res_panel))
add_img = Image.open('./images/add.png')
add_img = add_img.resize((22, 22), Image.ANTIALIAS)
add_img = ImageTk.PhotoImage(add_img)
add_photos.configure(image=add_img)
add_photos.grid(row=1, column=6)


# The minus button
minus_photos = ttk.Button(mainframe)
minus_img = Image.open('./images/minus.png')
minus_img = minus_img.resize((22, 22), Image.ANTIALIAS)
minus_img = ImageTk.PhotoImage(minus_img)
minus_photos.configure(image=minus_img)
minus_photos.grid(row=3, column=6)


# The divide button
divide_photos = ttk.Button(mainframe)
divide_img = Image.open('./images/divide.png')
divide_img = divide_img.resize((22, 22), Image.ANTIALIAS)
divide_img = ImageTk.PhotoImage(divide_img)
divide_photos.configure(image=divide_img)
divide_photos.grid(row=2, column=5)


# The multiply button
multiply_photos = ttk.Button(mainframe)
multiply_img = Image.open('./images/multiply.png')
multiply_img = multiply_img.resize((22, 22), Image.ANTIALIAS)
multiply_img = ImageTk.PhotoImage(multiply_img)
multiply_photos.configure(image=multiply_img)
multiply_photos.grid(row=2, column=7)


# The equals button
equals_button = ttk.Button(mainframe)
equals_img = Image.open('./images/equals.png')
equals_img = equals_img.resize((22, 22), Image.ANTIALIAS)
equals_img = ImageTk.PhotoImage(equals_img)
equals_button.configure(image=equals_img)
equals_button.grid(row=2, column=6)


app.mainloop()
