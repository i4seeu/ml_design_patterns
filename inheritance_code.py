class Animal:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} says: {dog.sound()}")
print(f"{cat.name} says: {cat.sound()}")
