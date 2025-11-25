# Ahmad Yasin UID: 748007669
# Afsa Farheen Shaik UID: 432000627
# Nahomi Tesfaye Duki UID: 433000292

# Task 1

# Dictionary containing all the available items and their prices

menu = {
    "drinks": {"cola": 5.0, "juice": 7.0},
    "entrees": {"burger": 20.0, "pizza": 25.0},
    "sides": {"fries": 8.0, "salad": 10.0}
}

# Task 2

class Combo:
    __slots__ = ("drink", "entree", "side", "total_price")

    def price(category, key):
        """
        Returns the price of the given item key from a category dictionary.

        If the key is not found, return 0 as the value.
        """
        try:
            return category[key]
        except:
            return 0

    def __init__(self, drink, entree, side, menu):
        """
        Initialize all fields of this class.

        Checks if the items exist in menu dictionary. 

        Sets the value of total_price as the sum of the prices of the given drink, entrée and side.
        """
        if drink in menu["drinks"]:
                self.drink = drink
        else:
            self.drink = ""
            print(f"\nThe drink {drink.capitalize()} isn't in the menu.")
        
        if entree in menu["entrees"]:
                self.entree = entree
        else:
            self.entree = ""
            print(f"The entrée {entree.capitalize()} isn't in the menu.")
        
        if side in menu["sides"]:
            self.side = side
        else:
            self.side = ""
            print(f"The side {side.capitalize()} isn't in the menu.\n")
        
        # Calculating the total price as the sum of the prices of drink, entrée and side.
        
        self.total_price = sum([Combo.price(menu["drinks"], self.drink),
                                Combo.price(menu["entrees"], self.entree),
                                Combo.price(menu["sides"], self.side)])

    def get_total(self):
        return self.total_price

    def display_combo(self):
        """
        Prints the details of the combo.

        Displays the name of item from each category along with the total price.
        """

        print("Combo 1:\n")

        print(f"Drink : {self.drink.capitalize()} | Entrée: {self.entree.capitalize()} | Side: {self.side.capitalize()} \n\n"
              f"Total Combo Price: {self.total_price} AED \n")
        


# Task 3

class Order:
    __slots__ = ("order_id", "combos", "total_amount")

    def __init__(self, order_id, combos = [], total_amount = 0):
        """
        Initialze the fields of this class.
        """

        self.order_id = order_id
        self.combos = combos
        self.total_amount = total_amount

    def add_combo(self, new_combo):
        """
        Appending the combo details to an empty combo dictionary.

        Calculates the total amount using the get_total() method defined in Combo class.
        """

        self.combos.append(new_combo)
        self.total_amount += new_combo.get_total()
    
    def display_receipt(self):
        """
        Displays the order receipt.

        Prints the order ID, combo details and total amount.

        Uses the display_combo() method defined in Combo class to display the details of the combo.
        """
        print(f"Receipt for Order ID: {self.order_id} \n\n"
            f"----------------------------------- \n")
        
        combo = self.combos[0]
        combo.display_combo()

        print(f"-----------------------------------\n\n"
        f"Total Amount: {self.total_amount} AED\n")

# Task 4

def take_order():
    """
    Displays the menu.

    Takes an input of the user's choice of drink, entrée and side. 

    Creates a combo and order using Combo and Order classes respectively.

    The receipt is displayed using the display_receipt() method from the Order class.
    """
    print("\n")
    print("--- Welcome to Eat and Drink ---")
    print("Today's Menu:")
    
    # Prints the menu
    for category in menu: 
        for item in menu[category]:
            price = menu[category][item]
            print(f"{item.capitalize()} - {price} AED")

    print("\nCreate your combo:")

    drink = input("Enter drink: ").lower()
    entree = input("Enter entrée: ").lower()
    side = input("Enter side: ").lower()

    # Creates a Combo object from the user's input
    combo = Combo(drink, entree, side, menu) 

    order = Order(101)  

    # Add the combo to the order
    order.add_combo(combo) 

    print("\nOrder successfully created!\n\n")
    order.display_receipt()

# Defines the main function.
def main():    
    take_order()

# Runs the main function.
if __name__ == "__main__":  
    main()


# Manifesto

"""

This program takes an order from the user and prints the receipt of the order.

Task 1: Done by Ahmad Yasin

Create a dictionary with different categories and the available items of the menu 

Task 2: Done by Ahmad Yasin

Create a class called Combo. Use __slots__ for its attributes. Initialize all its fields. 
Create get_total() method to calculate total price.
Create display_combo() to print the combo details.

Task 3: Done by Afsa Farheen Shaik

Create a class called Order. Use __slots__ for its attributes. Initialize all its fields.
Create add_combo() method to add a Combo object and calculate the total price using get_total() method.
Create display_receipt() method to print all the combo details and find the total price.

Task 4: Done by Nahomi Tesfaye Duki

Print a welcome message followed by the menu.
Take an input from the user for their choice of drink, entrée and side.
Display the reciept after the order is created.

"""