# Write a recursive binary search algorithm to check whether a given number is in an array
test_list = [9,45,76,32,789,553235,323,2,78,909,43,67,33,38,90987,123,659,327,682,1278,1776,1996,5]

# First, we need to sort the array in ascending order
test_list.sort()

def recursive_binary_search(data, num):
    # If the array's length is 0, there is no number to check
    if len(data) == 0:
        return False
    else:
        # The middle of the array is its length divided by 2 (rounded for an integer result)
        mid = len(data) // 2

        # If the value in the middle of the array is the number we're looking for, we return True
        if data[mid] == num:
            return True
        else:
            # If the number we're looking for is smaller than the number located in the middle of the array,
            # we repeat the process but only in the first half of the array
            if num < data[mid]:
                return recursive_binary_search(data[:mid], num)
            # Else we repeat the process in the second half of the array
            return recursive_binary_search(data[mid+1:], num)
        
# Example usage
target_number = 78
result = recursive_binary_search(test_list, target_number)
print(f"Is {target_number} present in the array? {result}")