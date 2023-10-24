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

