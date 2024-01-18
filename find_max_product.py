# Write a function that finds the maximum product of two integers in the array 
# without using any built-in sorting functions

def find_max_product(arr):
    max_product = 0

    # Loop through the entire list, excluding the last element to avoid index out of range
    for i in range(len(arr) - 1):
        # Multiply the current element with the next element in the list
        current_product = arr[i] * arr[i + 1]
        # Compare the product of current elements with the current maximum product
        if current_product > max_product:
            # If the current product is greater, update the maximum product
            max_product = current_product

    return max_product

# Example usage
arr = [2, 5, -1, 3, -4, 8, 6]
print(find_max_product(arr)) # Output: 48