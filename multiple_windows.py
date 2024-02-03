import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

window = tk.Tk()
window.geometry('600x400')
window.title('Multiple Windows')

def ask_yn():
    answer = messagebox.askquestion('Title', 'Body')
    print(answer)

class extra(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('extra window')
        self.geometry('300x400')
        ttk.Label(self, text='A Label').pack()
        ttk.Button(self, text="A button").pack()
        ttk.Label(self, text='Another Label').pack(expand=True)


def create_window():
    global extra_window
    extra_window = extra()
    # extra_window = tk.Toplevel()
    # extra_window.title('extra window')
    # extra_window.geometry('200x300')
    # ttk.Label(extra_window, text='A label').pack()
    # ttk.Button(extra_window, text='A Button').pack()
    # ttk.Label(extra_window, text='Another label').pack(expand=True)
    

def exit_main():
    extra_window.destroy()

button1 = ttk.Button(window, text='Open Main Window', command=create_window)
button1.pack(expand=True)

button2 = ttk.Button(window, text='Close Main Window', command=exit_main)
button2.pack(expand=True)

button3 = ttk.Button(window, text='Create yes no window', command=ask_yn)
button3.pack(expand=True)

# run
if __name__ == "__main__":
    window.mainloop()

