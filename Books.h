import mysql.connector
import sys


class Books:

    def __init__(self):
        self.isbn = ''

    # Getters FORMAT ALL OF THESE
    def get_title(self):
        return self.isbn

    def get_title(self):
        query = "SELECT name FROM inventory WHERE name=%s"
        data = (self.isbn, )
        cursor.execute(query,data)
        return str(cursor)

    def get_author(self):
        query = "SELECT producer FROM inventory WHERE name=%s"
        data = (self.isbn,)
        cursor.execute(query, data)
        return str(cursor)

    def get_stock(self):
        query = "SELECT stock FROM inventory WHERE name=%s"
        data = (self.isbn,)
        cursor.execute(query, data)
        return int(cursor)

    def get_price(self):
        query = "SELECT price FROM inventory WHERE name=%s"
        data = (self.isbn,)
        cursor.execute(query, data)
        return float(cursor)

    def get_shipping_price(self):
        query = "SELECT shipping_info FROM inventory WHERE name=%s"
        data = (self.isbn,)
        cursor.execute(query, data)
        return str(cursor)

    def get_stars(self):
        query = "SELECT stars FROM inventory WHERE name=%s"
        data = (self.isbn,)
        cursor.execute(query, data)
        return int(cursor)

    def get_reviews(self):
        query = "SELECT reviews FROM inventory WHERE name=%s"
        data = (self.isbn,)
        cursor.execute(query, data)
        return int(cursor)

    # Setters
    def set_title(self, title):
        query = "UPDATE inventory SET stock=%s  WHERE name=%s"
        data = (title, self.isbn,)
        cursor.execute(query, data)
        connection.commit()

    def set_author(self, author):
        query = "UPDATE inventory SET classification=%s  WHERE name=%s"
        data = (author, self.isbn,)
        cursor.execute(query, data)
        connection.commit()

    def set_stock(self, stock):
        query = "UPDATE inventory SET producer=%s  WHERE name=%s"
        data = (stock, self.isbn,)
        cursor.execute(query, data)
        connection.commit()

    def set_price(self, price):
        query = "UPDATE inventory SET price=%s  WHERE name=%s"
        data = (price, self.isbn,)
        cursor.execute(query, data)
        connection.commit()

    def set_shipping_info(self, shipping_info):
        query = "UPDATE inventory SET shipping_info=%s  WHERE name=%s"
        data = (shipping_info, self.isbn,)
        cursor.execute(query, data)
        connection.commit()

    def set_stars(self, stars):
        query = "UPDATE inventory SET stars=%s  WHERE name=%s"
        data = (stars, self.isbn,)
        cursor.execute(query, data)
        connection.commit()

    def set_reviews(self, reviews):
        query = "UPDATE inventory SET reviews=%s  WHERE name=%s"
        data = (reviews, self.isbn,)
        cursor.execute(query, data)
        connection.commit()


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


# Miscellaneous
