import tkinter as tk
from tkinter import ttk

# create a scrollbar
 
# create the class canvas
class ListFrame(ttk.Frame):
    def __init__(self, parent, text_data, item_height):
        super().__init__(master=parent)
        self.pack(expand=True, fill='both')

        # widget data
        self.text_data = text_data
        self.item_number = len(text_data)
        self.list_height = self.item_number * item_height

        # canvas
        self.canvas = tk.Canvas(self, background='aqua', scrollregion=(0,0,500,self.list_height))
        self.canvas.pack(expand=True, fill='both')

        # display frame
        self.frame = ttk.Frame(self)
        for index, item in enumerate(self.text_data):
            self.create_item(index, item).pack(expand=True, fill='both', padx=50, pady=10)

        # self.canvas.create_window((0,0), 
        #                           window=self.frame, anchor='nw', width=500, 
        #                           height=self.list_height)
            
        # create a scroll bar here before events
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne')

        # create an event here
        self.canvas.bind_all('<MouseWheel>',lambda event: self.canvas.yview_scroll(int(event.delta / 60), 'units'))
        self.bind('<Configure>', self.update_size)

    def update_size(self, event):
        if self.list_height >= self.winfo_height():
            height = self.list_height
            self.canvas.bind_all('<MouseWheel>',lambda event: self.canvas.yview_scroll(int(event.delta / 60), 'units'))
        else:
            height = self.winfo_height()
            self.canvas.unbind_all('<MouseWheel>')

        self.canvas.create_window((0,0),
                                  window=self.frame,
                                  anchor='nw',
                                  width=self.winfo_width(),
                                  height=height)
        
    def create_item(self, index, item):
        frame = ttk.Frame(self.frame)
        # grid layout
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure((0,1,2,3,4), weight=1, uniform='a')

        # widgets
        ttk.Label(frame, text=f'#{index}').grid(row=0, column=0)
        ttk.Label(frame, text=f'{item[0]}').grid(row=0, column=1)
        ttk.Button(frame, text=f'{item[1]}').grid(row=0, column=2, columnspan=3, sticky='news')

        return frame
        

# window 
window = tk.Tk()
window.geometry('500x400')
window.title('Scrolling Widgets')

# # creating a canvas widgets
# canvas = tk.Canvas(window, background='white')
# # place a widget
# canvas.create_window((20, 50), window=ttk.Label(canvas, text='A Label '))
# canvas.pack(expand=True, fill='both')

text_list = [('Label', 'button'), ('thing', 'click'),('third', 'something'),('Label 1', 'button'), ('Label 2','Click 2'),('Button x', "Button x1"), ('Button xx', 'Button X2')]

list_frame = ListFrame(window, text_list, 100)

# run the app
if __name__ == "__main__":
    window.mainloop()

