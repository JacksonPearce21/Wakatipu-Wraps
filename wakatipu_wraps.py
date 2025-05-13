from tkinter import *
from tkinter import messagebox

class Wraps:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self, parent):
        self.wrap_menu = [
            Wraps("Spicey", 7.99),
            Wraps("Chicken", 5.99),
            Wraps("Steak", 7.75),
            Wraps("Desert", 6.50)
            ]

        self.wrap_names = []
        self.wrap_prices = []
        for wrap in self.wrap_menu:
            self.wrap_names.append(wrap.name)


        parent.title("Wakatipu Wraps")
        parent.geometry("600x425")
        parent.configure(padx=20, pady=20)

        font_title = ("Verdana", 18, "bold")
        font_mini_title = ("Verdana", 14, "bold")
        font_default = ("Verdana", 11)

        self.current_item = 1
        self.display_item_num = "Add Item 1:"

        self.quantity_var = StringVar()
        self.name_var = StringVar()
        self.selected_item = StringVar()
        self.selected_item.set("Select Wrap")

        self.current_item_price = 0.00
        self.displayed_price = "Price: $" + format(self.current_item_price, ".2f")

        self.order_total_price = []
        self.order_price = sum(self.order_total_price)
        self.displayed_order_price = "Order Price: $" + format(self.order_price, ".2f")
 
        self.ordering_frame = Frame(parent)
        self.current_items_frame = Frame(parent)

        self.ordering_frame.grid(row=0, column=0)
        self.current_items_frame.grid(row=0, column=1, sticky=N, padx=10, pady=25)

        self.previous_orders_frame = Frame(parent)

        # Ordering frame content
        self.label_title = Label(self.ordering_frame, text="Create Order:", font=font_title)
        self.label_add_item = Label(self.ordering_frame, text=self.display_item_num, font=font_mini_title)

        self.label_item = Label(self.ordering_frame, text="What wrap would you like:", font=font_default)
        self.item_dropdown = OptionMenu(self.ordering_frame, self.selected_item, *self.wrap_names, command=self.update_price_label)
        self.item_dropdown.config(width=10)
        self.label_items_price = Label(self.ordering_frame, text=self.displayed_price, font=font_default)

        self.label_how_many = Label(self.ordering_frame, text="Amount of item:", font=font_default)
        self.number_of_items = Entry(self.ordering_frame, width=4, textvariable=self.quantity_var)

        self.button_add_item = Button(self.ordering_frame, text="Add Item", command=self.adding_item, font=font_default)

        self.label_complete_order = Label(self.ordering_frame, text="Completing order:",font=font_mini_title)

        self.name_entry_label = Label(self.ordering_frame, text="Name:", font=font_default)
        self.name_entry = Entry(self.ordering_frame, width=45, textvariable=self.name_var)
        
        self.button_complete_order = Button(self.ordering_frame, text="Place Order", font=font_default, command=self.place_order)
        self.check_order_history = Button(self.ordering_frame, text ="Previous Orders", font=font_default, command=self.order_history)

        # Ordering frame packing
        self.label_title.pack(anchor=W)
        self.label_add_item.pack(anchor=W, padx=(10))
        self.label_item.pack(anchor=W, padx=(10))
        self.item_dropdown.pack(anchor=W, padx=(10))
        self.label_items_price.pack(anchor=W, padx=(10))
        self.label_how_many.pack(anchor=W, padx=(10))
        self.number_of_items.pack(anchor=W, padx=(10))
        self.button_add_item.pack(anchor=E, padx=(10), pady=(10))
        self.label_complete_order.pack(anchor=W, padx=(10))
        self.name_entry_label.pack(anchor=W, padx=(10))
        self.name_entry.pack(anchor=W, padx=(10))
        self.button_complete_order.pack(anchor=E, padx=(10), pady=(10))
        self.check_order_history.pack(anchor=E, padx=(10), pady=(5))

        # Current items frame content
        self.items_listbox = Listbox(self.current_items_frame, width=40, height=15, bd=2, bg ="white", relief="sunken")
        self.label_all_items = Label(self.current_items_frame, text="Current Items:", font=font_mini_title)
        self.label_order_price = Label(self.current_items_frame, text=self.displayed_order_price, font=font_default)
    
        # Current items packing
        self.label_all_items.pack(anchor=W, padx=(10))
        self.items_listbox.pack(anchor=W, padx=(10))
        self.label_order_price.pack(anchor=W, padx=(10))

        # Orders frame content
        self.label_previous_orders = Label(self.previous_orders_frame, text="Previous Orders:", font=font_title)
        self.prev_orders_listbox = Listbox(self.previous_orders_frame, width=40, height=15, bd=2, bg ="white", relief="sunken")
        self.back_to_order = Button(self.previous_orders_frame, text="Return To Ordering", command=self.return_to_order, font=font_default)


        # Orders packing
        self.label_previous_orders.pack()
        self.prev_orders_listbox.pack()
        self.back_to_order.pack()



    def adding_item(self):
        """"""
        if self.selected_item.get() == "Select Wrap":
            messagebox.showerror("No Wrap Selected", "Please select a wrap from the dropdown menu.")
            return
        try:
            if int(self.number_of_items.get()) < 1:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Item Quantity", "Please enter a positive whole number for the quantity")
            self.quantity_var.set("")
            return
        self.item_price_calc()
        item_order = ("Item " + str(self.current_item) + ": " + self.number_of_items.get() + "x " + self.selected_item.get() + " Wraps, $" + str(format(self.items_value, ".2f")))
        self.items_listbox.insert(END, item_order)
        self.current_item += 1
        self.item_number()
        self.order_price_calc()
        self.reset_add_item()


    def reset_add_item(self):
        """"""
        self.selected_item.set("Select Wrap")
        self.label_items_price.config(text="Price: $0.00")
        self.current_item_price = 0.00
        self.quantity_var.set("")


    def reset_order(self):
        """"""
        self.reset_add_item()
        self.items_listbox.delete(0, END)
        self.order_total_price.clear()
        self.order_price_calc()
        self.name_var.set("")
        self.current_item = 1
        self.item_number()


    def place_order(self):
        """"""
        name = self.name_entry.get().strip()
        if name == "":
            messagebox.showerror("Invalid Name", "Name field cannot be empty.")
            self.name_var.set("")
            return
        if len(self.order_total_price) == 0:
            messagebox.showerror("Empty Order", "Please add items to your order.")
            return
        order_info = ("Name: " + self.name_entry.get() + ", " + self.displayed_order_price + ".")
        self.prev_orders_listbox.insert(END, order_info)
        messagebox.showinfo("Order Placed", order_info)
        self.reset_order()
        self.order_history()


    def item_price_calc(self):
        """"""
        quantity = int(self.number_of_items.get())
        self.items_value = self.current_item_price * quantity
        self.order_total_price.append(self.items_value)


    def order_price_calc(self):
        """"""
        self.order_price = sum(self.order_total_price)
        self.displayed_order_price = "Order Price: $" + format(self.order_price, ".2f")
        self.label_order_price.config(text=self.displayed_order_price)


    def item_number(self):
        """This function increases the item number, displaying the current number of item in label_add_item"""
        self.display_item_num = ("Add Item " + str(self.current_item) + ":")
        self.label_add_item.config(text=self.display_item_num)


    def get_price(self, name):
        """"""
        for wrap in self.wrap_menu:
            if wrap.name == name:
                return wrap.price
            
    
    def update_price_label(self, selection):
        """"""
        self.current_item_price = self.get_price(selection)
        self.displayed_price = "Price: $" + format(self.current_item_price, ".2f")
        self.label_items_price.config(text=self.displayed_price)


    def return_to_order(self):
        """"""
        self.previous_orders_frame.grid_forget()
        self.ordering_frame.grid(row=0, column=0)
        self.current_items_frame.grid(row=0, column=1, sticky=N, padx=10, pady=25)


    def order_history(self):
        """"""
        self.ordering_frame.grid_forget()
        self.current_items_frame.grid_forget()
        self.previous_orders_frame.grid()


if __name__ == "__main__":
    root = Tk()
    root.title("Wakatipu Wraps")
    Menu(root)
    root.mainloop()