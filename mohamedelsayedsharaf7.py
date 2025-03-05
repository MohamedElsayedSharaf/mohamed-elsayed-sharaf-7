# You are given a list of student scores in a class. Your task is to sort the scores in ascending order using Insertion Sort.

#Example Input:
# scores = [85, 72, 96, 61, 77, 89]

# Expected Output:
# [61, 72, 77, 85, 89, 96]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be placed correctly
        j = i - 1

        # Move elements that are greater than 'key' one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key at the correct position
        arr[j + 1] = key

# Test the function
scores = [85, 72, 96, 61, 77, 89]
insertion_sort(scores)
print(scores)
