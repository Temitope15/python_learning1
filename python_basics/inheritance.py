class Mammal:
    def walk(self):
        print("Walk")

class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat(Mammal):
    def be_annoying(self):
        print('Cats are annoying')

dog = Dog()
dog.bark()
cat = Cat()
cat.walk()