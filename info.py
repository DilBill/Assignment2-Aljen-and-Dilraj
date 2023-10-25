'''The class User is used to retain the information of the user such as the name, email, and address'''
class User:
    def __init__(self, name, email, address):
        self.userName = name
        self.userEmail = email
        self.userAddress = address
        
'''The class Pizza is used to create the order including the size, amount and total price before or after discounts'''
class Order:

    def __init__ (self, size, price, num):
        self.orderSize = size
        self.orderPrice = price
        self.numOfOrders = num

    def getTotal(self):
        tax = 1.13
        # checks how many pizza the user ordered to see if the discount should be applied
        if self.numOfOrders >= 3:
            # multiplys the single price of a pizza by the number of pizzas ordered
            newPrice = self.orderPrice * self.numOfOrders
            # apply tax to the price 
            newPrice = newPrice * 1.13
            # apply discount to the price
            total = newPrice - newPrice * 0.15
            
        # checks how many pizzas the user ordered
        elif self.numOfOrders < 3:
            # multiplys the price of a single pizza by the number of how many the user ordered
            newPrice = self.orderprice * self.numOfOrders
            # applys tax to the price
            total = newPrice * 1.13
            
        return total
    
    def toStr(self):
        # converts all variables to string using str() method
        orderSize = str(self.orderSize)
        orderPrice = str(self.orderPrice)
        numOfOrders = str(self.numOfOrder)
        # create a string that can be printed to the user
        info = f"Pizza Size: {orderSize} \n Quantity: {numOfOrders}"
        
        return info
