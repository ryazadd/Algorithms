# f = input()
# s = input()
# first_string = list(f)
# second_string = list(s)
# i = j = 0
# first_len, second_len = len(first_string), len(second_string)
# while i < first_len and j < second_len:
#     if first_string[i] == second_string[j]:
#         i += 1
#     j += 1
# print(i == first_len)


n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
arr.sort()
clumb = arr[0]
result = []
result.append(clumb)
for i in range(1,n):
    if clumb[1] < arr[i][0]:
        clumb = arr[i]
        result.append(clumb)
    elif clumb[1] < arr[i][1]:
        clumb[1] = arr[i][1]

for item in result:
    print(*item)
