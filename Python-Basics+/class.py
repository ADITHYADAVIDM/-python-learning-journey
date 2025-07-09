class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

    def display(self):
        print(f"(x, y) = ({self.x}, {self.y})")


p1 = Point(10, 30)
p1.display()
p2 = Point(2, 5)
p2.display()