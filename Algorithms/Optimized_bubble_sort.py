def bubblesort(arr):
    for i in range(len(arr)):
        swapped = True
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])
                swapped = False

        if swapped:
            break


if __name__ == '__main__':
    data = [int(i) for i in input().split()]
    bubblesort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
