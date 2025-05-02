from tkinter import *

class wraps:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class menu:
    def __init__(self, parent):

        parent.title("Wakatipu Wraps")
        parent.geometry("600x400")
        parent.configure(padx=20, pady=20)

        font_title = ("Ariel", 16)
        font_mini_title = ("Ariel", 14)
        font_everything = ("Ariel", 11)
        self.current_item = 1
        self.display_item_num = "Add Item 1:"
 
        self.ordering_frame = Frame(parent)
        self.current_items_frame = Frame(parent, bg="white", bd=2, relief='sunken')
        self.history_frame = Frame(parent)

        self.ordering_frame.grid(row=0, column=0)
        self.current_items_frame.grid(row=0, column=1, sticky=N, padx=10, pady=25)


        # Ordering frame content
        self.label_title = Label(self.ordering_frame, text="Create Order:", font=font_title)
        self.label_add_item = Label(self.ordering_frame, text=self.display_item_num, font=font_mini_title)
        self.label_item = Label (self.ordering_frame, text="What item would you like:", font=font_everything)
        self.label_how_many = Label(self.ordering_frame, text="Amount of item:", font=font_everything)
        self.number_of_items = Entry(self.ordering_frame, width=10)
        self.button_add_item = Button(self.ordering_frame, text="Add Item", command=self.item_number, font=font_everything)
        self.label_complete_order = Label(self.ordering_frame, text="Completing order:",font=font_mini_title)
        self.name_entry_label = Label(self.ordering_frame, text="Name:", font=font_everything)
        self.name_entry = Entry(self.ordering_frame, width=45)
        self.button_complete_order = Button(self.ordering_frame, text="Place Order", font=font_everything)

        # Ordering frame packing
        self.label_title.pack(anchor=W)
        self.label_add_item.pack(anchor=W, padx=(10))
        self.label_item.pack(anchor=W, padx=(10))
        self.label_how_many.pack(anchor=W, padx=(10))
        self.number_of_items.pack(anchor=W, padx=(10))
        self.button_add_item.pack(anchor=E, padx=(10), pady=(10))
        self.label_complete_order.pack(anchor=W, padx=(10))
        self.name_entry_label.pack(anchor=W, padx=(10))
        self.name_entry.pack(anchor=W, padx=(10))
        self.button_complete_order.pack(anchor=E, padx=(10), pady=(10))

        # Current items frame content
        self.label_all_items = Label(self.current_items_frame, text="Current Items:", font=font_mini_title, bg="white")

        # Current items packing
        self.label_all_items.pack(anchor=W, padx=(10))



    def item_number(self):
        """This function increases the item number, displaying the current number of item in label_add_item"""
        self.current_item += 1
        self.display_item_num = ("Add Item " + str(self.current_item) + ":")
        self.label_add_item.config(text=self.display_item_num)




if __name__ == "__main__":
    root = Tk()
    root.title("Wakatipu Wraps")
    menu(root)
    root.mainloop()