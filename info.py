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
        if self.numOfOrders >= 3:
            newPrice = self.orderPrice * self.numOfOrders
            newPrice = newPrice * 1.13
            total = newPrice - newPrice * 0.15
            
        elif self.numOfOrders < 3:
            newPrice = self.orderprice * self.numOfOrders
            total = newPrice * 1.13
            
        return total
    
    def toStr(self):
        orderSize = str(self.orderSize)
        orderPrice = str(self.orderPrice)
        numOfOrders = str(self.numOfOrder)
        
        info = f"Pizza Size: {orderSize} \n Quantity: {numOfOrders}"
        
        return info
