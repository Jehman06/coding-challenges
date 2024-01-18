# Write a recursive function to calculate the Fibonacci number for a given position (num)

def fibonacci(num):
    # Base case: if the position is 2, return the Fibonacci number 1
    if num == 2:
        return 1
    # Base case: if the position is 1, return the Fibonacci number 0
    elif num == 1:
        return 0
    else:
        # Recursive step: calculate the Fibonacci number for the given position
        return fibonacci(num-1) + fibonacci(num - 2)

# Example usage
print(fibonacci(9)) # Return the fibonacci number 21