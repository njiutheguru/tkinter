# pack becomes much easier to use when you combine it with frames 
# you always create layouts in a single direction 
# but some items are frames that contains their own layouts 

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Pack and Frames')
window.geometry('700x500')

# create the top frame

top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text='First Label', background='aqua')
label2 = ttk.Label(top_frame, text='Label 2',background='blue')

# middle widget
label3 = ttk.Label(window, text='Label 3', background='green')

# bottom frame
bottom_frame = ttk.Frame(window)
label4 = ttk.Label(bottom_frame, text='Last of the Labels',background='orange')
button1 = ttk.Button(bottom_frame, text='Button 1')
button2 = ttk.Button(bottom_frame, text='Button 2')

# Layout

top_frame.pack(fill='both', expand=True)
label1.pack(fill='both', expand=True)
label2.pack(fill='both', expand=True)
top_frame.pack(fill='both', expand=True)
label3.pack(expand=True)

bottom_frame.pack(expand=True, fill='both', padx=20, pady=20)
button1.pack(side='left', expand=True, fill='both')
label4.pack(side='left',expand=True, fill='both')
button2.pack(side='left', expand=True, fill='both')

# exercise
# create 3 more buttons and another frame
# the frame should be on the right inside of the bottom frame
# and the buttons should be stacked vertically inside of it

# create a right frame inside the bottom frame
right_frame = ttk.Frame(bottom_frame)
# create the three frames
button_ex1 = ttk.Button(right_frame, text='Buttton ex 1')
button_ex2 = ttk.Button(right_frame, text='Buttton ex 2')
button_ex3 = ttk.Button(right_frame, text='Buttton ex 3')

right_frame.pack(side='right', fill='both', expand=True)
button_ex1.pack(fill='both', expand=True)
button_ex2.pack(fill='both', expand=True)
button_ex3.pack(fill='both', expand=True)

# run 
if __name__ =="__main__":   
    window.mainloop()