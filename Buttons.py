 # start at 1.07
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('buttons')
window.geometry('499x333')
#  Simple button
def button_func():
    print('a basic button')
    print(radio_var.get())

button_string = tk.StringVar(value='A button with a string var')
button = ttk.Button(window, text='A simple Button', command=lambda: print("This is a basic button"),
                    textvariable=button_string)
button.pack()
# Check Button

check_var = tk.IntVar(value=10) # We can instead use IntVar instead of StringVar and would work the same...
check1 = ttk.Checkbutton(window, 
                        text='checkbox 1',
                        variable=check_var,
                        command = lambda: print(check_var.get()),
                        onvalue=10,
                        offvalue=5)
check1.pack()

check2 = ttk.Checkbutton(window, 
                        text='checkbox 2',
                        # variable=check_var,
                        command = lambda: print(check_var.get())
)



check2.pack()
# Radio buttons
# Setting up a string_var
radio_var = tk.StringVar()

radio1 = ttk.Radiobutton(window, 
                         text='radio_button 1', value= 'button 1',
                         variable=radio_var,
                         command=lambda: print(radio_var.get())
                         )

radio2 = ttk.Radiobutton(window, 
                         text='radio_button 2', value='button 2',
                         variable=radio_var)
radio1.pack()
radio2.pack()
# exercise let's go 

def radio_func():
    check_bool.set(False)
    print(check_bool.get())
    


# data
radio_string = tk.StringVar()
check_bool = tk.BooleanVar()
# widgets
exercise_radio1 = ttk.Radiobutton(window,
                                   text='Radio A', value='A', command=radio_func,variable=radio_string)

exercise_radio2 = ttk.Radiobutton(window,
                                   text='Radio B', value='B', command=radio_func,variable=radio_string)
exercise_check = ttk.Checkbutton(window, 
                                 text='exercise check',
                                 variable=check_bool,
                                 command=lambda: print(radio_string.get()))
# layout
exercise_radio1.pack()
exercise_radio2.pack()
exercise_check.pack()
# run the mainloop
window.mainloop()