import mysql.connector
import sys


class Movies:

    def __init__(self):
        self.name = ''

    # Getters FORMAT ALL OF THESE
    def get_title(self):
        query = "SELECT title FROM Movies WHERE name=%s"
        data = (self.title, )
        cursor.execute(query,data)
        return str(cursor)

    def get_stock(self):
        query = "SELECT stock FROM Movies WHERE name=%s"
        data = (self.stock,)
        cursor.execute(query, data)
        return int(cursor)

    def get_price(self):
        query = "SELECT price FROM Movies WHERE name=%s"
        data = (self.price,)
        cursor.execute(query, data)
        return float(cursor)

    def get_shipping_price(self):
        query = "SELECT shipping_price FROM Movies WHERE name=%s"
        data = (self.shipping_price,)
        cursor.execute(query, data)
        return str(cursor)

    def get_reviews(self):
        query = "SELECT reviews FROM Movies WHERE name=%s"
        data = (self.reviews,)
        cursor.execute(query, data)
        return int(cursor)
    
    def get_producer(self):
        query = "SELECT producer FROM Movies WHERE name=%s"
        data = (self.producer,)
        cursor.execute(query, data)
        return str(cursor)

     # Setters
    def set_stock(self, stock):
        query = "UPDATE Movies SET stock=%s  WHERE name=%s"
        data = (stock, self.stock,)
        cursor.execute(query, data)
        connection.commit()

    def  set_price(self, price):
        query = "UPDATE Movies SET price=%s  WHERE name=%s"
        data = (price, self.price,)
        cursor.execute(query, data)
        connection.commit()

    def set_shipping_price(self, shipping_price):
        query = "UPDATE Movies SET shipping_price=%s  WHERE name=%s"
        data = (shipping_info, self.shipping_price,)
        cursor.execute(query, data)
        connection.commit()

    def set_producer(self, producer):
        query = "UPDATE Movies SET producer=%s  WHERE name=%s"
        data = (producer, self.producer,)
        cursor.execute(query, data)
        connection.commit()

    def set_reviews(self, reviews):
        query = "UPDATE Movies SET reviews=%s  WHERE name=%s"
        data = (reviews, self.reviews,)
        cursor.execute(query, data)
        connection.commit()
