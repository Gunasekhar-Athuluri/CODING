def binary_search(k,arr):
    n = len(arr)
    if n>1:
        mid = n//2
        if arr[mid] == k:
            print("Found",k)
        elif arr[mid] <k:
            binary_search(k,arr[mid:])
        else:
            binary_search(k,arr[:mid])
    
l = [3,6,7,8,12,14,15,17]
binary_search(8,l)
