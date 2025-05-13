from tkinter import *
from tkinter import messagebox

class Wraps:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Menu:
    def __init__(self, parent):
        # Menu
        self.wrap_menu = [
            Wraps("Spicey", 7.99),
            Wraps("Chicken", 5.99),
            Wraps("Steak", 7.75),
            Wraps("Desert", 6.50)
            ]

        self.wrap_names = []
        for wrap in self.wrap_menu:
            self.wrap_names.append(wrap.name)

        # Window Setup
        parent.title("Wakatipu Wraps")
        parent.geometry("630x440")
        parent.configure(padx=20, pady=20)

        # Fonts + Colours
        font_title = ("Verdana", 18, "bold")
        font_mini_title = ("Verdana", 14, "bold")
        font_default = ("Verdana", 11)
        font_listbox = ("Verdana", 9)

        frame_colour = "#ffffff"
        button_frame_bg = "#D62828"
        add_button_bg = "#66CDAA"
        order_button_bg = "#0077B6"

        # Variables
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

        # Frames
        self.ordering_frame = Frame(parent, bg=frame_colour, relief='groove', bd= 2)
        self.current_items_frame = Frame(parent, bg=frame_colour, relief="groove", bd= 2)
        self.previous_orders_frame = Frame(parent, bg=frame_colour, relief="groove", bd=2)

        self.ordering_frame.grid(row=0, column=0, sticky= N)
        self.current_items_frame.grid(row=0, column=1, sticky= N, padx=10, pady=0)

        # Ordering frame content
        self.label_title = Label(self.ordering_frame, text="Create Order", font=font_title, bg=frame_colour)
        self.label_title.pack(anchor=N)

        self.label_add_item = Label(self.ordering_frame, text=self.display_item_num, font=font_mini_title, bg=frame_colour)
        self.label_add_item.pack(anchor=W, padx=(5))

        self.label_item = Label(self.ordering_frame, text="What wrap would you like:", font=font_default, bg=frame_colour)
        self.label_item.pack(anchor=W, padx=(10))

        self.item_dropdown = OptionMenu(self.ordering_frame, self.selected_item, *self.wrap_names, command=self.update_price_label)
        self.item_dropdown.config(width=10)
        self.item_dropdown.pack(anchor=W, padx=(10))

        self.label_items_price = Label(self.ordering_frame, text=self.displayed_price, font=font_default, bg=frame_colour)
        self.label_items_price.pack(anchor=W, padx=(10))

        self.label_how_many = Label(self.ordering_frame, text="Amount of item:", font=font_default, bg=frame_colour)
        self.label_how_many.pack(anchor=W, padx=(10))

        self.number_of_items = Entry(self.ordering_frame, width=3, textvariable=self.quantity_var, relief="solid", font=font_default)
        self.number_of_items.pack(anchor=W, padx=(14))

        self.button_add_item = Button(self.ordering_frame, text="Add Item", command=self.adding_item, font=font_default, bg=add_button_bg, fg=frame_colour)
        self.button_add_item.pack(anchor=E, padx=(10), pady=(10))

        self.label_complete_order = Label(self.ordering_frame, text="Completing order:",font=font_mini_title, bg=frame_colour)
        self.label_complete_order.pack(anchor=W, padx=(10))

        self.name_entry_label = Label(self.ordering_frame, text="Name:", font=font_default, bg=frame_colour)
        self.name_entry_label.pack(anchor=W, padx=(10))

        self.name_entry = Entry(self.ordering_frame, width=25, textvariable=self.name_var, relief="solid", font=font_default)
        self.name_entry.pack(anchor=W, padx=(14))
        
        self.button_complete_order = Button(self.ordering_frame, text="Place Order", font=font_default, command=self.place_order, fg=frame_colour, bg=order_button_bg)
        self.button_complete_order.pack(anchor=E, padx=(10), pady=(5))

        self.check_order_history = Button(self.ordering_frame, text ="Previous Orders", font=font_default, command=self.order_history, bg= button_frame_bg, fg=frame_colour)
        self.check_order_history.pack(anchor=E, padx=(10), pady=(3))

        # Current items frame content
        self.items_listbox = Listbox(self.current_items_frame, width=32, height=18, bd=3, bg=frame_colour, relief="sunken", font=font_listbox)
        self.items_listbox.pack(anchor=W, padx=(10), pady=(3))

        self.label_all_items = Label(self.current_items_frame, text="Current Items", font=font_title, bg=frame_colour)
        self.label_all_items.pack(anchor=N)

        self.label_order_price = Label(self.current_items_frame, text=self.displayed_order_price, font=font_default, bg=frame_colour)
        self.label_order_price.pack(anchor=W, padx=(10), pady=(3))

        # Orders frame content
        self.label_previous_orders = Label(self.previous_orders_frame, text="Previous Orders", font=font_title, bg=frame_colour)
        self.label_previous_orders.pack(anchor=N)

        self.prev_orders_listbox = Listbox(self.previous_orders_frame, width=35, height=21, bd=3, bg=frame_colour, relief="sunken", font=font_listbox)
        self.prev_orders_listbox.pack(anchor=W, padx=(10), pady=(3))

        self.back_to_order = Button(self.previous_orders_frame, text="Return To Ordering", command=self.return_to_order, font=font_default, bg= button_frame_bg, fg=frame_colour)
        self.back_to_order.pack(anchor=E, padx=(10), pady=(3))

    # --- Functions ---

    def adding_item(self):
        """
        Adds the selected wrap with its quantity to the current order.
        Displays the item to the listbox with the total item price.
        Validates user input, showing error messages for invalid selections or quantities.
        Updates the order list, total price, and item number.
        """
        if self.selected_item.get() == "Select Wrap":
            messagebox.showerror("No Wrap Selected", "Please select a wrap from the dropdown menu.")
            return
        
        try:
            if int(self.number_of_items.get()) < 1 or int(self.number_of_items.get()) > 99:
                messagebox.showerror("Invalid Item Quantity", "Please enter a number between 1-99 for the quantity")
                self.quantity_var.set("")
                return
        except ValueError:
            messagebox.showerror("Invalid Item Quantity", "Please enter a whole number for the quantity")
            self.quantity_var.set("")
            return
        
        self.item_price_calc()
        item_order = (" Item " + str(self.current_item) + ": " + self.number_of_items.get() + "x " + self.selected_item.get() + " Wraps, $" + str(format(self.items_value, ".2f")))
        self.items_listbox.insert(END, item_order)
        self.current_item += 1
        self.item_number()
        self.order_price_calc()
        self.reset_add_item()


    def reset_add_item(self):
        """
        Resets the current item selection, quantity and price to default values.
        """
        self.selected_item.set("Select Wrap")
        self.label_items_price.config(text="Price: $0.00")
        self.current_item_price = 0.00
        self.quantity_var.set("")


    def reset_order(self):
        """
        Resets the entire order to its initial state:
        Resets item listbox, total prices, item number and name entry.
        """
        self.reset_add_item()
        self.items_listbox.delete(0, END)
        self.order_total_price.clear()
        self.order_price_calc()
        self.name_var.set("")
        self.current_item = 1
        self.item_number()


    def place_order(self):
        """
        Validates the name input.
        Finalizes and records the current order to the order listbox.
        """
        name = self.name_entry.get().strip()
        if name == "":
            messagebox.showerror("Invalid Name", "Name field cannot be empty.")
            self.name_var.set("")
            return
        if len(self.order_total_price) == 0:
            messagebox.showerror("Empty Order", "Please add items to your order.")
            return
        order_info = (" Name: " + self.name_entry.get() + ", " + self.displayed_order_price + ".")
        self.prev_orders_listbox.insert(END, order_info)
        messagebox.showinfo("Order Placed", order_info)
        self.reset_order()
        self.order_history()


    def item_price_calc(self):
        """
        Calculates total price by multiplying the selected item based by its quantity.
        Appends the value to the order price list.
        """
        quantity = int(self.number_of_items.get())
        self.items_value = self.current_item_price * quantity
        self.order_total_price.append(self.items_value)


    def order_price_calc(self):
        """
        Sums the price list.
        Updates the displayed order price.
        """
        self.order_price = sum(self.order_total_price)
        self.displayed_order_price = "Order Price: $" + format(self.order_price, ".2f")
        self.label_order_price.config(text=self.displayed_order_price)


    def item_number(self):
        """
        Updates the label that shows the current item number.
        """
        self.display_item_num = ("Add Item " + str(self.current_item) + ":")
        self.label_add_item.config(text=self.display_item_num)


    def get_price(self, name):
        """
        Returns the price of a wrap based on its name.
        """
        for wrap in self.wrap_menu:
            if wrap.name == name:
                return wrap.price
            
    
    def update_price_label(self, selection):
        """
        Changes the price label shown when a wrap is selected.
        """
        self.current_item_price = self.get_price(selection)
        self.displayed_price = "Price: $" + format(self.current_item_price, ".2f")
        self.label_items_price.config(text=self.displayed_price)


    def return_to_order(self):
        """
        Grids the frames for the main ordering screen, hides the previous orders frame.
        """
        self.previous_orders_frame.grid_forget()
        self.ordering_frame.grid(row=0, column=0, sticky= N)
        self.current_items_frame.grid(row=0, column=1, sticky= N, padx=10, pady=0)


    def order_history(self):
        """
        Grids the previous orders frame, hides the frames for the main ordering screen.
        """
        self.ordering_frame.grid_forget()
        self.current_items_frame.grid_forget()
        self.previous_orders_frame.grid()


if __name__ == "__main__":
    root = Tk()
    root.title("Wakatipu Wraps")
    Menu(root)
    root.mainloop()