class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

class Dog(Animal):
    def __init__(self, name, age, gender):
        super().__init__(name, age)
        self.gender = gender

    def make_sound(self):
        print('Bark')

    def eat(self):
        print(f'{self.name} is eating')

class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print('Meow')

    def eat(self):
        print(f'{self.name} is eating')

class Cow(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print('Moo')

    def eat(self):
        print(f'{self.name} is eating')

class Hen(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('Cluck')

    def eat(self):
        print(f'{self.name} is eating')

    def lay_egg(self):
        print(f'{self.name} laid an egg')

if __name__ == "__main__":
    dog = Dog("It", 3, "Male")
    cat = Cat("Mushuk", 2, "Black")
    cow = Cow("Mol", 5, "Brown")
    hen = Hen("Tovuq", 1)

    dog.make_sound()
    dog.eat()

    cat.make_sound()
    cat.eat()

    cow.make_sound()
    cow.eat()

    hen.make_sound()
    hen.eat()
    hen.lay_egg()