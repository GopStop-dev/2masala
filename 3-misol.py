from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        ...

    @abstractmethod
    def move(self):
        ...

class Dog(Animal):
    def sound(self):
        print("Vov-Vov")

    def move(self):
        print("Yuguradi")

class Cat(Animal):
    def sound(self):
        print("miyov-miyov")

    def move(self):
        print("Yuradi")

class Bird(Animal):
    def sound(self):
        print("chirq-chirq")

    def move(self):
        print("Uchadi")

dog = Dog()
dog.sound()
dog.move()

cat = Cat()
cat.sound()
cat.move()

bird = Bird()
bird.sound()
bird.move()
