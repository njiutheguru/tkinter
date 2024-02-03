import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry
    print(entry.get())
    # string_label.set(entry.get())
    # update the label
    label.configure(text='some other different text')
    # label['text'] = 'some other text'
    button['state'] = 'disabled'
    entry['state'] = 'disabled'
    # print(label.configure())

def reset_func():
    entry['state'] = 'enabled'
    button['state'] = 'enabled'
    label['text'] = 'some text'

# window 
window = tk.Tk()
window.title("Getting and setting widgets")
window.geometry('800x500')
 # Widgets
# string_label = tk.StringVar()
label = ttk.Label(master = window, 
                  text='some text', #textvariable=string_label
                  )
label.pack()
# entry
entry = ttk.Entry(master=window)
entry.pack()
# button
button = ttk.Button(master=window,
                     text='The Button', command=button_func)
button.pack()

# Exercise button 
exercise_button = ttk.Button(master=window, text='exercise button', command=reset_func)
exercise_button.pack()

# run
window.mainloop()
 