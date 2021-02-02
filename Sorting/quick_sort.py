#! /bin/python3

# PARTITIONING
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high, 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

# SORTING DRIVER FUNCTION
def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot-1)
        quickSort(arr, pivot+1, high)


if __name__ == '__main__':
    arr = list(map(int, input('Enter the array elements in random order: ').split()))
    quickSort(arr, 0, len(arr)-1)
    print(arr)