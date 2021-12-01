import mysql.connector
import sys

def menu():
    print("""1) Search for Item\n
    2) Search for Item Type\n
    3) Add to Cart\n
    4) View Cart\n
    5) Return an Item\n
    6) Checkout\n
    7) Logout
    """)
    option = int(input())
    match option:
        case 1:
            search_item()
        case 2:
            search_item_type()
        case 3:
            add_item_cart()
        case 4:
            view_cart()
        case 5:
            return_item()
        case 6:
            checkout()
        case 7:
            logout()


def search_item():
    # INSERT SQL QUERY HERE
    print("NOT DONE")


def search_item_type():
    # INSERT SQL QUERY HERE
    print("NOT DONE")


def add_item_cart():
    # INSERT SQL QUERY HERE
    print("NOT DONE")


def view_cart():
    # INSERT SQL QUERY HERE
    print("NOT DONE")


def return_item():
    # INSERT SQL QUERY HERE
    print("NOT DONE")


def checkout():
    # INSERT SQL QUERY HERE
    print("NOT DONE")


def logout():
    # INSERT SQL QUERY HERE
    print("NOT DONE")


# Calling main
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

menu()
