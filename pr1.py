arr = [22, 33, 44, 55, 66, 77, 88, 99]

def lsearch(array, x):
    for i in range(len(array)):
        if array[i] == x:
            print("Element Found")
            return
    print("Element not Found")

lsearch(arr,44)

def bsearch(array, x):
    l = 0
    r = len(array) - 1
    
    while l <= r:
        mid = l + (r - l) // 2
        if array[mid] == x:
            print("Element Found")
            return
        elif array[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    print("Element not Found")

bsearch(arr,88)
