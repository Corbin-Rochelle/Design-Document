# import mysql.connector
import sys

# import order.py

# Connecting to the Database main
# try:
#     connection = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="password",
#         database="final_project"
#     )

#     print("Successful connection.")


# except:
#     print("Failed connection.")

#     sys.exit()

# cursor = connection.cursor()

# Calling the menuing
def Main_Menu():
     print()
     print("Enter an option: ")
     print("(A) Login")
     print("(B) Create an account")
     print("(C) Exit program")
     print()
     Screen_One()

def Screen_One():
    while True:
        # Gather user input on what to do
        user_input = str(input("").upper())

        # Login: Moves to screen 2
        if user_input == "A":
            Screen_Two()

        # Exit: Ends program
        elif user_input == "B":
            while True:
                user_name = str(input("Enter username: "))
                password = str(input("Enter password: "))
                confirm_password = str(input('Confirm Password : '))
                if password!=confirm_password: 
                    print()
                    print('Password does not match! Try Again')
                    print()
                else:
                    break
            print()
            print('Hurray!! Sign up succesfull!')
            print()
            print("Moving back to title screen.")
            Main_Menu()

        # Create Account: Gathers information, then restarts screen 1
        elif user_input == "C":
            print("Goodbye!")
            exit()

        # logout
        elif user_input == "10":
            print("Logout Successfull")
            Main_Menu()

        else:
            print("Error: Enter a correct option")

def Screen_Two():
    user_name = str(input("Enter username: "))
    password = str(input("Enter password: "))
    print()
    # If username/password passes
    print("Success!, logging you in.")
    print()
    Screen_Three()
    # return
    # If username/password fails
    # print("Failure: Returning to title screen.")
    # return


def Screen_Three():
    print("Enter an integer:")
    print()
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
    print()


print("Hello!, Welcome to the store.")
Main_Menu()
