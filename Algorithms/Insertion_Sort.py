arr = input().split()
n = len(arr)
i = 0
j = 0
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while(j >= 0 and arr[j] > key):
        arr[j+1] = arr[j]
        j = j-1

    arr[j+1] = key

for each in arr:
    print(each, end=" ")
