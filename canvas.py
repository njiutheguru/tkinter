import tkinter as tk
from tkinter import ttk 

# setup
window = tk.Tk()
window.geometry('600x400')
window.title('Canvas')
# canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack()
# canvas rectangle.. 
# canvas.create_rectangle((20,10,150,200),fill='red', width=10,dash=(4,1), outline='green')
# canvas.create_oval(200, 5, 300, 100, fill='green')
# canvas.create_arc((200, 5, 300, 100), fill='red', start=45, extent=135, style=tk.CHORD,outline='red', width=1)
# canvas.create_line((4,4,4,200), fill='blue', width=20)
# # canvas create polygon
# canvas.create_polygon((3,150, 50,200, 100,150, 80,100, 30,70), fill='green')

# Creating canvas create
# canvas.create_text((100, 200), text="this is text in a canvas", fill='green', width=100)

# canvas.create_window((150, 100), window=ttk.Button(window, text='Button inside Canvas'))
# # Exercise Use event binding to create a basic paint app
def draw_on_canvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brush_size/2,
                         y - brush_size/2,
                           x + brush_size/2,
                             y + brush_size/2), fill='black', width=2)


def brush_size_adjust(event):
    global brush_size
    if event.delta > 0:
        brush_size += 4
    else: 
        brush_size -= 4
    brush_size = max(0, min(brush_size, 50))

brush_size = 2
canvas.bind('<Motion>', draw_on_canvas)
canvas.bind('<MouseWheel>', brush_size_adjust)


# run the app
window.mainloop()