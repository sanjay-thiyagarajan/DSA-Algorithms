#! /bin/python3

def linear_search(arr, key):
    for i in range(0,len(arr)):
        if arr[i] == key:
            return i 
    return -1

if __name__ == '__main__':
    arr = list(map(int, input('Enter the elements of the array: ').split()))
    key = int(input('Enter the key to be searched for: '))
    res = linear_search(arr, key)
    if res == -1:
        print('Element not found')
    else:
        print('Element found at index [{}]'.format(res))