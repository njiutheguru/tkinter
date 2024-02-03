# starts at 9: 18
# Using hexadecimal decimal numbers for colors
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Colors')
window.geometry('400x300')

# widgets
ttk.Label(window, background='red').pack(expand=True, fill='both')
# using hexadecimal system
ttk.Label(window, background='#08F').pack(expand=True, fill='both')
ttk.Label(window, background='#4fc296').pack(expand=True, fill='both')

# creating a brownish color 
ttk.Label(window, background='#C50').pack(expand=True, fill='both')

# black color
ttk.Label(window, background='#000').pack(expand=True, fill='both')
# grey color
ttk.Label(window, background='#444').pack(expand=True, fill='both')
# white color
ttk.Label(window, background='#FFF').pack(expand=True, fill='both')

if __name__ == '__main__':
    window.mainloop()