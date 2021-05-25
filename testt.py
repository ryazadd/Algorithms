def merge_sort(array, left_index, right_index):
    if (right_index - left_index) > 1:
        middle = left_index + (right_index - left_index) // 2
        merge_sort(array, left_index, middle)
        merge_sort(array, middle, right_index)
        merge(array, left_index, right_index, middle)

def merge(array, left_index, right_index, middle):
    left_copy = array[left_index:middle]
    right_copy = array[middle:right_index]
    l = 0
    r = 0
    k = left_index
    while l < len(left_copy) and r < len(right_copy):
        if left_copy[l] <= right_copy[r]:
            array[k] = left_copy[l]
            l += 1
        else:
            array[k] = right_copy[r]
            r += 1
        k += 1
    while l < len(left_copy):
        array[k] = left_copy[l]
        l += 1
        k += 1
    while r < len(right_copy):
        array[k] = right_copy[r]
        r += 1
        k += 1

# array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
# merge_sort(array, 0, len(array))
# print(array)        
