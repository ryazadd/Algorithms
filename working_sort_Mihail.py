def merge(arr: list, left: int, mid: int, right: int) -> list:
    L, R = arr[left:mid], arr[mid:right]
    N, M = len(L), len(R)
    i = j = 0
    k = left
    while i < N and j < M:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
            k += 1
        else:
            arr[k] = R[j]
            j += 1
            k += 1
    while i < N:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < M:
        arr[k] = R[j]
        j += 1
        k += 1
    return arr
def merge_sort(arr: list, left: int, right: int) -> None:
    if (right - left) > 1:
        mid = left + (right - left) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid, right)
        merge(arr, left, mid, right)
        
array = [0,4,2,0,4,4,4,42,2,2,23,4,4,21,1]
merge_sort(array, 0, len(array))
print(array)        
