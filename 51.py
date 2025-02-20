class America:
    def __init__(self):
        print("This is the Parent Class")
class NewYork(America):
    def __init__(self):
        super().__init__()
        print("This is the Child class")

a = America()
b = NewYork()