# Write a function to unflatten a dictionary

def unflatten_dict(my_dict):
    # Create a new dictionary to store the unflatten key-value pairs
    new_dict = dict()

    # Loop through the keys of the input dictionary
    for outer_key in my_dict.keys():
        # If there is a dot in the keys
        if "." in outer_key:
            # Split the key into three parts: the first letter, the dot, and the second letter
            new_outer_key, dot, inner_key = outer_key.partition(".")
            # If the first letter is not already in the new dictionary
            if new_outer_key not in new_dict.keys():
                # Create a new nested dictionary as the value for the first letter
                new_dict[new_outer_key] = dict()
            # Add the new, nested dictionary to the parent dictionary with the inner key and its value
            new_dict[new_outer_key][inner_key] = my_dict[outer_key]
        else:
            # If there is no dot in the key, we add the unchanged key-value pair to the new dict
            new_dict[outer_key] = my_dict[outer_key]

    return new_dict

# Example usage
input_dict = {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}
unflattened_dict = unflatten_dict(input_dict)
print(unflattened_dict)
# Expected Output: {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}