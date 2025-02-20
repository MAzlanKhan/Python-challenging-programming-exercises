class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    @property
    def area(self):
        return f"Area is {self.length * self.width}"
    
a = Rectangle(20, 30)
print(a.area)