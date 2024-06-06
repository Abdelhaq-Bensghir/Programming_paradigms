class SumOfSquaresCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def filter_even_numbers(self):
        return filter(lambda x: x % 2 == 0, self.numbers)
    
    def calculate_squares(self, numbers):
        return map(lambda x: x ** 2, numbers)
    
    def calculate_sum_of_squares(self, squares):
        return sum(squares)
    
    def get_result(self):
        even_numbers = self.filter_even_numbers()
        squares = self.calculate_squares(even_numbers)
        return self.calculate_sum_of_squares(squares)

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create an instance of SumOfSquaresCalculator and calculate the result
calculator = SumOfSquaresCalculator(numbers)
print("Object-Oriented Approach Result:", calculator.get_result())