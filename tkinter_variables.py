import tkinter as tk
from tkinter import ttk

def button_func():
    print(string_var.get())
    string_var.set('Button has been pressed')
    test_string.set('This is the new value of the test')

# window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('399x433')
# ttk variable(string variable)
string_var = tk.StringVar(value='default text')
# widgets 
label = ttk.Label(master=window, text='label', textvariable=string_var)
label.pack()
entry = ttk.Entry(master=window, textvariable=string_var)
entry.pack()
entry2 = ttk.Entry(master=window, textvariable=string_var)
entry2.pack(pady=10)
# run
button = ttk.Button(master=window, text='button', command=button_func)
button.pack(pady=10)
# creating 2 entry fields and 1 labels, they should all be connected via a stringvar. the start value is 'test'
test_string = tk.StringVar(value='test')
test_label = ttk.Label(master=window, textvariable=test_string)
test_label.pack(pady=10)
first_entry = ttk.Entry(master=window, textvariable=test_string)
second_entry = ttk.Entry(master=window, textvariable=test_string)
first_entry.pack(pady=10)
second_entry.pack(pady=10)

window.mainloop()