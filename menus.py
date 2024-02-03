import tkinter as tk
from tkinter import ttk

window =tk.Tk()
window.geometry('600x500')
window.title('Menus')

# create a menu canvas/widget (invisible)
menu = tk.Menu(window)
# place the menu canvas inside the window
window.configure(menu=menu)
# create a menu item 
file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=lambda: print('New file'))
file_menu.add_command(label='Open', command=lambda: print('Open file'))
file_menu.add_command(label='Save', command=lambda: print('Save file'))
file_menu.add_separator()

help_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label='Help',menu=help_menu)
help_menu.add_command(label='Query', command=lambda: print(f'Check menu is {help_check_string.get()}'))
help_menu.add_command(label='FAQs', command=lambda: print('Visit frequently asked qustions here'))
# create another check help sub menu
help_check_string = tk.StringVar(value='off')
help_menu.add_checkbutton(label='Check', onvalue='on', offvalue='off', variable=help_check_string)
help_menu.add_separator()

# creating a menu button/drop down menu
menu_button = ttk.Menubutton(window, text='Menu Button')
menu_button.pack()

button_sub_menu = tk.Menu(menu_button, tearoff=False)
menu_button.configure(menu=button_sub_menu)
button_sub_menu.add_command(label='label', command=lambda: print(' drop down menu'))
button_sub_menu.add_checkbutton(label='check 1')

# exercise: add another menu to the main emnu, this one should have a sub menu
# try to read: https://www.tutorialspoint.com/python/tk_menu.htm

exercise_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_command(label='exercise test')
# configure the exercise menu
menu.add_cascade(label='Exercise', menu=exercise_menu)
# create a sub  menu with three options
exercise_sub_menu = tk.Menu(menu, tearoff=False)
exercise_menu.add_cascade(label='File', menu=exercise_sub_menu)
exercise_sub_menu.add_command(label='Create New file')
exercise_sub_menu.add_command(label='Open file')
exercise_sub_menu.add_command(label='Save file')


# run the app
if __name__ == "__main__":
    window.mainloop()
