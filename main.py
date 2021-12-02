import mysql.connector
import sys

import order.py

# Connecting to the Database main
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="final_project"
    )

    print("Successful connection.")


except:
    print("Failed connection.")

    sys.exit()

cursor = connection.cursor()

# Calling the menuing

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
