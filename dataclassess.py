from dataclasses import dataclass, field

@dataclass (frozen=True)
class Person:
    name: str
    age: int
    password: str = field(repr=False)
    is_alive: bool = True

    def __post_init__(self):
        if not self.age >= 0:
            raise ValueError('Age cannot be negative')

person1 = Person('Spongebob', 30, 'pineapple1')
person2 = Person('Patrick', 35, 'password')

print(person1)
print(person2)
print(person1 == person2)