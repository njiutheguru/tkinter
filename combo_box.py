import tkinter as tk
from tkinter import ttk

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Combo and Spin boxes')

# combo box
items = ('Ice Cream', 'Pizza', 'Broccoli')
food_string = tk.StringVar(value='Ice Cream')
combo = ttk.Combobox(window, textvariable=food_string)
combo['values'] = items
# combo.configure(values=items)
combo.pack()
# combo box events
combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text=f'Selected item: {food_string.get()}'))

# combo_label = ttk.Label(window, text='a label', textvariable=food_string)
combo_label = ttk.Label(window,
                         text='a label')
combo_label.pack()


# Spinbox
spin_int = tk.IntVar(value=12)
spin = ttk.Spinbox(window, 
                   from_=3,
                     to=20, 
                     increment=2, 
                     command=lambda: print(spin_int.get()),
                     textvariable=spin_int)
# spin['value'] = (1,2,4,5,6,7)
# events binding in a spin box

spin.pack()
spin.bind('<<Increment>>', lambda event: print('Up'))
spin.bind('<<Decrement>>', lambda event: print('Down'))
# Spinbox exercise: Create a spinbox that contains the letters A, B , C D E  and print the value whenver the value is decreased
spin_box_var = tk.StringVar(value='A')
spin_box = ttk.Spinbox(window,
                       textvariable=spin_box_var)
spin_box['value'] = ('A','B','C','D','E')
spin_box.bind('<<Decrement>>', lambda event: print(spin_box_var.get()))
spin_box.pack(pady=20)








# run the app
window.mainloop()

