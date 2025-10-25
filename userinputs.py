# Theory
'''
name = input('Enter your name: ')
age = int(input('Enter your age: '))

print(f'Hello {name}')
print(f'You are {age} years old')
'''

# Mad Libs
'''
adjective1 = input('Enter your adjective: ')
noun = input('Enter your noun: ')
adjective2 = input('Enter your adjective: ')
verb = input('Enter your verb: ')
adjective3 = input('Enter your adjective: ')

print(f'Today i went to a {adjective1} zoo')
print(f'in an exhibit, i saw {noun}')
print(f'{noun} was {adjective2} and {verb}ing')
print(f'I was {adjective3}')
'''

# Area/Volume Cale
'''
length = float(input('Enter the length of a rectangle: '))
width = float(input('Enter the width of a rectangle: '))
height = float(input('Enter the height of a rectangle: ')) # just for volume

area = length * width * height

print(f'The are is: {area}cm^3') # cm^2 for area, cm^3 for volume
'''

# Shopping cart
item = input('What item would you like to buy? ')
price = float(input('What is the price? '))
quantity = int(input('How many would you like? '))

total = price * quantity
print(f'You have bought {quantity} x {item}/s')
print(f'Your totla is: ${round(total, 2)}') # round the number with 2 decimal numbers