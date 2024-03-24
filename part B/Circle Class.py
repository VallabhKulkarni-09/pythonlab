class Circle:
    def Area(self, radius):
        area = 3.142 * radius * radius
        print('Area of circle is:', area)

    def Perimeter(self, radius):
        peri = 2 * 3.142 * radius
        print('Perimeter of circle is:', peri)

c = Circle()
radius = int(input('Enter the radius\n'))
c.Area(radius)
c.Perimeter(radius)
