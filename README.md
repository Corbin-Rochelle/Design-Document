# Design-Document
Part 1 of the Final Project in Methods and Tools.

## Group Information
Group Number 27

Group Member Names/netIDs:
- David Burk
  - dab724
- Brandon Lynchard
  - bsl159
- Raysita Maharani
  - rjm470
- Connor Moody
  - mcm1053
- Corbin Rochelle 
  - ctr233

List of Classes and Explanation: 
1. Inventory: This is the most simple, yet, neccessary class for an e-commerce store. For our store to function as a store we need to keep track of what we have and some information about each item. 
2. User: This class will allow user accounts to be created and to view the information associated with them.
3. Order: This class will takes in the users order information, associate it with the users personal information and where to ship them.
4. Shopping Cart: This class will handle everything related to a user's shopping cart, such as checking out and totaling the price.

## Detailed UML Class diagrams

### Class 1: Inventory 
<img width="273" alt="Inventory_UML_Corbin_Rochelle" src="https://user-images.githubusercontent.com/94238706/141689458-47c3fe7e-205b-4fd7-bd4a-a5ddfafe3df6.png">

- Inventory(): This is the constrcutor function, which sets up a new item of inventory. 
- getName(): This is a getter for the Name of the item.
- getClassification(): This is a getter for the Classification of the item.
- getPrice(): This is a getter for the Price of the item.
- getShippingInfo(): This is a getter for the Shipping Info of the item.
- getProducer(): This is a getter for the Producer of the item.
- getStars(): This is a getter for the Stars of the item.
- getReviews(): This is a getter for the Reviews of the item. 
- setName(): This is a setter for the Name of the item.
- setClassification(): This is a setter for the Classification of the item.
- setPrice(): This is a setter for the Price of the item.
- setShippingInfo(): This is a setter for the Shipping Info of the item.
- setProducer(): This is a setter for the Producer of the item.
- setStars(): This is a setter for the Stars of the item. 
- setReviews(): This is a setter for the Reviews of the item.

All of these functions, except the constructor, are either getters or setters because the item class is not going to be manipulating anything itself. 

---
### Class 2: User
<img width="273" alt="Users_UML_Connor_Moody" src="https://user-images.githubusercontent.com/89549880/141785135-35fc24cb-ff48-4c0e-b2f2-4749dd00d63c.png">

- User(): This is the constructor for the user class.
- getFirstName(): This gets the users first name.
- getLastName(): This gets the users last name.
- getEmail(): This gets the users email address.
- getPassword(): This gets the users password for their email to login.
- getAddress(): This gets the users address to know where to ship to.
- setFirstName(): This sets the users first name.
- setLastName(): This sets the users last name.
- setEmail(): This sets the users email.
- setPassword(): This sets the users password for the email.
- setAddress(): This sets the users address.

All of these functions, except the constructor, are either getters or setters because the item class is not going to be manipulating anything itself. 

---
### Class 3: Order
<img width="273" alt="Order_UML_Raysita_Maharani" src="https://user-images.githubusercontent.com/85123454/144342008-9955ef4b-1c76-4411-b394-f6b04351c138.PNG">

- Order(): This is the constructor function, which takes the users order.
- getEmail(): This gets the users email address.
- getContact(): This gets the users phone number.
- getReceivingAddress(): This gets the users delivery address.
- getBillingAddress(): This gets the users billing address.
- getPaymentMethod(): This gets the users payment method.
- setEmail(): This sets the users email address.
- setContact(): This sets the users phone number.
- setReceivingAddress(): This sets the users delivery address.
- setBillingAddress(): This sets the users billing address.
- setPaymentMethod(): This sets the users payment method.

All of these functions, except the constructor, are either getters or setters because the item class is not going to be manipulating anything itself. 

---
### Class 4: Shopping Cart

![ShoppingCartUML](https://user-images.githubusercontent.com/58010076/141879885-4e7d3896-d7c3-4067-be6a-493f3272f4da.PNG)

- ShoppingCart(): This is the constructor functiom, it requires a user to initialize.
- displayCart(): Displays the contents of the the users shopping cart.
- checkoutCart(): Does everything necessary to checkout a users shopping cart.
- addToCart(): Adds an item to the cart.
- removeFromCart(): Removes an item from the cart.
- setUser(): Sets the owner/user of the shopping cart.
- getUser(): Gets the owner/user of the shopping cart.
- setTotal(): Sets the total price of the shopping cart.
- getTotal(): Gets the total price of the shopping cart.
- setNumItems(): Sets the total number of items in the shopping cart.
- getNumItems(): Gets the total number of items in the shopping cart.

---

## Menuing 
The menuing will be split into three sections: before login, after login but before checkout, and after login during checkout. 

### Before Login [1]
- Login (moves to [2])
- Create Account
- Exit Store

### Login [2]
- Username Entry
- Password Entry
- Forgot Username/Password
- Enter (if pass, moves to [3], if fail moves to [1])

### After Login But Before Checkout [3]
- Search for Item Name
- Search for Item Type
- Add to Cart
  - Prompts to enter which Item Number and How Many
- View Cart
  - Remove Item
  - Back to Shopping
- Return and Item
  - Which Item?
  - Back to Shopping
- Checkout (moves to [3])
- Logout (moves to [1])

### After Login, During Checkout [4]
- Billing Information
- Shipping Address
- Billing Address
- Shipping Options
  - Overnight, Standard, etc.
- Finalize
- Go Back (moves to [3])

The menu covers all known requirements at the present moment; although, it will have to be edited in the future more than likely to account for some present unforseen reason(s). 

## Storing Data
This group has decided by a vote that we are going to use a database. The database we are going to use is mySQL (tentative). 
