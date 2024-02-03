import tkinter as tk
from tkinter import ttk
 # create a window
window = tk.Tk()
window.geometry('600x500')
window.title('Event Binding')
 
# widgets
text = tk.Text(window)
text.pack(padx=10, pady=10)

entry = ttk.Entry(window)
entry.pack()

btn =ttk.Button(window, text='A button')
btn.pack()

# events
# List of events
# pythontutorial.net/tkinter/tkinter-event-binding
# window.bind('<Alt-KeyPress-a>',lambda event: print(event))

btn.bind('<Alt-KeyPress-a>',lambda event: print(event))
# events binding with functions
def get_pos(event):
    print(f'x: {event.x}  y: {event.y}')

text.bind('<Motion>', get_pos)
# binding an event to a key press 
btn.bind('<KeyPress>', lambda event: print(f'a button is pressed ({event.char})'))
# entry widget selection and uselection
entry.bind('<FocusIn>', lambda event: print('The entry widget is selected'))
entry.bind('<FocusOut>', lambda event: print('The entry widget is unselected'))
# exercise: Print 'mousewheel' when the user hold down shift and uses the mousewheel while test is selected
text.bind('<Shift-MouseWheel>', lambda event: print('MouseWheel'))

# run the app
window.mainloop()


