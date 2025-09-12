# Your code here
class MathOperations:
    def __init__(self, pi = 3.141559):
        self.pi = pi
        

    def calculate_circle_area(self, r):
        return self.pi * (r ** 2)
    
    @staticmethod
    def add_numbers(n, m):
        return f"# Sum of Numbers : {n + m}"
    

math_operations_instance = MathOperations()
sum_of_numbers = print(MathOperations.add_numbers(10, 15))

print(math_operations_instance.calculate_circle_area(5))


