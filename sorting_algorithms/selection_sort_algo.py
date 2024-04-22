def findSmallest(arr):
    """
    Finds the smallest item in an array.

    Args:
        arr (list): an array of items where we need to find the smallest item

    Returns:
        integer: an index of the smallest item.
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i 
    return smallest_index

def selectionSort(arr):
    """
    Sort an array from the smallest item to the largest.

    Args:
        arr (list): an array of items which we need to sort

    Returns:
        array: an array of sorted items.
    """
    newArr = []
    copiedArr = list(arr) # copy an array
    for i in range(len(copiedArr)):
        smallest_index = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest_index))
    return newArr

print(selectionSort([5, 3, 6, 2, 10,3]))