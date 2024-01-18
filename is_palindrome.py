# Write a recursive function to check if a given word is a palindrome or not

def is_palindrome(string):
    # Base case: if the length of the string is 1, it's a palindrome
    if len(string) == 1:
        return True
    
    # Recursive case: check if the first and last letters are the same,
    # and then call the function again with the string excluding the first and last letters
    return (string[0] == string[-1] and is_palindrome(string[1:-1]))

# Test cases
print(is_palindrome("madam"))  # True
print(is_palindrome("apple"))  # False