def binarySearch(arr, x, left, right):
    if right <= left: 
        return -1
    mid = (left + right) // 2
    if arr[left]<x and arr[right]<x:
        return -1
    elif arr[left]>=x:
        return left +1        
    elif arr[mid]>=x and arr[mid-1]<x:
        return mid +1 
    elif arr[mid+1]>=x and arr[mid]<x:
        return mid +2            
    elif x <= arr[mid]: 
        return binarySearch(arr, x, left, mid)
    else: 
        return binarySearch(arr, x, mid + 1, right)
# n = int(input())
# arr = list(map(int,input().split()))
# m =int(input())
# print(binarySearch(arr, m, left = 0, right = n-1), binarySearch(arr, 2*m, left = 0, right = n-1))

class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if  len(self.items) >0:
            return self.items.pop()
        print('error')

    def get_max(self):
        if  len(self.items) >0:
            return max(self.items)
        return None

def is_correct_bracket_seq(in_str) -> bool:
    stack = StackMax()
    for j in range(0, len(in_str)):
        if in_str[j]=='(':
            stack.push(in_str[j])
        else:
            if len(stack.items)> 0:
                if (in_str[j] == ')' and stack.items[-1]=='('):
                        stack.pop()
                else:
                    break
            else:
                stack.push(in_str[j])
                break
    if len(stack.items)==0:
        return True
    else:
        return False


# def gen_binary(n, prefix)->str:
#     if n == 0:
#         arr.append(prefix)
#         return prefix
#     else:
#         gen_binary(n - 1, prefix + ')')
#         gen_binary(n - 1, prefix + '(')  
# # (())
# arr = []
# gen_binary(int(input())*2,'')
# arr.sort()
# for i in arr:
#     if is_correct_bracket_seq(i)==True:
#         print(i)

def gen_binary(n,arr, m, prefix)->str:
    if m == n:
        arr.append(prefix)
    elif arr[m] == '2':
        gen_binary(n,arr, m+1, prefix + 'a')
        gen_binary(n,arr, m+1, prefix + 'b')
        gen_binary(n,arr, m+1, prefix + 'c')
    elif arr[m] == '3':
        gen_binary(n,arr, m+1, prefix + 'd')
        gen_binary(n,arr, m+1, prefix + 'e')
        gen_binary(n,arr, m+1, prefix + 'f')  
    elif arr[m] == '4':
        gen_binary(n,arr, m+1, prefix + 'g')
        gen_binary(n,arr, m+1, prefix + 'h')
        gen_binary(n,arr, m+1, prefix + 'i')               
    elif arr[m] == '5':
        gen_binary(n,arr, m+1, prefix + 'j')
        gen_binary(n,arr, m+1, prefix + 'k')
        gen_binary(n,arr, m+1, prefix + 'l')  
    elif arr[m] == '6':
        gen_binary(n,arr, m+1, prefix + 'm')
        gen_binary(n,arr, m+1, prefix + 'n')
        gen_binary(n,arr, m+1, prefix + 'o')  
    elif arr[m] == '7':
        gen_binary(n,arr, m+1, prefix + 'p')
        gen_binary(n,arr, m+1, prefix + 'q')
        gen_binary(n,arr, m+1, prefix + 'r')
        gen_binary(n,arr, m+1, prefix + 's')   
    elif arr[m] == '8':
        gen_binary(n,arr, m+1, prefix + 't')
        gen_binary(n,arr, m+1, prefix + 'u')
        gen_binary(n,arr, m+1, prefix + 'v')
    elif arr[m] == '9':
        gen_binary(n,arr, m+1, prefix + 'w')
        gen_binary(n,arr, m+1, prefix + 'x')
        gen_binary(n,arr, m+1, prefix + 'y')
        gen_binary(n,arr, m+1, prefix + 'z') 

# arr = list(input())
# arr = []
# gen_binary(len(arr), arr,0, '')
# print(*arr)

# n = int(input())
# arr = list(map(int,input().split(' ')))
# flag = True
# for k in range(0, n-1):
#     for i in range(0, n-1):
#         if arr[i]>arr[i+1]:   
#             flag = True         
#             arr[i],arr[i+1] = arr[i+1], arr[i]
#     if flag:
#         print(*arr)
#     flag =False
    
def merge(arr: list, left: int, mid: int, right: int):
    # arr = [0 for i in range(len(arr))]
    l, r, k = 0, 0, left
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    while l < len(left_arr) and r < len(right_arr): 
        if left_arr[l] <= right_arr[r]: 
            arr[k] = left_arr[l]
            l += 1
        else:
            # print(arr[k])
            arr[k] = right_arr[r]
            r += 1
        k += 1
    while l < len(left_arr): 
        arr[k] = left_arr[l] # перенеси оставшиеся элементы left в arr
        l += 1
        k += 1  
    while r < len(right_arr): 
        arr[k] = right_arr[r] # перенеси оставшиеся элементы right в arr
        r += 1
        k += 1
    return arr    

def merge_sort(arr: list, left: int, right: int):
    if left >= right:  # базовый случай рекурсии
        return 
    mid = ( left + right ) // 2 
    # if left == mid:
    #     mid = right   
    merge_sort(arr, left, mid)
    merge_sort(arr, mid+1, right)
    merge(arr,left,mid,right)


arr = [3,1,5,4,2]
merge_sort(arr, 0, 4)
print(arr)

