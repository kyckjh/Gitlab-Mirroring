def binary_search(key, arr):
    start = 0
    end = key-1
    while start < end:
        mid = (start+end)//2
        if arr[mid] == key:
            return True
        elif key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return False