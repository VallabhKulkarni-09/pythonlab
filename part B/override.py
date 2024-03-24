class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def perimeter(self):
        return 4 * (self.length + self.width + self.height)

class VolumeBox(Box):
    def volume(self):
        return self.length * self.width * self.height

    def perimeter(self):
        return 2 * (self.length + self.width + self.height)

length = 3
width = 4
height = 5
box_instance = VolumeBox(length, width, height)

print("Perimeter of the box:", box_instance.perimeter())
print("Volume of the box:", box_instance.volume())
