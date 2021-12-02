# Information
    # I need to be able to update the databse from inside the shopping cart class

class ShoppingCart:
    def __init__(self, user):
        self.user = user

        # Retrieve comma separated value from table as a string called items
        # This will both be updated as the user adds/removes things
        # This makes it easier to handle updating a database and
        # handling the items in python themselves
        self.items = ""
        self.items_list = self.items.split(",")

        self.total = 0
        for item in self.items_list:
            # Loop through each item
            # Access the database to get its price using its name. The name is "item", the primary key
            pass
            price = 0
            self.total += price


        self.numItems = len(self.items_list)



    def displayCart(self):
        my_dictionary = {}
        for item in self.items_list:
            if item in my_dictionary.keys():
                my_dictionary[item] = my_dictionary[item] + 1
            else:
                my_dictionary[item] = 1

        for key, value in my_dictionary.items():
            print(key,": ", value)

    def checkoutCart(self):
        self.items = ""
        self.items_list = []
        # Push items = "" into the database for self.user
        pass

    def addToCart(self, item):
        self.items_list.append(item)
        self.items = self.items + "," + item

        # Query the database for the price of the item, then add it to total
        pass
        price = 0
        self.total += price

        # Push items into the database
        pass


    def removeFromCart(self, item):
        self.items_list.remove(item)

        temp_str = ""
        for item in self.items_list:
            temp_str = temp_str + item + ","
        self.items = temp_str.rstrip(",")

        # Update the csv for this user in the database
        pass
        self.total -= item.get_price()

        # Push items into the database
        pass



    # Setters/Getters
    def setUser(self, user):
        self.user = user

    def getUser(self):
        return self.user

    def setTotal(self, total):
        self.total = total

    def getTotal(self):
        return self.total

    def setNumItems(self, num_items):
        self.numItems = num_items

    def getNumItems(self):
        return self.numItems


def Screen_One():
    while True:
        # Gather user input on what to do
        print("Enter an integer")
        print("(1) Login")
        print("(2) Create an account")
        print("(3) Exit program")
        print()
        user_input = str(input(""))

        # Login: Moves to screen 2
        if user_input == "1":
            Screen_Two()

        # Exit: Ends program
        elif user_input == "2":
            user_name = str(input("Enter username: "))
            password = str(input("Enter password: "))
            print("Moving back to title screen.")

        # Create Account: Gathers information, then restarts screen 1
        elif user_input == "3":
            print("Goodbye!")
            exit()

        else:
            print("Error: Enter a correct integer")

def Screen_Two():
    user_name = str(input("Enter username: "))
    password = str(input("Enter password: "))

    # If username/password passes
    print("Success!, logging you in.")
    Screen_Three()
    return
    # If username/password fails
    # print("Failure: Returning to title screen.")
    # return

def Screen_Three():
    print("Enter an integer")

    # Requires a branch, no need to create new function
    print("(1): View all items in a specific category")

    print("(2): View all items in your shopping cart")

    # Requires a branch, no need to create new function
    print("(3): Add an item from a category to your shopping cart")

    print("(4): Remove an item from your shopping cart")
    print("(5): Checkout items currently in your shopping cart")
    print("(6): View your order history")
    print("(7): Edit your shipping information")
    print("(8): Edit your payment information")
    print("(9): Delete your account")
    print("(10): Logout")

# print("Hello!, Welcome to the store.")
# Screen_One()



