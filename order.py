import mysql.connector
import sys

class Order:

	def __init__(self):
		self.first_name = ''
		self.last_name = ''
		self.email = ''
		self.contact = ''
		self.recieving_address = ''
		self.billing_address = ''
		self.payment_method = ''

	def getFirstName(self):
		name = str(input('First name : '))
		query = 'SELECT first_name FROM order WHERE first_name=%s'
		data = (self.first_name, )
		cursor.execute(query,data)
		return (name)

	def getLastName(self):
		name = str(input('Last name : '))
		query = 'SELECT last_name FROM order WHERE last_name=%s'
		data = (self.last_name, )
		cursor.execute(query,data)
		return(name)

	def getEmail(self):
		mail = str(input('Email : '))
		query = 'SELECT email FROM order WHERE email=%s'
		data = (self.email, )
		cursor.execute(query,data)
		return(mail)

	def getContact(self):
		contact = int(input('Contact Number : '))
		query = 'SELECT contact FROM order WHERE contact=%s'
		data = (self.contact, )
		cursor.execute(query,data)
		return(contact)

	def getReceivingAddress(self):
		rec_address = ''
		address = str(input('Address : '))
		state = str(input('State : '))
		zip_c = str(input('Zip code : '))
		country = str(input('Country : '))
		rec_address = f'{address},{state},{country},{zip_c}'
		query = 'SELECT recieving_address FROM order WHERE recieving_address=%s'
		data = (self.recieving_address, )
		cursor.execute(query,data)
		return(rec_address)

	def getBillingAddress(self):
		address = str(input('Address : '))
		state = str(input('State : '))
		zip_c = str(input('Zip code : '))
		country = str(input('Country : '))
		bill_address = f'{address},{state},{country},{zip_c}'
		query = 'SELECT billing_address FROM order WHERE billing_address=%s'
		data = (self.billing_address, )
		cursor.execute(query,data)
		return(bill_address)

	def getPaymentMethod(self):
		payment_method = int(input('Payment Method\n1.Credit Card\n2.Debit card\n3.Paypal\nOption : '))
		query = 'SELECT payment_method FROM order WHERE payment_method=%s'
		data = (self.payment_method, )
		cursor.execute(query,data)
		if payment_method == 1:
			return('Credit Card')
		elif payment_method == 2:
			return('Debit Card')
		elif payment_method == 3:
			return('Paypal')
		elif payment_method == 4:
			return('Please enter the right option of payment method')
			getPaymentMethod()


	def setFirstName(self,fname):
		self.first_name = fname
		query = 'UPDATE order SET fname=%s  WHERE first_name=%s'
        data = (fname, self.first_name)
        cursor.execute(query, data)
        connection.commit()
		

	def setLastName(self,lname):
		self.last_name = lname
		query = "UPDATE order SET lname=%s  WHERE last_name=%s"
        data = (lname, self.last_name)
        cursor.execute(query, data)
        connection.commit()

	def setEmail(self,mail):
		self.email = mail
		query = "UPDATE order SET mail=%s  WHERE email=%s"
        data = (mail, self.email)
        cursor.execute(query, data)
        connection.commit()

	def setContact(self,contact):
		self.contact = contact
		query = "UPDATE order SET contact=%s  WHERE contact=%s"
        data = (contact, self.contact)
        cursor.execute(query, data)
        connection.commit()

	def setReceivingAddress(self,add):
		self.recieving_address = add
		query = "UPDATE order SET add=%s  WHERE recieving_address=%s"
        data = (add, self.recieveing_address)
        cursor.execute(query, data)
        connection.commit()

	def setBillingAddress(self,add):
		self.billing_address = add
		query = "UPDATE order SET add=%s  WHERE billing_address=%s"
        data = (add, self.billing_address)
        cursor.execute(query, data)
        connection.commit()

	def setPaymentMethod(self,pay):
		self.payment_method = pay
		query = "UPDATE order SET pay=%s  WHERE payment_method=%s"
        data = (pay, self.payment_method)
        cursor.execute(query, data)
        connection.commit()

def login():
	username = str(input('Username : '))
	password = str(input('Password : '))
	return(username,password)

def sign_up():
	while True:
		username = str(input('Username : '))
		password = str(input('Password : '))
		confirm_password = str(input('Confirm Password : '))
		if password!=confirm_password:
			print('Password does not match!')
		else:
			break
	print('Hurray!! Sign up succesfull!')
	return(username,password)

def menu():
	log_status = int(input('Are you a member ?\n1.Yes\n2.No\nChoice: '))
	if log_status == 1:
		login()
	elif log_status == 2:
		sign_up()
	print()
	order = Order()
	fname = order.getFirstName()
	lname = order.getLastName()
	mail = order.getEmail()
	contact = order.getContact()
	if log_status==2:
		rec_add = order.getReceivingAddress()
		opt = int(input('Billing Adress same as Receiving Address ? \n1.Yes\n2.No\nChoice: '))
		if opt == 2:
			bill_add = order.getBillingAddress()
		else:
			bill_add = rec_add
		pay_method = order.getPaymentMethod()

	order.setFirstName(fname)
	order.setLastName(lname)
	order.setEmail(mail)
	order.setContact(contact)
	if log_status==2:
		order.setReceivingAddress(rec_add)
		order.setBillingAddress(bill_add)
		order.setPaymentMethod(pay_method)

	print('\n\tOrder class attributes :')
	if log_status==2:
		print(f'First name : {order.first_name}\nLast name : {order.last_name}\nEmail : {order.email}\nContact Number : {order.contact}\nReceiving Address : {order.recieving_address}\nBilling Address : {order.billing_address}\nPayment Method : {order.payment_method}')
	else:
		print(f'First name : {order.first_name}\nLast name : {order.last_name}\nEmail : {order.email}\nContact Number : {order.contact}')

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
