# ID success sended 51332556
class Deque:
    """Класс реализующий двухстороннюю очередь"""
    def __init__(self, n):
        self.__queue = [None] * n
        self.__max_n = n
        self.__head = 0
        self.__tail = 0
        self.__size = 0 
       
    def is_empty(self):
        return self.__size == 0
  
    def push_back(self, x):
        if self.__size != self.__max_n:
            self.__queue[self.__tail] = x
            self.__tail = (self.__tail + 1) % self.__max_n
            self.__size += 1
        else:
            raise IndexError
    
    def push_front(self, x):
        if self.__size != self.__max_n:
            temp_index = (self.__head - 1) % self.__max_n
            self.__queue[temp_index] = x
            self.__head = temp_index
            self.__size += 1
        else:
            raise IndexError

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.__queue[self.__head]
        self.__queue[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_n
        self.__size -= 1
        return x
    
    def pop_back(self):
        if self.is_empty():
            raise IndexError
        temp_index = (self.__tail - 1) % self.__max_n
        x = self.__queue[temp_index]
        self.__queue[temp_index] = None
        self.__tail = temp_index
        self.__size -= 1
        return x
    
if __name__ == '__main__':
    n = int(input())
    deque = Deque(int(input()))
    operation_dicts = {'pop_front': lambda t:print(deque.pop_front()),
                        'pop_back': lambda t:print(deque.pop_back()),
                        'push_front':lambda t :deque.push_front(int(t[1])),
                        'push_back':lambda t:deque.push_back(int(t[1]))}
    for i in range(0,n):
        input_string = input().split()
        try: 
            operation_dicts[input_string[0]](input_string)
        except IndexError:
            print('error')
