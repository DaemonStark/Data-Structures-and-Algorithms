def kthSmallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    arr.sort()
    kthsmall = arr[k-1]
    return kthsmall


# Driver Code
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        print(kthSmallest(arr, 0, n-1, k))


# PASSED
# Problem Solved on GFG(Practice)
# Input:
# 2
# 6
# 7 10 4 3 20 15
# 3
# 5
# 7 10 4 20 15
# 4

# Output:
# 7
# 15

# Explanation:
# Testcase 1: 3rd smallest element in the given array is 7.
# Testcase 2: 4th smallest element in the given array is 15.
