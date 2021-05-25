def get_pivot(data, start, end):
    mid = (start + end) // 2
    result = [data[start], data[mid], data[end]]
    for i in range(-1, len(result) - 1):
        if result[i + 1] < result[i]:
            result[i], result[i + 1] = result[i + 1], result[i]

    return result[1]


def partition(data, start, end):
    pivot = get_pivot(data, start, end)
    left, right = start, end
    while True:
        while data[left] < pivot:
            left += 1
        while data[right] > pivot:
            right -= 1
        if left >= right:
            return right
        data[left], data[right] = data[right], data[left]


def effective_quick_sort(participant_data, start, end):
    if start < end:
        p = partition(participant_data, start, end)

        effective_quick_sort(participant_data, start, p)
        effective_quick_sort(participant_data, p + 1, end)


if __name__ == '__main__':
    file_in = open('input.txt')
    num_of_participants = int(file_in.readline())
    participant_data = [list] * num_of_participants
    for i in range(num_of_participants):
        temp = file_in.readline().strip().split() # Приведём в нужный формат
        temp[0], temp[1] = -int(temp[1]), temp[0]
        temp[2], temp[1] = temp[1], int(temp[2])

        participant_data[i] = temp
    file_in.close()

    effective_quick_sort(participant_data, 0, num_of_participants - 1)


    for participant in participant_data:
        print(participant[2])
