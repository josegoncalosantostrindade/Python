# name = input('Enter your name: ')
# age = int(input('Enter your age: '))
# food = input('Enter a food you like (q to quit): ')
num = int(input('Enter a number between 1 - 10: '))

'''
while name == '':
    print('You did not enter your name')
    name = input('Enter your name: ')

print(f'Hello {name}')
'''

'''
while age < 0:
    print('Age can not be negative')
    age = int(input('Enter your age: '))

print(f'You are {age} years old')
'''

'''
while not food == 'q':
    print(f'Ypu like {food}')
    food = input('Enter another food you like (q to quit): ')

print('Bye')
'''

while num < 1 or num > 10:
    print(f'{num} is not valid')
    num = int(input('Enter a number between 1 - 10: '))

print(f'Your number is {num}')