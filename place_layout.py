# widgets are placed by specyfing the left, top, width and height
# these numbers can be absolute or relative

import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('700x500')
window.title('Place Layout')
print(window.winfo_screenwidth(),window.winfo_screenheight())

# widgets
label1 = ttk.Label(window, text='Label 1', background='aqua')
label2 = ttk.Label(window, text='Label 2', background='gray')
label3 = ttk.Label(window, text='Label 3', background='pink')
button1 = ttk.Button(window, text='Button 1')

# place layout
label1.place(relx=0.4, y=0.7, width=500, height=200)
label2.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.5)
label3.place(x=0.6*700, y=0.2*500, width=0.1*700, height=0.5*500)
button1.place(relx=1, rely=1, anchor='se')

# frame
frame = ttk.Frame(window)
frame_label = ttk.Label(frame, text='Frame Label', background='yellow')
frame_button = ttk.Button(frame, text='Frame Button')

# Frame Layout
frame.place(relx=0, rely=0, relwidth=0.3, relheight=1)
frame_label.place(relx=0, rely=0, relwidth=1, relheight=0.5)
frame_button.place(relx=0, rely=0.5, relwidth=1, relheight=0.5)

# exercise: crate a label and place it right in the center of the window. The label should be half as wide as the window and the 200px tall
ex_label = ttk.Label(window, text='exercise label', background='orange')
ex_label.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.3,anchor='center')








if __name__ == "__main__":
    window.mainloop()

