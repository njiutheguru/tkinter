
# external modules that build on top of tkinter to improve it
# customtkinter and ttkbootstrap
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk # nOt recommended for putting these widgets alongside customtkiter widgets

 # window
window = ctk.CTk()
window.title('Custom tkinter app')
window.geometry('600x400')

# create a widget
string_var = ctk.StringVar(value='a custome string')
label = ctk.CTkLabel(window,
                     text='A CTK label',
                     fg_color='aqua',
                     text_color='white',
                     corner_radius=10,
                     textvariable=string_var)
label.pack()
button = ctk.CTkButton(window, text='A ctk button', fg_color='#FF0', text_color='#000',
                       hover_color='#AA0',
                       command= lambda: ctk.set_appearance_mode('dark'))
button.pack()
# create a frame 9:45
frame = ctk.CTkFrame(window)
frame.pack()

# create a ctk slider
slider = ctk.CTkSlider(frame)
slider.pack(padx=20, pady=20)
# exercise
switch = ctk.CTkSwitch(window,
                       text='Exercise Switch',
                       fg_color=('blue','red'),
                       progress_color='pink',
                        button_color='green',
                        button_hover_color='yellow',
                        switch_width=60,
                        switch_height=30,
                        corner_radius=2
                       )
switch.pack()

if __name__ == '__main__':
    window.mainloop()