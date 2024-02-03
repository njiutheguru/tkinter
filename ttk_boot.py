# start at 10:00
import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk # works same like tkinter ttk

# create a window
window = ttk.Window(themename='litera')
window.title('Ttk bootstrap intro')
window.geometry('400x300')

label = ttk.Label(window, text='Label')
label.pack(pady=10)

button1 = ttk.Button(window, text='RED 1', bootstyle='danger-outline')
button1.pack(pady=10)

button2 = ttk.Button(window, text='WARNING 2', bootstyle= 'warning')
button2.pack(pady=10)

button3 = ttk.Button(window, text='SUCCESS 3', bootstyle='success')
button3.pack(pady=10)

if __name__ == '__main__':
    window.mainloop()