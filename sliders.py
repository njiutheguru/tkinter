import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

window = tk.Tk()
window.title('Sliders')
window.geometry('700x600')
# # slider
scale_float = tk.DoubleVar(value=15)
scale = ttk.Scale(window, 
                  command=lambda event: print(scale_float.get()),
                  from_=0,
                  to=25,
                  length=300,
                  orient='horizontal',
                  variable=scale_float)

scale.pack()

# progress bars
progress = ttk.Progressbar(window,
                           variable=scale_float,
                           maximum=25,
                           orient='horizontal',
                           mode='determinate',
                           length=300)
progress.pack(pady=20)
# progress.start(100)
# scrolledtext import from tkinter
scrolled_text = scrolledtext.ScrolledText(window,width=100, height=3)
scrolled_text.pack()
# create a progress that is vertical, starts automatically and also show the progress as a number.
# there should also be a scale slider that is affectd by the progress bar
progress_int = tk.IntVar(value=15)
scale_exercise = ttk.Scale(window, 
                  command=lambda event: print(progress_int.get()),
                  from_=0,
                  to=100,
                  length=300,
                  orient='horizontal',
                  variable=progress_int)

scale_exercise.pack()

# progress bars
progress_exercise = ttk.Progressbar(window,
                           variable=progress_int,
                           maximum=100,
                           mode='determinate',
                           length=300,
                           orient='vertical')
progress_exercise.pack(pady=20)

progress_exercise.start()
label = ttk.Label(window, textvariable=progress_int)
label.pack()
# run the app
window.mainloop()