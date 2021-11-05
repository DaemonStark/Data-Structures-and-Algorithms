# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2; sort the array in ascending order.
    """
    # We can use the built-in sort() function to sort the list.
    # The sort() function sorts the list in place, so we don't need to return anything.
    input_list.sort()

if __name__ == '__main__':
    input_list = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
    sort_012(input_list)
    print(input_list)
