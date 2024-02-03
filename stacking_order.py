# Widgets are always placed on top of other widgets when they are created (not when they are placed!)

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Stacking Order')
window.geometry('500x400')

# widgets
label1 = ttk.Label(window, text='Label 1', background='aqua')
label2 = ttk.Label(window, text='Label 2', background='yellow')
label3 = ttk.Label(window, text='Label 3', background='yellow')

# stacking methods
# label1.lift() # argument aboveThis
# label2.lower()
# e.g label1.lift(aboveThis)


button1 = ttk.Button(window, text="Raise Label 1", command=lambda: label1.lift())
button2 = ttk.Button(window, text="Raise Label 2", command=lambda: label2.lift())
button3 = ttk.Button(window, text="Raise Label 3", command=lambda: label3.tkraise())# tk raise argument aboveThis


# Layout
label1.place(x=50, y=100, width=200, height=150)
label2.place(x=150, y=60, width=140, height=100)
label3.place(x=130, y=120, width=140, height=100)

button1.place(rely=1, relx=0.84, anchor='se')
button2.place(rely=1, relx=1, anchor='se')
button3.place(rely=1, relx=0.68, anchor='se')

# run the app
if __name__ == "__main__":
    window.mainloop()