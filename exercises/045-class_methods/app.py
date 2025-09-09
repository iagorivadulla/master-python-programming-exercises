# Your code here

class MathOperations:
    def __init__(self, pi=3.14159):
        self.pi = pi

    def calculate_circle_area(self, r):
        return f"# Circle Area: {self.pi * r**2}"

mops = MathOperations()
circle_area = mops.calculate_circle_area(5)
print(circle_area)