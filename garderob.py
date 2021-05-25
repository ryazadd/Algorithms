def counting_sort(array, k):
    counted_values = [0] * k
    for value in array:
        counted_values[value] += 1
    index = 0
    for value in range(k):
        for amount in range(1, counted_values[value]+1):
            array[index] = value
            index += 1 
n = input()
arr = list(map(int,input().split()))   
counting_sort(arr, 3)
print(*arr)
