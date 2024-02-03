# starts at 11: 15
# you can add images to some widgets(labels, buttons, canvas)
# But for images that scale properly, you will need to create logic yourself
#     On top of that, you will need the pillow library to use images # pip install pillow
# Image manipulation in pillow(A complete guide to pillow) 2 hours 17 minutes

import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

def stretch_image(event):
    global resized_tk

    # size of the canvas
    width = event.width
    height = event.height

    # create an image
    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(0,0,image=resized_tk, anchor='nw')


def fill_image(event):
    global resized_tk
    # current ratio
    canvas_ratio = event.width / event.height
     # get coordinates
    if canvas_ratio > image_ratio: # canvas wider than image
        width = int(event.width)
        height = int(width / image_ratio)
    else:
        height = int(event.height)
        width = int(height * image_ratio)

    resized_image = image_original.resize((width, height))
    resized_tk = ImageTk.PhotoImage(resized_image)
    canvas.create_image(int(event.width/2),
                        int(event.height/2),
                        anchor='center',
                        image=resized_tk)
    


def show_full_image(event):
    global resized_tk
    # current ratio
    canvas_ratio = event.width / event.height
     # get coordinates
    if canvas_ratio > image_ratio: # canvas wider than image
        height = int(event.height)
        width = int(height * image_ratio)
    else:
        width = int(event.width)
        height = int(width / image_ratio)

    if width > 0 and height > 0:    
        resized_image = image_original.resize((width, height))
        resized_tk = ImageTk.PhotoImage(resized_image)
        canvas.create_image(int(event.width/2),
                        int(event.height/2),
                        anchor='center',
                        image=resized_tk)


# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Images')

# grid layout
window.columnconfigure((0,1,2,3), weight=1, uniform='a')
window.rowconfigure(0,weight=1)

# import an image
image_original = Image.open('kasarani.jpg')
image_ratio = image_original.size[0] / image_original.size[1]
print(image_ratio)
image_or = Image.open('ostrich.jpg').resize((50,30))
image_tk = ImageTk.PhotoImage(image_or)

image_ctk = ctk.CTkImage(light_image=Image.open('kasarani.jpg'),
                          dark_image=Image.open('kasarani.jpg'))
# widget
# label = ttk.Label(window, text='ostrich', image=image_tk)
# label.pack()
button_frame = ttk.Frame(window)
button = ttk.Button(button_frame, text='A button   ', image=image_tk, compound='right')
button.pack(pady=10)
button_ctk = ctk.CTkButton(button_frame, text='A button', image=image_ctk, compound='left')
button_ctk.pack(pady=10)
button_frame.grid(column=0, row=0,sticky='nsew')

# canvas -> imagge
canvas = tk.Canvas(window, background='aqua', bd=0, highlightthickness=0, relief='raised')
canvas.grid(row=0, column=1,columnspan=3, sticky='news')
canvas.bind('<Configure>',show_full_image)
# run
if __name__ == '__main__':
    window.mainloop()

# end of the program...
