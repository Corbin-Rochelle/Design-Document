import mysql.connector
import sys

class User:

	def __init__(self):
		self.firstName = ''
		self.lastName = ''
		self.email = ''
		self.password = ''
		self.address = ''

	def getFirstName(self):
        query = "SELECT firstName FROM user WHERE name=%s"
        data = (self.firstName, )
        cursor.execute(query,data)
        return str(cursor)

	def getLastName(self):
        query = "SELECT lastName FROM user WHERE name=%s"
        data = (self.lastName, )
        cursor.execute(query,data)
        return str(cursor)

	def getEmail(self):
        query = "SELECT email FROM user WHERE name=%s"
        data = (self.email, )
        cursor.execute(query,data)
        return str(cursor)

	def getPassword(self):
        query = "SELECT password FROM user WHERE name=%s"
        data = (self.password, )
        cursor.execute(query,data)
        return str(cursor)

	def getAddress(self):
        query = "SELECT address FROM user WHERE name=%s"
        data = (self.address, )
        cursor.execute(query,data)
        return str(cursor)

	def setFirstName(self,fname):
		query = "UPDATE firstName SET user=%s  WHERE name=%s"
        data = (user, self.name,)
        cursor.execute(query, data)
        connection.commit()

	def setLastName(self,lname):
		query = "UPDATE lastName SET user=%s  WHERE name=%s"
        data = (user, self.name,)
        cursor.execute(query, data)
        connection.commit()

	def setEmail(self,mail):
		query = "UPDATE email SET user=%s  WHERE name=%s"
        data = (user, self.name,)
        cursor.execute(query, data)
        connection.commit()

	def setPassword(self,password):
		query = "UPDATE password SET user=%s  WHERE name=%s"
        data = (user, self.name,)
        cursor.execute(query, data)
        connection.commit()

	def setAddress(self,add):
		query = "UPDATE address SET user=%s  WHERE name=%s"
        data = (user, self.name,)
        cursor.execute(query, data)
        connection.commit()
