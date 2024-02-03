# starts at 12:17

import customtkinter as ctk

# catching exceptions for different os
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

app = ctk.CTk(fg_color='aqua')
app.geometry('300x200')

# change the title bar color
try:
    HWND = windll.user32.GetParent(app.winfo_id())
    title_bar_color = 0x00FF0000
    title_text_color = 0x0000FF99
    print(type(title_bar_color))
    windll.dwmapi.DwmSetWindowAttribute(HWND,
                                        35,
                                        byref(c_int(title_bar_color)),
                                        sizeof(c_int))

    windll.dwmapi.DwmSetWindowAttribute(HWND,
                                        36,
                                        byref(c_int(title_text_color)),
                                        sizeof(c_int))
except:
    pass

# run
if __name__ == '__main__':
    app.mainloop()

