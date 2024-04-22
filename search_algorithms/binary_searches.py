def binary_search(arr, item):
    """
    Searches for an item in array using binary search algorithm.

    Args:
        arr (list): an array of items to search for an itemm.
        item (float): an iteam to search in an arry.

    Returns:
        integer: an indexx of the searched item.
    """
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low+high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list,7))
print(binary_search(my_list,-1))