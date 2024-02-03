import customtkinter as ctk
from random import choice

window = ctk.CTk()
window.title('Animated Widgets')
window.geometry('600x400')

class SliderPanel(ctk.CTkFrame):
    def __init__(self, parent, start_pos, end_pos):
        super().__init__(parent)
        # general attributes
        self.start_pos = start_pos + 0.04
        self.end_pos = end_pos - 0.03
        self.width = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True
        # layout
        self.place(relx=self.start_pos, rely =0.05, relwidth = self.width, relheight =0.9)

    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()
    
    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos -= 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False
        
    def animate_backward(self):
        if self.pos < self.start_pos:
            self.pos += 0.008
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(10, self.animate_backward)
        else:
            self.in_start_pos = True
            

# exercise
# animate the button and move it to the right side of the window
            
def move_b():
    global button_x
    button_x += 0.001
    if button_x <= 0.88:
        button.place(relx=button_x, rely=0.5, anchor='center')
        window.after(1, move_b)


def move_btn():
    global button_x
    button_x += 0.05
    button.place(relx=button_x, rely=0.5, anchor='center')
    # colors = ['red', 'pink', 'yellow', 'aqua', 'black', 'white', 'green', 'blue']

    # color = choice(colors)
    # button.configure(fg_color=color)

def infinite_print():
    global button_x
    button_x += 0.5
    if button_x < 10:
        print(button_x)
        print('infinite print')
        window.after(1000, infinite_print)

animated = SliderPanel(window,1.0,0.7)
ctk.CTkLabel(animated, text='Label 1').pack(expand=True, fill='both', pady=10)
ctk.CTkLabel(animated, text='Label 2').pack(expand=True, fill='both', pady=10)
button1 = ctk.CTkButton(animated, text='Button')
button1.pack(expand=True, fill= "both") 
ctk.CTkTextbox(animated).pack(expand=True, fill='both')
# button
button_x = 0.5
button = ctk.CTkButton(window, 
                     text='Toggle sidebar',
                     command=animated.animate)
button.place(relx=button_x,
              rely=0.5,
                # relheight=button_x, 
                anchor='center')

# run the app
if __name__ == "__main__":
    window.mainloop()