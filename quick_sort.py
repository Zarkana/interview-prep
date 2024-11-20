import random

# In place quick sort
def qsort(arr, start, stop_before):
    partition_size = stop_before - start
    print(f"partition_size: {partition_size}")
    # Repeat until the base case is reached (subarrays of size 0 or 1)
    if(partition_size) < 2:
        return
    else:
        # Partition the array:
        boundary = partition(arr, start, stop_before)
        # Recursively sort the left and right partitions
        qsort(arr, start, boundary + 1)
        qsort(arr, boundary+1, stop_before)

def partition(arr, start, stop_before):
    pivot_value = arr[start]
    # The partitioning step uses two pointers to scan the array:
    low = start - 1
    high = stop_before

    while True:
        # Move low pointer to the right until an element >= pivot is found
        low += 1
        # Find the element that needs to be swapped higher
        while arr[low] < pivot_value:
            low += 1
    
        # Move high pointer to the left until an element <= pivot is found
        high -= 1
        # Find the element that needs to be swapped lower
        while arr[high] > pivot_value:
            high -= 1

        if low >= high:
            # This continues until the pointers cross, and the pivot is placed in its correct position.
            return high
        
        arr[low], arr[high] = arr[high], arr[low]

def test(input, output):
    print(f"Unsorted: {input}")
    qsort(input, 0, len(input))
    print(f"Sorted: {input}")
    if input != output:
        print("FAILURE")
    else:
        print("SUCCESS")

test([0], [0])
test([0,1], [0,1])
test([1,0], [0,1])
test([0,0,0], [0,0,0])
test([3,2,1], [1,2,3])
test([1,5,3,2], [1,2,3,5])
test([5,-1,-2,0], [-2,-1,0,5])
test([1,0,0,0,0], [0,0,0,0,1])
test([0,0,1,0,0], [0,0,0,0,1])
test([0,0,0,0,1], [0,0,0,0,1])
