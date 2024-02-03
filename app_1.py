import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk # Install exteranl package

def convert():
    miles_input = entry_int.get()
    km_output = miles_input * 1.61
    string_var.set(km_output)





 # create a window
window = ttk.Window(themename = 'journal') # Can also use 'journal'
#  Create the shape of the window
window.title('Demo')
window.geometry('500x300')

# title
title_label = ttk.Label(master=window, text="Miles to Kilometers", font='Calibri 24 bold')
title_label.pack()
# Create an imput field
input_frame = ttk.Frame(master=window)
entry_int = tk.DoubleVar()

entry = ttk.Entry(master= input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert", command=convert)
input_frame.pack(pady=10) # Can be placed anywhere after, before, or between the two widgets
# Entry and button have to be placed in the same order to appear
entry.pack(side='left', padx=10)
button.pack(side='left')
 # output
string_var = tk.StringVar()
output_label = ttk.Label(master=window, 
                         text='Output', 
                         font='Calbri 24 italic', textvariable=string_var)


output_label.pack(pady=10)





# Run the application
window.mainloop()


