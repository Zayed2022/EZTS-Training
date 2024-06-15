class Animal:
    name = ""
    def caneat(self):
        print("I can eat")
class Dog(Animal):
    def eat(self):
        print("I like to eat parle G")
labrador = Dog()
labrador.eat()
labrador.caneat()