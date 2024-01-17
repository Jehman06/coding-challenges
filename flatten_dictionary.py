# Write a function to flatten a nested dictionary

def flatten_dict(my_dict):
    # Create a new empty dictionary
    new_dict = dict()

    # Loop through the outer keys of the input dictionary
    for outer_key in my_dict:
        if type(my_dict[outer_key]) == dict:
            # Because the value is a dictionary, we loop through its key-value pairs
            for key, value in my_dict[outer_key].items():
                # We create a new key composed of the outer key, a dot, and the inner key
                new_key = outer_key + "." + key
                # We assign the value to the new key in the flatten dictionary
                new_dict[new_key] = value # ("b.j": 2, "b.j": 3)

        else:
            # Because the value isn't a dictionary, we add the key-value pair unchanged to the flattened dictionary
            new_dict[outer_key] = my_dict[outer_key]

    return new_dict

# Example usage
input_dict = {'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}
flattened_dict = flatten_dict(input_dict)
print(flattened_dict)
# Expected Output: {'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}