# Import the User and Pizza classes from the info.py file
from info import User, Order
# ask the user for their name
name = input('Whats the name for the order? ')
# ask the user to provide a email
email = input('please provide a email so that we can send you updates on the order\n (exampleEmail@gmail.com): ')
# ask the use for an address for delivery
address = input('Please provide an address for delivery: ')

while True:
    # ask the user what size pizza they want
    size = int(input('What size pizza would you like to order\n 1 for SMALL / 2 for MEDIUM / 3 for LARGE / 4 for X-LARGE : '))
    # conditonal statement checking if the user inputed 1
    if size == 1:
        # Changes the variable price depending on the selection
        price = 10
        print(f'One small pizza will cost ${price}')
        break
    # conditonal statement checking if the user inputed 2
    elif size == 2:
        price = 12
        print(f'One medium pizza will cost ${price}')
        break
    # conditonal statement checking if the user inputed 3
    elif size == 3:
        price = 15
        print(f'One large pizza will cost ${price}')
        break
    # conditonal statement checking if the user inputed 4
    elif size == 4:
        price = 18
        print(f'One x-large pizza will cost ${price}')
        break
    # conditonal statement checking if the user input something other than 1, 2, 3, 4 and will allow them to try again
    elif size != 1 or size != 2 or size != 3 or size != 4:
        print('Invaild Size Try Again')

# ask the user how many pizza they would like        
numPizza = int(input('How many pizzas would you like to order '))
    
# create the object pizza
pizza = Order(size, price, numPizza)
# create the object user
user = User(name, email, address )

print(pizza.getTotal())
print(f'The order will be deliverd to {user.userName} at {user.userAddress}')
print(f'A copy of the reciept will be sent to {user.userEmail}')

    
    