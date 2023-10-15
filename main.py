import runpy
import tkinter as tk
from Classes import CustButton


# This runs the queue script. How modularized.
def open_queue():
    runpy.run_module("Queue")


if __name__ == "__main__":
    # I have set up the main window to be able to spawn other windows that can take exclusive control
    # When making a new window in a different script be sure to use tk.TopLevel() instead of tk.Tk()
    splash = tk.Tk()

    splash.title("Black Rock")
    splash.iconbitmap("img/coffee-ico.ico")

    # Come now, must the customer be able to control window size?
    splash.resizable(width=False, height=False)
    HEIGHT = 320
    WIDTH = HEIGHT * 1.5

    # The use of a canvas provides more precise control over object position
    canvas = tk.Canvas(splash, height=HEIGHT, width=WIDTH)
    canvas.pack()

    # The CustButton function must be initialized with the .initialize_button() function or the button will not appear
    open_queue_btn = CustButton(splash, "Open Queue", x=0, y=0, pack=False, command=open_queue)

    # The .initialize_button() function returns a tkinter button, so it can be used with tkinter functions, such as
    # create window
    button_window_1 = canvas.create_window((WIDTH / 2), (HEIGHT / 2) + 120, anchor='center', window=open_queue_btn.initialize_button())

    splash.mainloop()