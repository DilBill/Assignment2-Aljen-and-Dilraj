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
        if self.numOfOrders >= 3:
            newPrice = self.orderPrice * self.numOfOrders
            total = newPrice - newPrice * 0.15
            
        elif self.numOfOrders < 3:
            total = self.orderPrice * self.numOfOrders
            
        return total
    
    def toStr(self):
        orderSize = str(self.orderSize)
        orderPrice = str(self.orderPrice)
        numOfOrder = str(self.numOfOrder)
        
        info = f"Pizza Size: {self.orderSize} \n Quantity: {self.numOfOrders}"
        
        return info
