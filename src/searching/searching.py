# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if len(arr) <= 0:
        return -1
    index = start + (end - start)//2
    if arr[index] == target:
        return index
    elif start == end:
        return -1
    elif target < arr[index]:
        return binary_search(arr, target, start, index)
    elif target > arr[index]:
        return binary_search(arr, target, index, end)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
def agnostic_binary_search(arr, target):
    ascending = True
    found = False
    if len(arr) <= 0:
        return -1
    if arr[0] > arr[-1]:
        ascending = False
    index = (len(arr)-1)//2
    max_index = len(arr)-1
    min_index = 0
    while not found:
        if arr[index] == target:
            return index
        elif max_index == min_index or index == min_index or index == max_index:
            return -1
        elif target < arr[index] and ascending:
            max_index = index
            index = index - (index - min_index)//2
        elif target > arr[index] and ascending:
            min_index = index
            index = index + (max_index-index)//2
        elif target > arr[index] and not ascending:
            max_index = index
            index = index - (index - min_index)//2
        elif target < arr[index] and not ascending:
            min_index = index
            index = index + (max_index-index)//2
        else:
            return -1
