
class Animal:
    def __init__(self, age, name):
        self.age = 0
        if age > 0:
            self.age = age
        self.name = name
        print(f'Creating animal {self.name}, age: {self.age}')

    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}'
    
    def makeSound(self):
        print('???')

class Mammal(Animal):
    def __init__(self, age, name):
        super().__init__(age, name)
        print(f'Creating mammal')
        self.limbs = ['topleft','topright','bottomleft', 'bottomright']
    
    def __str__(self):
        return f'Name: {self.name}, Age: {self.age}, {self.limbs}'


class Cat(Mammal):
    def __init__(self, age, name, race):
        super().__init__(age, name)
        print(f'Creating cat')
        self.race = race

    def makeSound(self):
        print('Meow!!!')

class Dog(Mammal):
    def __init__(self, age, name, race):
        super().__init__(age, name)
        print(f'Creating dog')
        self.race = race

    def makeSound(self):
        print('Woof!!!')



zw1 = Cat(10, 'Romek', 'Dachowiec')
zw1.makeSound()

zw2 = Dog(10, 'Azor', 'Burek')
zw2.makeSound()

    
