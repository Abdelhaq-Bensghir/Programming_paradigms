# Function to calculate the sum of squares of even numbers in a list using functional programming
def calculate_sum_of_squares_of_even_numbers(numbers):
    # Filter even numbers
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    
    # Calculate squares
    squares = map(lambda x: x ** 2, even_numbers)
    
    # Calculate sum
    sum_of_squares = sum(squares)
    
    # Return the sum of squares
    return sum_of_squares

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate and print the sum of squares of even numbers
print("Functional Approach Result:", calculate_sum_of_squares_of_even_numbers(numbers))