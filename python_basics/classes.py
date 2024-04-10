class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print('draw')

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')


point = Point(10,20)
person1 = Person("Sunmade")
bob = Person('Bob smith')
person1.talk()
bob.talk()