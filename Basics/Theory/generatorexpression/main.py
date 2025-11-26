'''
number = int(input('Enter a number to count up to: '))

counter = (count for count in range(1, number + 1))

for num in counter:
    print(num)
'''


# Files
'''
file_path = 'generatorexpression/test.txt'

with open(file_path) as file:
    lines = (line.strip() for line in file)
    for line in lines:
        print(line)
'''


# 
number = int(input('Enter a number to square up to: '))

even_squares = (num**2 for num in range(1, number + 1) if num % 2 == 0)
for square in even_squares:
    print(square)