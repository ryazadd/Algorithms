# ID sent 50795013
def nearest_zero() -> str:
    """Возращает для всех чисел в последовательности
        расстояние до ближайшего нуля"""
    n: int = int(input())
    arr: List[int] = list(map(int, input().split()))
    left_zero: int = arr.index(0)
    right_zero: int = n-list(reversed(arr)).index(0)-1
    result: List[int] = arr
    for i in range(left_zero, n):
        if arr[i] != 0:
            result[i] = result[i-1]+1

    for i in range(right_zero, left_zero, -1):
        if arr[i] != 0:
            result[i] = min(result[i], result[i+1]+1)

    for i in range(left_zero, -1, -1):
        if arr[i] != 0:
            result[i] = result[i+1]+1

    return result


if __name__ == '__main__':
    result = nearest_zero()
    print(*result)
