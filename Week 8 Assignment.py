"""Program: Week6Assignment.py   
Author: Felix Ortiz   
Defining the list and options   
1. The user will be shown options 1-6 to be able to choose what they want to do.   
2. The functions are defined per option.   
The while loop will continue and present the users with the options over and over until they enter 6 or anything outside of 1-6."""   

class orderData:  

    number = 0  

    name = ""  

    price = 0.0  

      

    def __init__(self, number, name, price):  

        self.number = number  

        self.name = name  

        self.price = price  

          

    def setnumber(self,number):  

        self.number = number  

    def setname (self,name):  

        self.name = name  

    def setprice(self,price):  

        self.price = price  

          

          

    def getnumber(self):  

        return self.number  

          

    def getname(self):  

        return self.name  

          

    def getprice(self):  

        return self.price  

      

    def displayData(self):  

        print("")  

        print("Order Information: ")  

        print("---------------------------")  

        print("Order Number: ", self.number)  

        print("Order Name: ", self.name)  

        print("Order Price: ", self.price)  

# Defining the list and options   

orders = {} #this is the name of the list the user is going to be creating.   

def getSelection():   

  
   

    print ("=========Options Selection=========")   

  
   

    print("1. Add Order")   

  
   

    print("2. Delete Order")   

  
   

    print("3. Edit Order")   

  
   

    print("4. Display Order")   

      

    print("5. Save Order")  

      

    print("6. Exit Program")   

  
   

    selection = int(input("Enter a number from 1-5 or 6 to Exit: "))   

  
   

    return selection   

# The user has the option to add an order to the list.
def addOrder(orders):
    try:
        number = int(input("Enter Order Number: "))  

        name = input("Enter Order Name: ")  

        price = float(input("Enter Order Price: "))  

        orders[number] = orderData(number, name, price)
    except ValueError:
        print("You did not enter a valid number or price!")

    return orders  

    print("Added")  

# The user has the option to delete any of the orders they've inputed.   
def deleteOrder(orders):   

  
   

        removeNumber = int(input("Enter Order Number to be deleted: "))  

  
   

        if removeNumber in orders:   

            del orders[removeNumber]  

            print("Order has been deleted.")  

        else:  

            print("Order not found.")  

        return orders  

#an edit option for the user   
def editOrder(orders):  

    oldOrder = int(input("Enter Order Number to edit: "))  

    if oldOrder in orders:  

        newOrder = int(input("Enter New Order Number: "))  

        newName = input("Enter New Order Name: ")  

        newPrice = float(input("Enter New Order Price: "))  

        orders[oldOrder] = orderData(newOrder, newName, newPrice)  

    else:  

        print("Order not found in List.")  

    return orders  

#This is going to show what orders the user has inputed
def displayOrders(orders):  

    if len(orders) == 0:  

        print("No orders in dictionary.")  

    else:  

        for x in orders.keys():  

            orders[x].displayData()  

    return ''  

#This will save the order to a text filter  
def saveOrder(orders):  

    import pickle  

    text_file = open("orders.txt", "wb")  

    pickle.dump(orders, text_file)  

    text_file.close()  

    file_text = open("orders.txt", "rb")  

    test_file = pickle.load(file_text)  

    print ("---------------------------\n", displayOrders(orders))  

# This loop is going to continue until the user enters 5 to exit or enter any number outside of 1-5   
while True :   

  
   

    print("\n")   

  
   

    selection = getSelection()   

  
   

    if (selection == 1):   

  
   

        addOrder(orders)  

  
   

    elif (selection == 2):   

  
   

       deleteOrder(orders)  

  
   

    elif (selection == 3):   

  
   

        editOrder(orders)  

  
   

    elif(selection == 4):   

  
   

        displayOrders(orders)  

      

    elif(selection == 5):  

      

        saveOrder(orders)  

  
   

    elif(selection == 6):   

  
   

        print("Exiting Program...")   

  
   

        break   

  
   

    else:   

  
   

        print("Invalid Entry! Please enter a number 1-5 or 6 to exit.")   

  
   

        print("Exiting Loop")   

  
   

        break  

 

 

 