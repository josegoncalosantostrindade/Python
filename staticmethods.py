class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f'{self.name} = {self.position}'
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
        return position in valid_positions
    

employee1 = Employee('Eugene', 'Manager')
employee2 = Employee('Squidward', 'Cashier')
employee3 = Employee('Spongebob', 'Cook')


print(Employee.is_valid_position('Rocket Scientist'))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

print(employee1.is_valid_position(employee1.position))
print(employee2.is_valid_position(employee2.position))
print(employee3.is_valid_position(employee3.position))