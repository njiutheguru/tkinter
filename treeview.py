import tkinter as tk
from tkinter import ttk
from random import choice

# window
window = tk.Tk()
window.geometry('700x500')
window.title('Treeview')

# data
first_names = ['Bob', 'Andrew', 'Rais','Guru','Mathew','Adonijah','Hilary','Escobar','Martinez','Sam']
last_name = ['Kamau','Achieng', 'Ouma', 'Otieno', 'Kulo','Salma','Halima','Bakari','Rashid','Moha','Diego']
# create a treeview
table = ttk.Treeview(window, columns=('first', 'last','email'), show='headings')
table.heading('first', text='First name')
table.heading('last', text='Surname')
table.heading('email', text='Email')
table.pack(fill='both', expand=True)

# Insert values into the table
# table.insert(parent='', index=0, values=('John', 'Doe', 'johndoe@email.com'))
for i in range(100):
    first = choice(first_names).capitalize()
    second = choice(last_name).capitalize()
    email = f'{first.lower()}{second.lower()}@email.com'
    data = (first, second, email)
    table.insert(parent='', index=0,values=data)

# inserting at the end of the table
table.insert(parent='', index=tk.END, values=('master','guru','masterguru@gmail.com'))

# events
# items refers to the whole row with all columns data
# table.selection show all items selected inside a tuple
# to get the real values of table selections, use a for loop of tap the ['values'] and print them...
def items_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])

table.bind('<<TreeviewSelect>>', items_select)

def delete_items(_):
    for i in table.selection():
        print(i)
        table.delete(i)

table.bind('<Delete>',delete_items)

# run
window.mainloop()