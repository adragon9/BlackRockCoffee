import runpy
import tkinter as tk


def launch_queue():
    runpy.run_module("Queue")


if __name__ == "__main__":
    # The current set up for these windows allows for multiple queues being up at once
    # guess we could call it a feature?
    root = tk.Tk()
    root.title("Black Rock Coffee App")

    r_height = 50
    r_width = 150

    root.configure(padx=r_width, pady=r_height)

    place_order_button = tk.Button(root, text="Run Queue", command=launch_queue)
    place_order_button.pack()

    root.mainloop()
