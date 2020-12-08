# Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

def sort012(arr, n):
    low = 0
    high = n - 1
    mi = 0
    while(mi <= high):
        if(arr[mi] == 0):
            arr[low], arr[mi] = arr[mi], arr[low]
            low += 1
            mi += 1
        elif (arr[mi] == 1):
            mi += 1
        else:
            arr[mi], arr[high] = arr[high], arr[mi]
            high += 1
    return arr


def printarray(arr):
    for each in arr:
        print(each)
    return


if __name__ == '__main__':
    n = int(input())
    arr = (int(i) for i in input().split()[:n])
    array = sort012(arr, n)
    print(printarray(array))
