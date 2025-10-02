#Output
print(' -=-=-=-=-=-=-=-=-=-=-=-=-= ')
print('|                          |')
print('|        Calculator        |')
print('|                          |')
print('|    +     -    *     /    |')
print(' -=-=-=-=-=-=-=-=-=-=-=-=-= ')

#Input
num1 = float(input('\nEnter the first number: '))
num2 = float(input('Enter the second number: '))
oper = input('Enter the operation: ')

#Conditions
if oper == '+':
    res = num1 + num2
    print(f'The result of the addition is {num1} + {num2} = {res}')
elif oper == '-':
    res = num1 - num2
    print(f'The result of the subtraction is {num1} - {num2} = {res}')
elif oper == '*':
    res = num1 * num2
    print(f'The result of the multiplication is {num1} x {num2} = {res}')
elif oper == '/':
    res = num1 / num2
    print(f'The result of the division is {num1} / {num2} = {res:.2f}')