# ID sent 51518496
def partition(arr, left, right):
    """Сравниваем элементы относительно опорного, 
        слева переносим элементы меньше опорного, 
        справа - больше"""
    pivot = arr[(left + right) // 2]
    l_pointer, r_pointer = left, right
    while True:
        while arr[l_pointer] < pivot:
            l_pointer += 1
        while arr[r_pointer]> pivot:
            r_pointer -= 1
        if l_pointer >= r_pointer:
            return r_pointer
        arr[l_pointer], arr[r_pointer] = arr[r_pointer], arr[l_pointer]

def better_quick_sort(arr, left, right):
    """Рекурсивно запускаем алгоритм"""
    if left < right:
        part = partition(arr, left, right)
        better_quick_sort(arr, left, part)
        better_quick_sort(arr, part + 1, right)

if __name__ == '__main__':
    class Candidate:
        """Класс участников соревнования и их результатов"""
        def __init__(self, name, tasks, fine):
            self.name = name
            self.tasks = tasks
            self.fine = fine 
            self.sort_key = (self.tasks, self.fine, self.name)
        
        def __lt__(self, other):
            return self.sort_key < other.sort_key

        def __gt__(self, other):
            return self.sort_key > other.sort_key

        def __repr__(self):
            return self.name

    with open('input.txt') as f:
        n = int(f.readline())
        arr = [0]*n
        for i in range(n):
            temp = f.readline().split()
            arr[i] = (Candidate(temp[0], -int(temp[1]), int(temp[2])))
    better_quick_sort(arr, 0, n - 1)
    print(*arr, sep='\n')

