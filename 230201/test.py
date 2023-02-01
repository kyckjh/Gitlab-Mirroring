def ar(arr):
    arr = [1,2,3]
    return arr
    
arr = [1]
arr += ar(arr)
print(arr)