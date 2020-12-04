from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(kg.get())
        lbs.set(int(value*2.205))
    except ValueError:
        pass


app = Tk()
app.title('kg to lbs')
app.geometry('640x480')

mainframe = ttk.Frame(app, padding='3 3 12 12')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

app.columnconfigure(0, weight=1)
app.rowconfigure(0, weight=1)

kg = StringVar()
kg_entry = ttk.Entry(mainframe, width=7, textvariable=kg)
kg_entry.grid(column=2, row=1, sticky=(W, E))

lbs = StringVar()
ttk.Label(mainframe, textvariable=lbs).grid(column=2, row=2, sticky=(W, E))

calculate_button = ttk.Button(mainframe, text='Calculate', command=calculate)
calculate_button.grid(column=3, row=3, sticky=W)


ttk.Label(mainframe, text="kgs").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="lbs").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

kg_entry.focus()
app.bind("<Return>", calculate)

app.mainloop()


# Create window object
# app = Tk()
# app.title('Part Manager')
# app.geometry('640x480')


# # ttk frame
# test_frame = ttk.Frame(app, padding='3 3 12 12')
# test_frame.grid(column=1, row=5)


# # Part
# part_text = StringVar()
# part_label = Label(test_frame, text='Part Name', font=('bold', 14), pady=20)
# part_label.grid(row=0, column=0, sticky=W)

# part_entry = Entry(app, textvariable=[part_text])
# part_entry.grid(row=0, column=1)


# # Start program
# app.mainloop()
