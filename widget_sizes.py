# starts at 5:45
# Widget can have a custom size But that size wil be overwritten by the layout method

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Widgets Sizes')
window.geometry('600x400')

# widgets
label1 = ttk.Label(window, text='Label 1', background='yellow')
label2 = ttk.Label(window, text='Label 2', background='aqua', width=50)

# Layout
# label1.pack()
# label2.pack(fill='x')

# grid layout method
window.columnconfigure((0,1), weight=1, uniform='a')
window.rowconfigure((0,1), weight=1, uniform='a')

label1.grid(row=0, column=0)
label2.grid(row=1, column=0, sticky='nsew')


# run the app
if __name__ == "__main__":
    window.mainloop()
