import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

class App(ctk.CTk):
    def __init__(self, title, size):
        # main setup
         super().__init__()
         self.title(title)
         self.geometry(f'{size[0]}x{size[1]}')
         self.minsize(size[0], size[1])

         # widgets
         self.menu = Menu(self)
         self.main = Main(self)

         # run
         self.mainloop()


class Menu(ctk.CTkFrame):
     def __init__(self, parent):
          super().__init__(parent)
        #   ttk.Label(self, background='red').pack(expand=True, fill='both')
          self.place(x=0,y=0, relwidth=0.3, relheight=1)
          self.create_widgets()
    
     def create_widgets(self):
          # menu widgets 
        menu_button1 = ctk.CTkButton(self, text='Button 1')
        menu_button2 = ctk.CTkButton(self, text='Button 2')
        menu_button3 = ctk.CTkButton(self, text='Button 3')

        menu_slider1 = ctk.CTkSlider(self, orientation='vertical', width=20)
        menu_slider2 = ctk.CTkSlider(self, orientation='vertical', width=20)
 
        # toggle widgets
        toggle_frame = ctk.CTkFrame(self)
        menu_toggle1 = ctk.CTkCheckBox(toggle_frame, text='Check 1')
        menu_toggle2 = ctk.CTkCheckBox(toggle_frame, text='Check 2')

        # entry widget
        entry = ctk.CTkEntry(self)

        # menu layout
        self.columnconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure((0,1,2,3,4), weight=1, uniform='a')

        menu_button1.grid(row=0, column=0, sticky='nswe', columnspan=2, padx=10, pady=10)
        menu_button2.grid(row=0, column=2, sticky='nswe', padx=10, pady=10)
        menu_button3.grid(row=1, column=0, sticky='nswe', columnspan=3, padx=10, pady=10)

        # place the menu sliders
        menu_slider1.grid(row=2, column=0, rowspan=2, sticky='ns', pady=20)
        menu_slider2.grid(row=2, column=2, rowspan=2, sticky='ns', pady=20)

        # toggle layout
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nsew', pady=10)
        menu_toggle1.pack(side='left',expand=True, pady=10)
        menu_toggle2.pack(side='left',expand=True, pady=10)

        # entry layout 
        entry.place(relx=0.5, rely=0.96, relwidth=0.9, anchor='center')

    #  def create_layout(self):
         
class Main(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, rely=0, relwidth=0.7, relheight=1)
        
        Entry(self, 'Label 1', 'Button 1', 'aqua')
        Entry(self, 'Label 2', 'Button 2', 'light green')

        

        # exercise Turn the entry frame with its children ito a separate class. You should be able to set the color, the label text and the button text via the arguments


class Entry(ctk.CTkFrame):
    def __init__(self, parent, label_text, button_text, label_background):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text=label_text)
        button = ctk.CTkButton(self, text=button_text)

        label.pack(expand=True, fill='both')
        button.pack(expand=True, fill='both', pady=10)
        self.pack(side='left', expand=True, fill='both', padx=20, pady=20)


App('Class Based App', (600,600))