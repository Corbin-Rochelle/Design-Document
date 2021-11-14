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

List of Classes and Explaination: 
1. Inventory: This is the most simple, yet, neccessary class for an e-commerce store. For our store to function as a store we need to keep track of what we have and some information about each item. 
2.
3.
4.
5.

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

All of these functions, except the constructor, are either getters or setters because the itme class is not going to be manipulating anything itself. 

---
### Class 2:

---
### Class 3:
---

### Class 4:
---

### Class 5:


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
