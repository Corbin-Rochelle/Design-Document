import mysql.connector
import sys

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
            query = "SELECT price FROM books, movies WHERE name =%s"
            data = (item,)
            cursor.execute(query, data)
            price = int(cursor)
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
        
        # Push items into the database
        query = "UPDATE shopping_cart SET csv=%s  WHERE name=%s"
        data = (self.items, self.user)
        cursor.execute(query, data)
        connection.commit()

    def addToCart(self, item):
        self.items_list.append(item)
        self.items = self.items + "," + item

        # Query the database for the price of the item, then add it to total
        query = "SELECT price FROM books, movies WHERE name =%s"
        data = (item,)
        cursor.execute(query, data)
        price = int(cursor)
        self.total += price

        # Push items into the database
        query = "UPDATE shopping_cart SET csv=%s  WHERE name=%s"
        data = (self.items, self.user)
        cursor.execute(query, data)
        connection.commit()


    def removeFromCart(self, item):
        self.items_list.remove(item)

        temp_str = ""
        for item in self.items_list:
            temp_str = temp_str + item + ","
        self.items = temp_str.rstrip(",")

        # Retrieve the price for this item in the database
        query = "SELECT price FROM books, movies WHERE name =%s"
        data = (item,)
        cursor.execute(query, data)
        price = int(cursor)
        self.total -= price

        # Push items into the database
        query = "UPDATE shopping_cart SET csv=%s  WHERE name=%s"
        data = (self.items, self.user)
        cursor.execute(query, data)
        connection.commit()



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



