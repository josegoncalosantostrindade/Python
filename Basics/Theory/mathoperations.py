# Arithmetic Operators
'''friends = 10

# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 2

print(friends)
print(remainder)
'''

# Built-In Functions
'''
x = 3.14
y = 4
z = 5

# result = round(x)
# result = abs(y)
# result = pow(4, 3)
# result = max(x, y, z)
# result = min(x, y, z)

print(result)
'''

# Math Module
'''
import math
x = 9.9

# print(math.pi)
# print(math.e)
# result = math.sqrt(x)
# result = math.ceil(x)
# result = math.floor(x)

print(result)
'''

# Exercise: Circumference Of A Circle
'''
import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius
print(f'The circunference is: {round(circumference, 2)}cm')
'''

# Exercise: Area Of A Circle
'''
import math

radius = float(input('Enter the radius of a circle: '))

area = math.pi * pow(radius, 2)
print(f'The area of the circle is: {round(area, 2)}^cm2')
'''

# Exercise: Hypotenuse Calculator
'''
import math

a = float(input('Enter side a: '))
b = float(input('Enter side b: '))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f'Side C = {round(c, 2)}')
'''