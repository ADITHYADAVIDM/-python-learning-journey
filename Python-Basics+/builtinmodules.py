import random


for i in range(3):
    print(random.random())
    print(random.randint(10, 20))

# to work with list
members = ["john", "Jake", "David", "Robert"]
print(random.choice(members)) # pass in the name of the list

class Dice:
    def roll(self):
        return((random.randint(1, 6), random.randint(1, 6)))


d1 = Dice()
print(d1.roll())