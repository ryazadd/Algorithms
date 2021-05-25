# ID sent 51518469
def search(arr:list, search_item:int) -> int:
    """Поиск в сломанном массиве, подается массив, границы и искомый элемент"""
    left = 0
    right = len(arr)-1
    middle = (left + right) // 2
    while search_item != arr[middle] and left <= right: 
        if arr[left] <= search_item <= arr[middle]:
            right = middle
        elif arr[left] <= arr[middle]:
            left = middle+1
        elif arr[middle] <= search_item <= arr[right]:
            left = middle+1
        else:
            right = middle    
        middle = (left + right) // 2            
    if search_item == arr[middle]: 
        return middle
    return -1

        

if __name__ == "__main__":
    len_arr = int(input())
    search_item = int(input())
    arr = [int(i) for i in input().split()]
    print(search(arr, search_item))
