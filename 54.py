class Shape:
    def __init__(self):
        pass
    def shape_area(self):
        area = 0
        return area

class Square(Shape):
    def square_area(self, length):
        self.length = length
        return f"Area of Square is {self.length * self.length}"
    

# Outputs
a = Shape()
print(a.shape_area())


b = Square()
print(b.square_area(100))
