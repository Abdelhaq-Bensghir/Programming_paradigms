# Function to calculate the sum of squares of even numbers in a list
def calculate_sum_of_squares_of_even_numbers(numbers):
    # Initialize sum
    sum_of_squares = 0
    
    # Iterate through the list
    for number in numbers:
        # Check if the number is even
        if number % 2 == 0:
            # Square the number and add it to the sum
            sum_of_squares += number ** 2
    
    # Return the sum of squares
    return sum_of_squares

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculate and print the sum of squares of even numbers
print("Procedural Approach Result:", calculate_sum_of_squares_of_even_numbers(numbers))