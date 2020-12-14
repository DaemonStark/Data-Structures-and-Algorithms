def bubblesort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])


if __name__ == '__main__':
    arr = [int(i) for i in input().split()]
    temp = []
    bubblesort(arr)
    print("In ascending order")
    print(arr)
    temp = arr
    temp.sort()
    print(temp)
