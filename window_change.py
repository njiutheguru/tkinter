import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('More on the window')
wid=int(window.winfo_screenwidth())
heig=int(window.winfo_screenheight())
x_w = 700
y_h = 500
x_place = int(wid/2 - x_w/2)
y_place = int(heig/2 - y_h/2)
window.geometry(f'{x_w}x{y_h}+{x_place}+{y_place}')
# + indicates the placement on the screen size x, and y
window.iconbitmap('logo-white.ico')
# exercise
# start the window in the middle of the screen


# window sizes
window.minsize(200, 100)
# window.maxsize(900, 700)
window.resizable(True, True) # x is resizable but not y

# window sizes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

# window attributes
window.attributes('-alpha')
# window.attributes('-topmost', True) # the screen overrides every other screen opened and remains opened and at the top

# security event
window.bind('<Escape>', lambda event: window.quit())
# window.attributes('-disable', True)
# window.attributes('-fullscreen', True)

# title bar
window.overrideredirect(False)
grip = ttk.Sizegrip(window)
grip.place(relx=1.0, rely=1.0, anchor='se')


# run
if __name__ == '__main__':
    window.mainloop()