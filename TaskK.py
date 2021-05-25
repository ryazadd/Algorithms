def merge(arr: list, left: int, mid: int, right: int):
    l, r, k = 0, 0, left
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    while l < len(left_arr) and r < len(right_arr): 
        if left_arr[l] <= right_arr[r]: 
            arr[k] = left_arr[l]
            l += 1
        else:
            arr[k] = right_arr[r]
            r += 1
        k += 1
    while l < len(left_arr): 
        arr[k] = left_arr[l] 
        l += 1
        k += 1  
    while r < len(right_arr): 
        arr[k] = right_arr[r]
        r += 1
        k += 1
    return arr    

def merge_sort(arr: list, left: int, right: int):
    if left >= right:
        return 
    mid = ( left + right ) // 2  
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr,left,mid,right)


array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
merge_sort(array, 0, len(array))
print(array)        
