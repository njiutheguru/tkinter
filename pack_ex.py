import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('700x500')
window.title('Pack')

# create the widgets
label1 = ttk.Label(window, text='First Label', background='red')
label2 = ttk.Label(window, text='Label 2', background='aqua')
label3 = ttk.Label(window, text='Label 3', background='gray')
button = ttk.Button(window, text='Button')

# Layout
label1.pack(side='top',fill='both', padx=10, pady=10,ipady=50)
label2.pack(side='left', expand=True,fill='both')
label3.pack(side='top', expand=True, fill='both')
button.pack(side='top', expand=True, fill='both')

# run the app
if __name__ == "__main__":
    window.mainloop()