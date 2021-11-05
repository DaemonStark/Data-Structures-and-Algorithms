# Quick Sort
# Using approach of divide and conquer
# We partition the array by using pivot element then sort the
# We need to implement 2 functions to fully implement quick sort

# 1. Partition
# put highest element as the pivot
# and then index as low - 1
# then use loop to find the smaller and greater elements and swap the elements to sort it

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    # Now we will put smaller elements to left and larger elements to the right of pivot
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # swap
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i+1], arr[high]) = (arr[high], arr[i+1])

    return i+1

# QuickSort Implementation


def quicksort(arr, low, high):
    if low < high:
        # select pivot position and put all the elements smaller than pivot to the left and larger than pivot to the right
        pi = partition(arr, low, high)

        quicksort(arr, low, pi-1)

        quicksort(arr, pi+1, high)


if __name__ == '__main__':
    data = [8, 7, 2, 1, 0, 9, 6]
    size = len(data)
    quicksort(data, 0, size - 1)
    print('Sorted Array in Ascending Order:')
    print(data)
    print("Reverse", data[::-1])
