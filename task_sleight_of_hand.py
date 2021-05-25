# ID sent 50795953
def sleight_of_hand() -> int:
    """Задана следующая игра:
        игроки могут нажать в один момент времени на k клавиш каждый.
        Если в момент времени t были нажаты все нужные клавиши,
        то игроки получают 1 балл.
        Возвращает число баллов, которое смогут заработать игроки,
        если будут нажимать на клавиши вдвоём."""
    k = int(input())
    field_numbers = ''
    for i in range(0, 4):
        field_numbers += input().replace('.', '')

    count_numbers = {}
    for i in field_numbers:
        count_numbers[i] = count_numbers.setdefault(i, 0)+1
    return(sum(value <= k*2 for value in count_numbers.values()))


if __name__ == '__main__':
    result = sleight_of_hand()
    print(result)
