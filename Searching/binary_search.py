#! /bin/python3

def binary_search(arr, low, high, key):
    if high >= low:
        mid = (low + high)//2
        if arr[mid] == key:
            return mid 
        elif arr[mid] < key:
            return binary_search(arr, mid+1, high, key)
        elif arr[mid] > key:
            return binary_search(arr, low, mid-1, key)
    else:
        return -1

if __name__ == '__main__':
    arr = list(map(int, input('Enter the elements of the array: ').split()))
    key = int(input('Enter the key to be searched for: '))
    res = binary_search(arr, 0, len(arr)-1, key)
    if res == -1:
        print('Element not found')
    else:
        print('Element found at index [{}]'.format(res))
