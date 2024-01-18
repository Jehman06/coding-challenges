# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# The length of the array is within the range [2, 10^4].
# Each element in the array is within the range [-10^9, 10^9].
# The target is within the range [-10^9, 10^9].

def two_sums(nums, target):
    # Loop through the numbers in the array
    for i in range(len(nums) - 1):
        # Create another loop with range i + 1 to sum all numbers
        for j in range(i + 1, len(nums)):
            # If the sum of the numbers is equal to the target
            if nums[i] + nums[j] == target:
                # Return the indices of the found pair
                return [nums[i], nums[j]]
    # If no pairs were found for the target, return None
    return None

# Example usage
nums = [2, 7, 11, 15]
target = 17
result = two_sums(nums, target)

if result:
    print(f"Pair found: {result}")
else:
    print(f"No pairs found for the target {target}")