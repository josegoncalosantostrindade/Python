'''
def happy_birthday(name, age):
    print(f'Happy birthday to {name}!')
    print(f'Your are {age} years old!')
    print(f'Happy birthday to {name}!')
    print()

happy_birthday('Gonçalo', 20)
happy_birthday('Bro', 30)
'''

'''
def display_invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due: {due_date}')

display_invoice('JGTrindade', 42.50, '24/11')'''

'''
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))
'''

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + ' ' + last

full_name = create_name('gonçalo', 'trindade')
print(full_name)