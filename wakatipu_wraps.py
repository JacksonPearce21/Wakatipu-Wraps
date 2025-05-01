from tkinter import *

class wraps:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class menu:
    def __init__(self, parent):
        parent.title("Wakatipu Wraps")
        parent.geometry("340x300")
        parent.configure(padx=20, pady=20)

        font_title = ("Ariel", 16)
        font_everything = ("Ariel", 12)

        self.ordering_frame = Frame(parent)
        self.history_frame = Frame(parent)





if __name__ == "__main__":
    root = Tk()
    root.title("Wakatipu Wraps")
    menu(root)
    root.mainloop()