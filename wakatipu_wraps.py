from tkinter import *

class Wraps:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self, parent):
        self.wrap_menu = [
            Wraps("Spicey", 7.00),
            Wraps("Chicken", 6.00),
            Wraps("Steak", 7.50),
            Wraps("Desert", 6.50)
        ]

        self.wrap_names = []
        self.wrap_prices = []
        for wrap in self.wrap_menu:
            self.wrap_names.append(wrap.name)
        for wrap in self.wrap_menu:
            self.wrap_prices.append(wrap.price)
    
        parent.title("Wakatipu Wraps")
        parent.geometry("600x400")
        parent.configure(padx=20, pady=20)

        font_title = ("Helvetica", 16, "bold")
        font_mini_title = ("Helvetica", 14, "bold")
        font_everything = ("Helvetica", 11)
        self.current_item = 1
        self.display_item_num = "Add Item 1:"
        self.selected_item = StringVar()
 
        self.ordering_frame = Frame(parent)
        self.current_items_frame = Frame(parent)
        self.history_frame = Frame(parent)

        self.ordering_frame.grid(row=0, column=0)
        self.current_items_frame.grid(row=0, column=1, sticky=N, padx=10, pady=25)


        # Ordering frame content
        self.label_title = Label(self.ordering_frame, text="Create Order:", font=font_title)
        self.label_add_item = Label(self.ordering_frame, text=self.display_item_num, font=font_mini_title)

        self.label_item = Label(self.ordering_frame, text="What wrap would you like:", font=font_everything)
        self.item_dropdown = OptionMenu(self.ordering_frame, self.selected_item, *self.wrap_names)

        self.label_how_many = Label(self.ordering_frame, text="Amount of item:", font=font_everything)
        self.number_of_items = Entry(self.ordering_frame, width=10)

        self.button_add_item = Button(self.ordering_frame, text="Add Item", command=self.adding_item, font=font_everything)

        self.label_complete_order = Label(self.ordering_frame, text="Completing order:",font=font_mini_title)

        self.name_entry_label = Label(self.ordering_frame, text="Name:", font=font_everything)
        self.name_entry = Entry(self.ordering_frame, width=45)
        
        self.button_complete_order = Button(self.ordering_frame, text="Place Order", font=font_everything)

        # Ordering frame packing
        self.label_title.pack(anchor=W)
        self.label_add_item.pack(anchor=W, padx=(10))
        self.label_item.pack(anchor=W, padx=(10))
        self.item_dropdown.pack(anchor=W, padx=(10))
        self.label_how_many.pack(anchor=W, padx=(10))
        self.number_of_items.pack(anchor=W, padx=(10))
        self.button_add_item.pack(anchor=E, padx=(10), pady=(10))
        self.label_complete_order.pack(anchor=W, padx=(10))
        self.name_entry_label.pack(anchor=W, padx=(10))
        self.name_entry.pack(anchor=W, padx=(10))
        self.button_complete_order.pack(anchor=E, padx=(10), pady=(10))

        # Current items frame content
        self.items_listbox = Listbox(self.current_items_frame, width=40, height=15, bd=2, bg ="white", relief="sunken")
        self.label_all_items = Label(self.current_items_frame, text="Current Items:", font=font_mini_title)
    

        # Current items packing
        self.label_all_items.pack(anchor=W, padx=(10))
        self.items_listbox.pack(anchor=W, padx=(10))


    def adding_item(self):
        item_order = ("Item " + str(self.current_item) + ": " + self.number_of_items.get() + "x " + self.selected_item.get() + " Wraps")
        self.items_listbox.insert(END, item_order)
            
        self.item_number()


    def item_number(self):
        """This function increases the item number, displaying the current number of item in label_add_item"""
        self.current_item += 1
        self.display_item_num = ("Add Item " + str(self.current_item) + ":")
        self.label_add_item.config(text=self.display_item_num)




if __name__ == "__main__":
    root = Tk()
    root.title("Wakatipu Wraps")
    Menu(root)
    root.mainloop()