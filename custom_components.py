# To use tkinter (or any gui framework) efficiently you need to create your own components
import tkinter as tk
from tkinter import ttk

# def create_segment(parent, label_text, button_text):
#     frame = ttk.Frame(master=parent)

#     # grid layout
#     frame.rowconfigure(0, weight=1)
#     frame.columnconfigure((0,1,2), weight=1, uniform='a')

#     # widgets
#     ttk.Label(frame, text=label_text).grid(row=0,column=0, sticky='news')
#     ttk.Button(frame, text=button_text).grid(row=0,column=1, sticky='news')
    
#     return frame

class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, button_t):
        super().__init__(master=parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2), weight=1, uniform='a')

        # widgets
        ttk.Label(self, text=label_text).grid(row=0,column=0, sticky='news')
        ttk.Button(self, text=button_text).grid(row=0,column=1, sticky='news')

        self.pack(expand=True, fill='both', padx=10, pady=10)

        # self.second_widget(parent,'Button 1').grid(row=0, column=3)
        self.second_widget(button_t).grid(row=0, column=2, padx=10,sticky='news')

    def second_widget(self, button_t):
        frame_2 = ttk.Frame(self)
        # frame_2.grid(row=0, column=2, columnspan=2)
        # grid configure
        frame_2.rowconfigure((0,1), weight=1, uniform='a')
        frame_2.columnconfigure((0), weight=1, uniform='a')
        bn = ttk.Button(frame_2, text=button_t)
        bn.grid(row=1, column=0, sticky='nsew', rowspan=2)
        ent = ttk.Entry(frame_2)
        ent.grid(row=0, column=0,sticky='news')

        return frame_2


# window 
window = tk.Tk()
window.title('Widgets and Return') 
window.geometry('400x600')

# widgets

# create_segment(window, 'Label', 'Button').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'Test', "Click").pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'Hello Bro', 'Test').pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'Bye', "Launch").pack(expand=True, fill='both', padx=10, pady=10)
# create_segment(window, 'Last one', 'Exit').pack(expand=True, fill='both', padx=10, pady=10)

Segment(window, 'Label', 'Button', 'Button 1')
Segment(window, 'Test', "Click", 'Button 2')
Segment(window, 'Hello Bro', 'Test', 'Button 3')
Segment(window, 'Bye', "Launch", 'Button 4')
Segment(window, 'Last one', 'Exit', 'Button 5')

# exercise: create a smaller widget inside of the segment class using a function/method
# It should be a container that has an entry field and a button stacked on top of each other
# the button should be set via the paramenters
# all of this should be on the third column

window.mainloop()
