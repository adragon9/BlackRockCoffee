import tkinter as tk


class Order:
    def __init__(self, order_num, coffee_name, coffee_temp, special_requests, coffee_price):
        try:
            self.order_num = int(order_num)
        except TypeError:
            self.order_num = "error_type_required INT"

        try:
            self.coffee_name = str(coffee_name)
        except TypeError:
            self.coffee_name = "error_type_required STRING"

        try:
            self.coffee_temp = str(coffee_temp)
        except TypeError:
            self.coffee_temp = "error_type_required STRING"

        self.special_requests = special_requests

        try:
            self.coffee_price = float(coffee_price)
        except TypeError:
            self.coffee_price = "error_type_required NUMBER"


"""
Contains entry box objects for easier implementation and access
"""


class EntryBox(tk.Tk):
    """
    Allows for one to make an entry box by inserting the master window, width, grid row, and grid column
    """
    def __init__(self, master=None, width=None, y=None, x=None, relief=None, font=None):
        """
        :param master:
        :param width:
        :param y:
        :param x:
        :param relief:
        :param font:
        """
        self.entryBox = None
        self.master = master
        self.width = width
        self.x = x
        self.y = y
        self.relief = relief
        self.font = font

    def initialize_box(self):
        """
        initialize_box() Initializes the entry box by calling tk's entry box function, and grid function
        Relief types: raised, sunken, solid, flat, ridge, groove
        """
        self.entryBox = tk.Entry(self.master, width=self.width, relief=self.relief, font=self.font,
                                 background="#f0f0f0")
        # self.entryBox.grid(row=self.row, column=self.column)
        self.entryBox.place(x=self.x, y=self.y)

        return self.entryBox

    def get_box(self):
        """
        get_data() the entry box for easy access
        """
        # print(self.entryBox.get()) -- debug print
        return self.entryBox


class CustButton(tk.Tk):
    """
    Allows for easy creation of a button accepts:
    master window, text of the button, width of the button, its grid row and column, the buttons callback command,
    and the buttons padx and pady
    """

    def __init__(self, master=None, text=None, width=None, y=None, x=None, command=None, padx=None, pady=None, pack=False):
        self.button = None
        self.master = master
        self.text = text
        self.width = width
        self.y = y
        self.x = x
        self.padx = padx
        self.pady = pady
        self.command = command
        self.pack = bool(pack)

    def initialize_button(self):
        """
        initialize_button: initializes the button with the passed values
        """
        self.button = tk.Button(self.master, text=self.text, width=self.width, command=self.command)
        if self.pack is True:
            self.button.pack()
        else:
            self.button.place(x=self.x, y=self.y)
        # self.button.grid(row=self.row, column=self.column, padx=self.padx, pady=self.pady)
        return self.button

    def initialize_button_grid(self, gridx=0, gridy=0):
        """
        initialize_button_grid: initializes the button with a grid system

        :param gridx:
        :param gridy:
        :return:
        """
        self.button = tk.Button(self.master, text=self.text, command=self.command)
        self.button.grid_configure(column=gridx, row=gridy)
