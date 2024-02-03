# Hiding and showing widgets (toggling widgets)
# You don't really hide/reveal widgets. Instead you remove and add widgets to the layout. 
# Pack to place a widget, pack_forget to remove it
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Toggling Widgets')

# functionality
def toggle_label_grid():
    global label_visible

    if label_visible:
        label.grid_forget()
        # label.place_forget()
        label_visible = False
    else:
        label_visible = True
        # label.place(relx=0.5, rely=0.5, anchor='center')
        label.grid(column=1, row=0)


        
# widgets
# button = ttk.Button(window, text='Toggle Label_grid', command=toggle_label_grid)
# button.place(x=10, y=10)

def toggle_label_pack():
    global label_visible

    if label_visible:
        label.pack_forget()
        label_visible = False
        frame.pack(expand=True, before=button)
    else:
        frame.pack_forget()
        label_visible = True
        label.pack(expand=True, before=button)

button = ttk.Button(window, text='Toggle Label_pack', command=toggle_label_pack)
label_visible = True
label = ttk.Label(window, text="A Label ")
# label.place(relx=0.5, rely=0.5, anchor='center')

# Layout using the toggle button
window.columnconfigure((0,1), weight=1, uniform='a')
window.rowconfigure(0, weight=1, uniform='a')

# button.grid(column=0,row=0)
# label.grid(column=1, row=0)

# Pack method
label.pack(expand=True)
button.pack()

frame = ttk.Frame(window)
# run the app

if __name__ == "__main__":
    window.mainloop()

