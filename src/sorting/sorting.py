# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []
    a = 0
    b = 0
    while len(merged_arr) < elements:
        if a >= len(arrA):
            merged_arr.extend(arrB[b:])
        elif b >= len(arrB):
            merged_arr.extend(arrA[a:])
        elif arrA[a] <= arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        elif arrA[a] > arrB[b]:
            merged_arr.append(arrB[b])
            b += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    elif len(arr) == 2:
        return merge(arr[:1],arr[1:])
    else:
        half = (len(arr))//2
        arr = merge(merge_sort(arr[:half]),merge_sort(arr[half:]))
        return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass
    # Your code here


def merge_sort_in_place(arr, l, r):
    pass
    # Your code here
