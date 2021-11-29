class Order:

	def __init__(self):
		self.firstName = ''
		self.lastName = ''
		self.email = ''
		self.password = ''
		self.address = ''
		self.isAdmin = ''

	def getFirstName(self):
		name = str(input('First name : '))
		return(name)

	def getLastName(self):
		name = str(input('Last name : '))
		return(name)

	def getEmail(self):
		mail = str(input('Email : '))
		return(mail)

	def getPassword(self):
		password = int(input('Password : '))
		return(password)

	def getAddress(self):
		rec_address = ''
		address = str(input('Address : '))
		state = str(input('State : '))
		zip_c = str(input('Zip code : '))
		country = str(input('Country : '))
		rec_address = f'{address},{state},{country},{zip_c}'
		return(rec_address)

	def setFirstName(self,fname):
		self.first_name = fname

	def setLastName(self,lname):
		self.last_name = lname

	def setEmail(self,mail):
		self.email = mail

	def setPassword(self,password):
		self.password = password

	def setAddress(self,add):
		self.address = add

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
menu()