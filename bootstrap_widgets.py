import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame # scrolled frame
from ttkbootstrap.toast import ToastNotification # toast
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry, Floodgauge, Meter

# window
window = ttk.Window(themename='darkly')
window.title('Bootstrap widgets')
# window.geometry('600x400')

# create a scrollable frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand=True, fill='both')

for i in range(100):
    frame = ttk.Frame(scroll_frame)
    ttk.Label(frame, text=f'Label: {i}').pack(fill='x', side='left', pady=10, padx=10)
    ttk.Button(frame, text=f'Button: {i}').pack(fill='x', side='right', pady=10, padx=10)
    frame.pack()


# toast
toast = ToastNotification(title='This is a message title',
                          message='This is the actual message',
                          duration=2000,
                          bootstyle='dark',
                          position=(50, 100, 'nw'))

# toast.show_toast() Function should be called at certain times
ttk.Button(window, text='Show toast', command=toast.show_toast).pack(pady=10)

# create a tooltip
button = ttk.Button(window, text='tooltip button',bootstyle='warning')
button.pack(pady=10)
ToolTip(button, text='This does something', bootstyle='danger-inverse')

# calender
calendar = DateEntry(window)
calendar.pack(pady=10)

ttk.Button(window, text='Get calendar date', command=lambda: print(calendar.entry.get())).pack()

# create a progres -> floodgauge
# create a tk var
progress_int = tk.IntVar(value=50)
progress = ttk.Floodgauge(window, 
                          text='Progress', variable=progress_int,
                          bootstyle='info',
                          mask='Progress {}%')
progress.pack(pady=10, fill='x')
ttk.Scale(window, from_=0, 
          to=100, 
          variable=progress_int).pack()

# creating a meter
meter = ttk.Meter(window,
                  amounttotal=100,
                  amountused=10,
                  interactive=True,
                #   metertype='semi',
                  subtext='Percentage',
                  bootstyle='info')

meter.pack()
# run the app

if __name__ == "__main__":
    window.mainloop()