class Circle:
    def __init__(self, raduis):
        self.radius = raduis
    @property
    def compute_area(self):
        return 3.14 * self.radius * self.radius
    
a = Circle(150)
print(a.compute_area)


