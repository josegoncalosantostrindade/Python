from car import Car

car1 = Car('Porsche', 2025, 'Black', False)
car2 = Car('Corvette', 2022, 'Red', True)
car3 = Car('BMW', 2016, 'Blue', True)

'''
print(car3.model)
print(car3.year)
print(car3.color)
print(car3.for_sale)
'''

car2.drive()
car3.stop()
car3.describe()