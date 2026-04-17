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

    
