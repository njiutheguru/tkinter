# tkinter lacks inbuilt tools for responsive layouts
# We cannot update an existing layout
# we need to create a separate layout for each window size
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self, start_size):
        super().__init__()
        self.title('Responsive Layout')
        self.geometry(f'{start_size[0]}x{start_size[1]}')

        self.frame = ttk.Frame(self)

        ttk.Label(self.frame, text='Label 1', background='gray').pack(expand=True, fill='both', padx=5, pady=5)  
        ttk.Label(self.frame, text='Label 2', background='aqua').pack(expand=True, fill='both', padx=5, pady=5)
        ttk.Label(self.frame, text='Label 3', background='light green').pack(expand=True, fill='both', padx=5, pady=5)
        ttk.Label(self.frame, text='Label 4', background='pink').pack(expand=True, fill='both', padx=5, pady=5)

        self.frame.pack(expand=True, fill='both')

        SizeNotifier(self,
                      {300: self.create_small_layout,
                        600: self.create_medium_layout,
                        900: self.create_large_layout})
        
        self.mainloop()

    def create_small_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)

        ttk.Label(self.frame, text='Label 1', background='gray').pack(expand=True, fill='both', padx=5, pady=5)  
        ttk.Label(self.frame, text='Label 2', background='aqua').pack(expand=True, fill='both', padx=5, pady=5)
        ttk.Label(self.frame, text='Label 3', background='light green').pack(expand=True, fill='both', padx=5, pady=5)
        ttk.Label(self.frame, text='Label 4', background='pink').pack(expand=True, fill='both', padx=5, pady=5)

        self.frame.pack(expand=True, fill='both')

    def create_medium_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1), weight=1, uniform='a')
        self.frame.rowconfigure((0,1), weight=1, uniform='a')
        self.frame.pack(expand=True, fill='both')

        ttk.Label(self.frame, text='Label 1', background='gray').grid(row=0, column=0, sticky='news')
        ttk.Label(self.frame, text='Label 2', background='aqua').grid(row=1, column=0, sticky='news')
        ttk.Label(self.frame, text='Label 3', background='light green').grid(row=0, column=1, sticky='news')
        ttk.Label(self.frame, text='Label 4', background='pink').grid(row=1, column=1, sticky='news')

    def create_large_layout(self):
        self.frame.pack_forget()
        self.frame = ttk.Frame(self)
        self.frame.columnconfigure((0,1,2,3), weight=1, uniform='a')
        self.frame.rowconfigure(0, weight=1, uniform='a')
        self.frame.pack(expand=True, fill='both')

        ttk.Label(self.frame, text='Label 1', background='gray').grid(row=0, column=0, sticky='news')
        ttk.Label(self.frame, text='Label 2', background='aqua').grid(row=0, column=1, sticky='news')
        ttk.Label(self.frame, text='Label 3', background='light green').grid(row=0, column=2, sticky='news')
        ttk.Label(self.frame, text='Label 4', background='pink').grid(row=0, column=3, sticky='news')

class SizeNotifier:
    def __init__(self, window, size_dict):
        self.window = window

        # sort the dictionary using dict comprehension
        self.size_dict = {key: value for key, value in sorted(size_dict.items())}

        self.current_min_size = None
        self.window.update()

        self.window.bind('<Configure>',self.check_sizes)

        min_height = self.window.winfo_height()
        min_width = list(self.size_dict)[0]
        self.window.minsize(min_width, min_height)

    def check_sizes(self,event):
        if event.widget == self.window:
            window_width = event.width
            checked_size = None

            for min_size in self.size_dict:
                delta = window_width - min_size
                if delta >= 0:
                    checked_size = min_size
            
            if checked_size != self.current_min_size:
                self.current_min_size = checked_size
                self.size_dict[self.current_min_size]()




app = App((400, 300))
