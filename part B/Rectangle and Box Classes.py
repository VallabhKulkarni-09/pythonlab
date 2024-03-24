class Rectangle:
    def __init__(self, a, b,c):
        self.length = a
        self.width = b
        self.height=c
    def Area(self):
        print('Area of Rectangle is:', self.length * self.width)

    def Perimeter(self):
        print('Perimeter of Rectangle is:', 2 * (self.length + self.width))


class Box(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b,c)

    def Volume(self):
        print('Volume of Box:', self.length * self.width * self.height)

    def Perimeter(self):
        print('Perimeter of Box:', 2 * (self.length + self.width))

box = Box(4, 3, 2)
box.Area()
box.Perimeter()
box.Volume()
