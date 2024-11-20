import random

# In place quick sort
def qsort(arr, start, stop_before):
    partition_size = stop_before - start
    print(f"partition_size: {partition_size}")
    # Repeat until the base case is reached (subarrays of size 0 or 1)
    if(partition_size) < 2:
        return
    else:
        # Choose a random pivot element from the array
        pivot = random.randint(start, stop_before-1)
        # print(f"random_pivot: {pivot}, start: {start}, stop_before: {stop_before}")
        # Partition the array:
        pivot = partition(arr, start, stop_before, pivot)
        # Recursively sort the left and right partitions
        qsort(arr, start, pivot)
        qsort(arr, pivot+1, stop_before)

def partition(arr, start, stop_before, pivot):
    # The partitioning step uses two pointers to scan the array:
    low = start
    high = stop_before - 1
    pivot_value = arr[pivot]
    while low < high:
        # Find the element that needs to be swapped higher
        while low < pivot:
            if arr[low] >= pivot_value:
                break
            else:
                low += 1
    
        # Find the element that needs to be swapped lower
        while high > pivot:
            if arr[high] < pivot_value:
                break
            else:
                high -= 1

        
        if low >= high:
            # This continues until the pointers cross, and the pivot is placed in its correct position.
            return pivot
        else:
            arr[low], arr[high] = arr[high], arr[low]
            # # When pivot moves the pivot index must also move, otherwise we may have values that are no longer for sure less than or greater than the pivot value
            if low == pivot:
                pivot = high
            elif high == pivot:
                pivot = low


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
