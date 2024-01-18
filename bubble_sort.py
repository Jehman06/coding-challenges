# Write a bubble sort algorithm to sort a given list in ascending order

def bubble_sort(list):
    # Iterate through the entire list
    for i in range(len(list)):
        swapped = False
        
        # Display the current iteration
        print(f"Iteration {i + 1}")

        # Iterate through the list, compare adjacent, and swap if necessary
        for j in range(len(list) - 1):
            # Display the elements being compared
            print(f"Comparing {list[j], list[j + 1]}")

            if list[j] > list[j + 1]:
                # Swap the elements if they are in the wrong order
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            return

# Example usage: Sorting a sample list
sample_list = [1, 48, 32, 8, 25]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")