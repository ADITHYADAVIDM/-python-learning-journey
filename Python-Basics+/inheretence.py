class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def talk(self):
        print("Bark")


class Cat(Mammal):
    def talk(self):
        print("Meaw")

dog1 = Dog()
dog1.walk()