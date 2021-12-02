import mysql.connector
import sys

class User:

	def __init__(self):
		self.firstName = ''

	def getFirstName(self):
        query = "SELECT firstName FROM user WHERE name=%s"
        data = (self.firstName, )
        cursor.execute(query,data)
        return str(cursor)

	def setFirstName(self,fname):
		query = "UPDATE firstName SET user=%s  WHERE name=%s"
        data = (user, self.name,)
        cursor.execute(query, data)
        connection.commit()
