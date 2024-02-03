# There are three widgets that can be scrolled:
# Canvas, Text and Treeview
# Canvas is the most useful one since it can display widgets
 
import tkinter as tk
from tkinter import ttk
from random import randint, choice

 # create a window 
window = tk.Tk()
window.geometry('700x500')
window.title('Scroll Window')

# canvas
# canvas = tk.Canvas(window, bg='white', scrollregion=(0,0,2000,5000))
# canvas.create_line(0,0,2000,5000, fill='green', width=10)
# canvas.pack(expand=True, fill='both')

# for i in range(100):
#     l = randint(0,2000)
#     t = randint(0,5000)
#     r = l + randint(10, 5000)
#     b = t + randint(10, 5000)
#     color = choice (('green','aqua','gray','light blue','light green', 'orange', 'purple','pink'))
#     canvas.create_rectangle(l,t,r,b, fill=color)


# # creating a mousewheel scrolling effect
# canvas.bind('<MouseWheel>', lambda event: canvas.yview_scroll(int(event.delta / 60), 'units'))
#     # creating the scrollbar
# scrollbar = ttk.Scrollbar(window, orient='vertical', command=canvas.yview)
# canvas.configure(yscrollcommand=scrollbar.set)
# scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

# # scroll bar exercise
#   # create a horizontal srollbar at the bottom and use it to scroll the canvas lef tand right 
# scrollbar_bottom = ttk.Scrollbar(window, orient='horizontal', command=canvas.xview)
# canvas.configure(xscrollcommand=scrollbar_bottom.set)
# scrollbar_bottom.place(relx=0, rely=1, relwidth=1, anchor='sw')

# # addd an evetn to scroll left or right on ctr + mousewheel

# canvas.bind('<Control MouseWheel>', lambda event: canvas.xview_scroll(int(event.delta / 60), 'units'))

# text scrollbar
# text = tk.Text(window)
# for i in range(1, 200):
#     text.insert(f'{i}.0', f'text: {i}.0 \n')

# text.pack(expand=True, fill='both')

# # add a scrolling bar
# scrollbar_text = ttk.Scrollbar(window, orient='vertical', command=text.yview)
# text.configure(yscrollcommand=scrollbar_text.set)
# scrollbar_text.place(relx=1, rely=0, relheight=1, anchor='ne')


# Treeview 
table = ttk.Treeview(window, columns=(1,2), show='headings')
table.heading(1, text='First Name')
table.heading(2, text='Last Name')
first_names = ['Bob', 'Marley', 'Angela','Losa','Bakar','Fahad','Moha','Said','Andrei','Juliet','Grace','Otieno']
last_names = ['Kamau','Kariuki','Karim','Kampany','Neagoie','Richard','Ricky','Wambui','Sylvester','Atieno']

for i in range(100):
    table.insert(parent='', index=tk.END, values=(choice(first_names), choice(last_names)))
table.pack(expand=True, fill='both')

# creating a table scroll bar
scrollbar_table = ttk.Scrollbar(window, orient='vertical', command=table.yview)
table.configure(yscrollcommand=scrollbar_table.set)
scrollbar_table.place(relx=1, rely=0, relheight=1, anchor='ne')
# run the app
if __name__ == "__main__":
    window.mainloop()