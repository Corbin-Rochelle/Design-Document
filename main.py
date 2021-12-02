from books import *
from movies import *
from order import *
from user import *
from shopping_cart import *

import mysql.connector
import sys

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


       

def Screen_Two():
    user_name = str(input("Enter username: "))
    password = str(input("Enter password: "))
    print()
    # Checking password
    query = "SELECT password FROM users WHERE first_name=%s"
    data = (user_name,)
    cursor.execute(query, data)
    result = cursor.fetchall()
    if password == result[0][0]:
        print("Success!, logging you in.")
        print()
        Screen_Three(user_name)
        return
    # If username/password fails
    else:
        print("Failure: Returning to title screen.")
        return


def Screen_Three(user_name):
    
    shopping_cart = ShoppingCart(user_name)
    # Requires a branch, no need to create new function
    print("(1): View all items in movies or books")

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
    
    user_input = int(intput("Enter an integer: ))
                            
    
    # Screen Three
        elif user_input == "1":
            answer = str(input("Do you want to see 1) movies or 2) books?"))
            if answer == "1":
                cursor.execute("SELECT title FROM movies")
                result = cursor.fetchall()
                for x in result:
                    print(x[0])
            elif answer == "2":
                cursor.execute("SELECT title FROM books")
                result = cursor.fetchall()
                for x in result:
                    print(x[0])
            else:
                pass

        elif user_input == "2":
            user_name = str(input("What is your user name? "))
            query = "SELECT csv FROM shopping_cart WHERE name = %s"
            data = (user_name,)
            cursor.execute(query, data)
            result = cursor.fetchall()
            for x in result:
                print(x[0])
        
        elif user_input == "3":
            item_name = str(input("Enter the name of the item: "))
            shopping_cart.addToCart(item_name)
                            
        elif user_input == "4":
            
                            
        elif user_input == "5":
            pass
                            
         elif user_input == "6":
            print("Your order history: ")
            cursor.execute("SELECT * FROM order where email = %s")
            result = cursor.fetchall()
            for x in result:
                print(x[0])
                            
        elif user_input == "7":
            pass  
                            
        elif user_input == "8"
            pass
                            
        elif user_input == "9":
            user_name = str(input("What is your user name? "))
            query = "DELETE FROM user WHERE name= %s"
            data = (user_name,)
            result = cursor.fetchall()
            for x in result:
                print(x[0])
            print("User deleted")
            print()
                            
        elif user_input == "10":
            print("Logout Successfull")
            Main_Menu()
            
        else:
            print("Select a correct option!")


print("Hello!, Welcome to the store.")
Main_Menu()
