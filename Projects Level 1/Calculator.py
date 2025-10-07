print('|----------------|')
print('|   Calculator   |')
print('|----------------|')
print('|----------------|')
print('|    Operators   |')
print('|  +  -    *  /  |')
print('|----------------|')

num1 = float(input('\nFirst number: '))
num2 = float(input('Second number: '))
ope = input('Choose the operation: ')

if ope == '+':
    res = num1 + num2
    print(f'{num1} + {num2} = {res:.2f}\n')
elif ope == '-':
    res = num1 - num2
    print(f'{num1} - {num2} = {res:.2f}\n')
elif ope == '*':
    res = num1 * num2
    print(f'{num1} x {num2} = {res:.2f}\n')
elif ope == '/':
    res = num1 / num2
    print(f'{num1} / {num2} = {res:.2f}\n')
else :
    print('Something went wrong!\n')
