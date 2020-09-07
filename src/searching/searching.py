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
def agnostic_binary_search(arr, target, start=0, end=None):
    if end is None:
        end = len(arr)
    if len(arr) <= 0:
        return -1
    index = start + (end - start)//2
    if arr[index] == target:
        return index
    elif start == end:
        return -1
    elif target < arr[index] and arr[0] < arr[index]:
        return binary_search(arr, target, start, index)
    elif target > arr[index] and arr[0] < arr[index]:
        return binary_search(arr, target, index, end)
    elif target < arr[index]:
        return binary_search(arr, target, index, end)
    elif target > arr[index]:
        return binary_search(arr, target, start, index)
