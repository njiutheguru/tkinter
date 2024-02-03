import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Frames and Parenting')

# frame
frame = ttk.Frame(window, 
                  width=200, 
                  height=200, 
                  borderwidth=10,
                    relief=tk.GROOVE)

frame.pack_propagate(False) # True means that dimensions take the size of frames children
frame.pack(side='left', padx=10)

# master settings
label = ttk.Label(frame, text='Label in Frame')
label.pack()

button = ttk.Button(frame, text='Button in frame')
button.pack()

label_2 = ttk.Label(window, text='Label outside frame')
label_2.pack(side='bottom')
# exercise
# create another frame with a label, a button and an entry and place it to the right of the other widgets.
frame_2 = ttk.Frame(window,
                     width=200,
                       height=100, 
                       borderwidth=10, 
                       relief=tk.GROOVE)
frame_2.pack_propagate(False)
frame_2.pack(side='right', padx=10)
label_exercise = ttk.Label(frame_2, text='Exercise label')
label_exercise.pack()
button_2 = ttk.Button(frame_2, text="Button exercise")
button_2.pack()
entry = ttk.Entry(frame_2)
entry.pack()

# run the app

if __name__=='__main__':
    window.mainloop()