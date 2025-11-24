# List
'''
fruits = ['banana', 'orange', 'apple', 'coconut']

# frutis.sort()
fruits.sort(reverse=True)
print(fruits)
'''

# Tuple
'''
fruits = ('banana', 'orange', 'apple', 'coconut')

# fruits = tuple(sorted(fruits))
fruits = tuple(sorted(fruits, reverse=True))
print(fruits)
'''

# Dictionary
'''
fruits = {'banana': 105, 'orange': 73, 'apple': 72, 'coconut': 354}

# fruits = dict(sorted(fruits.items()))
# fruits = dict(sorted(fruits.items(), key = lambda item: item[0], reverse=True))
# fruits = dict(sorted(fruits.items(), key = lambda item: item[1]))
fruits = dict(sorted(fruits.items(), key = lambda item: item[1], reverse=True))
print(fruits)
'''

# Objects
class Fruits:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def __repr__(self):
        return f'{self.name}: {self.calories}'
    

fruits = [Fruits('banana', 105), Fruits('apple', 72),
          Fruits('orange', 73), Fruits('coconut', 354)]

# fruits = sorted(fruits, key = lambda fruit: fruit.name)
# fruits = sorted(fruits, key = lambda fruit: fruit.name, reverse=True)
# fruits = sorted(fruits, key = lambda fruit: fruit.calories)
fruits = sorted(fruits, key = lambda fruit: fruit.calories, reverse=True)
print(fruits)