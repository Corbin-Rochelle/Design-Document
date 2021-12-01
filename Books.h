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
