# inbuilt styling tools
# widget options and the style object
# external themes
# external modules (customtkinter and ttkbootstrap)

import tkinter as tk
from tkinter import ttk, font


window = tk.Tk()
window.title('Styling')
window.geometry('600x400')

# print(font.families())

# style
style = ttk.Style()
# print(style.theme_names())
# style.theme_use('classic')

style.configure('new.TButton', foreground='green', font=('Jokerman',20))
style.map('new.TButton',
          foreground=[('pressed','red'),
                       ('disabled','yellow')],
          background= [('pressed','green'),
                        ('active','blue')]
                        )

# styling for the frame
style.configure('TFrame', background='pink')

# widgets
label = ttk.Label(window, 
                  text='A Label \n and then another line', 
                  background='pink',
                    foreground='green',
                    font=('Qaz', 20),
                    justify='right')
label.pack()
button = ttk.Button(window, 
                    text='A button', 
                    style='new.TButton')
button.pack(pady=20)

# exercise
# add a frame with a width and height and give it a pink background color
frame = ttk.Frame(window, height=200, width=100,style='TFrame').pack(expand=True)

window.mainloop()