from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
from functools import partial
import numpy as np


# initializing the main app
app = Tk()
app.title('Image Calculator')
app.geometry('800x600')

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
    res_arr = [255 if val > 255 else val for val in res_arr]
    print(res_arr[:100])
    res_arr = np.array(res_arr, dtype=np.uint8).reshape(200, 200, 3)
    print(res_arr[:100])
    img = Image.fromarray(res_arr, 'RGB')
    img.save('result.jpg')

    # converting to Photoimage
    img = ImageTk.PhotoImage(img)

    # displaying the image.
    panel.configure(image=img)
    panel.image = img


def subtract(panel):

    res_arr = [x-y for x, y in zip(image1, image2)]
    res_arr = [0 if val < 0 else val for val in res_arr]
    print(res_arr[:100])
    res_arr = np.array(res_arr, dtype=np.uint8).reshape(200, 200, 3)
    print(res_arr[:100])
    img = Image.fromarray(res_arr, 'RGB')
    img.save('result.jpg')

    # converting to Photoimage
    img = ImageTk.PhotoImage(img)

    # displaying the image.
    panel.configure(image=img)
    panel.image = img


def multiply(panel):

    res_arr = [x*y for x, y in zip(image1, image2)]
    res_arr = [255 if val > 255 else val for val in res_arr]
    print(res_arr[:100])
    res_arr = np.array(res_arr, dtype=np.uint8).reshape(200, 200, 3)
    print(res_arr[:100])
    img = Image.fromarray(res_arr, 'RGB')
    img.save('result.jpg')

    # converting to Photoimage
    img = ImageTk.PhotoImage(img)

    # displaying the image.
    panel.configure(image=img)
    panel.image = img


def divide(panel):

    # res_arr = [x/y for x, y in zip(image1, image2)]
    # res_arr = [0 if val < 250 else val for val in res_arr]
    res_arr = []
    for x, y in zip(image1, image2):
        if(x == 0 and y == 0):
            res_arr.append(0)
        elif (x == 0):
            res_arr.append(1/y)
        elif (y == 0):
            res_arr.append(x/1)
        else:
            res_arr.append(x/y)

    print(res_arr[:100])
    res_arr = np.array(res_arr, dtype=np.uint8).reshape(200, 200, 3)
    print(res_arr[:100])
    img = Image.fromarray(res_arr, 'RGB')
    img.save('result.jpg')

    # converting to Photoimage
    img = ImageTk.PhotoImage(img)

    # displaying the image.
    panel.configure(image=img)
    panel.image = img


# creating the mainframe for all the widgets
mainframe = ttk.Frame(app, padding='50 20')
mainframe.grid(row=0, column=0, sticky=(N, E, S, W))

# creating the input frame 1
input_frame = ttk.Frame(mainframe, padding=15)
input_frame.grid(row=0, column=0, sticky=(N, W), rowspan=2)

# creating the input frame 2
input_frame2 = ttk.Frame(mainframe, padding=15)
input_frame2.grid(row=3, column=0, sticky=(N, W), rowspan=2)


# Label for photo1
panel1 = Label(input_frame)
panel1.grid(row=1, column=0, columnspan=5, pady=10)

# default white image
img = Image.open('./images/white.jpg')
img = img.resize((200, 200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel1.configure(image=img)
panel1.image = img


# Add photo button 1
add_photo_1 = ttk.Button(input_frame, text='Add Photo',
                         padding='5 2', command=partial(open_image, panel1))
add_photo_1.grid(row=0, column=2, sticky=(N))


# Label for photo2
panel2 = Label(input_frame2)
panel2.grid(row=1, column=0, columnspan=5, pady=10)
panel2.configure(image=img)
panel2.image = img

# Add photo button 2
add_photo_2 = ttk.Button(input_frame2, text='Add Photo',
                         padding='5 2', command=partial(open_image, panel2))
add_photo_2.grid(row=0, column=2, sticky=(N))


# Frame for result
res_frame = ttk.Frame(mainframe, padding=10)
res_frame.grid(row=0, column=4, rowspan=2)


# Panel for result photo
res_panel = Label(res_frame)
res_panel.grid(row=1, column=0, columnspan=5, pady=10)
res_panel.configure(image=img)
res_panel.image = img

# result photo label
res_label = ttk.Label(res_frame, text='Result')
res_label.config(font=("Helvetica", 16))
res_label.grid(row=0, column=2, sticky=(N))


# frame for the buttons
btn_frame = ttk.Frame(mainframe)
btn_frame.grid(row=1, column=3, padx='60')


# The plus button
add_photos = ttk.Button(btn_frame, padding=2, command=partial(add, res_panel))
add_img = Image.open('./images/add.png')
add_img = add_img.resize((22, 22), Image.ANTIALIAS)
add_img = ImageTk.PhotoImage(add_img)
add_photos.configure(image=add_img)
add_photos.grid(row=0, column=1)


# The minus button
minus_photos = ttk.Button(btn_frame, padding=2,
                          command=partial(subtract, res_panel))
minus_img = Image.open('./images/minus.png')
minus_img = minus_img.resize((22, 22), Image.ANTIALIAS)
minus_img = ImageTk.PhotoImage(minus_img)
minus_photos.configure(image=minus_img)
minus_photos.grid(row=2, column=1)


# The divide button
divide_photos = ttk.Button(
    btn_frame, padding=2, command=partial(divide, res_panel))
divide_img = Image.open('./images/divide.png')
divide_img = divide_img.resize((22, 22), Image.ANTIALIAS)
divide_img = ImageTk.PhotoImage(divide_img)
divide_photos.configure(image=divide_img)
divide_photos.grid(row=1, column=0)


# The multiply button
multiply_photos = ttk.Button(
    btn_frame, padding=2, command=partial(multiply, res_panel))
multiply_img = Image.open('./images/multiply.png')
multiply_img = multiply_img.resize((22, 22), Image.ANTIALIAS)
multiply_img = ImageTk.PhotoImage(multiply_img)
multiply_photos.configure(image=multiply_img)
multiply_photos.grid(row=1, column=2)


# The equals button
equals_button = ttk.Button(btn_frame, padding=2)
equals_img = Image.open('./images/equals.png')
equals_img = equals_img.resize((22, 22), Image.ANTIALIAS)
equals_img = ImageTk.PhotoImage(equals_img)
equals_button.configure(image=equals_img)
equals_button.grid(row=1, column=1)


app.mainloop()
