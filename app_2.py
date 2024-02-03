import tkinter as tk
from tkinter import ttk # modern widgets

def button_function():
    print('a button was pressed')

def exercise_function():
    print("Hello")

 # Create a window

window = tk.Tk()
# Set the title
window.title('Window and Widgets')
window.geometry('800x500')
# Create widgets
text_input =tk.Text(master=window) # text input widget
# ttk widgets
text_label = ttk.Label(master=window, text='This is a test')
text_label.pack()
text_input.pack()
# Create a text input
entry = ttk.Entry(master=window)
entry.pack()
# button
# exercise label
exercise_label = ttk.Label(master=window, text='my label')
exercise_label.pack()
button = ttk.Button(master=window, text="A Button", command=button_function)
button.pack()
# Exercise button
exercise_button = ttk.Button(master=window, text='exercise_button', command=exercise_function)
exercise_button.pack()
# Run the application
window.mainloop()
# The mainloop updates the gui
# It also checks for events (button clicks, mouse movements, closing the window)
