class ShoppingCart:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.total = 0
        self.numItems = 0

    def displayCart(self):
        for item in self.items:
            print(item.get_name(), end=' ')

    def checkoutCart(self):
        for item in self.items:
            # Actually handle the order physically IRL
            self.items.remove(item)

    def addToCart(self, item):
        self.items.append(item)
        self.total += item.get_price()


    def removeFromCart(self, item):
        self.items.remove(item)
        self.total -= item.get_price()



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

print("Hello!, Welcome to the store.")
Screen_One()




