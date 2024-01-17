# Write a binary search algorithm to check whether a given number is in an array
test_list = [9,45,76,32,789,553235,323,2,78,909,43,67,33,38,90987,123,659,327,682,1278,1776,1996,5]

# First, we need to sort the array in ascending order
test_list.sort()

def binary_search(data, num):
    """
    Perform binary search on a sorted array to check if a given number is present.

    Parameters:
        data (list): A sorted list to be searched.
        num (int): The number to be checked for presence in the array.

    Returns:
        bool: True if the number is found, False otherwise.
    """

    # Define the start and end indices of the array and a "found" boolean
    first = 0
    last = len(data)-1
    found = False

    # Loop through the array as long as the start index is smaller or equal to the end index, and found is False
    while first <= last and not found:
        # Calculate the middle index of the current search range
        mid = (first + last) // 2

        # Check if the middle element is equal to the target number
        if data[mid] == num:
            found = True
        else: 
            # If the target number is less than the middle element, adjust the search range to the left
            if num < data[mid]:
                last = mid - 1
            # If the target number is greater than the middle element, adjust the search range to the right
            else:
                first = mid + 1
    return found

# Example usage
target_number = 43
result = binary_search(test_list, target_number)
print(f"Is {target_number} present in the array? {result}")