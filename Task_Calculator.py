# ID success sended 51331583
class Stack:
    """Класс реализующий стек"""
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            print('error')
             

def calculator()->int:
    """Калькульятор, пример ввода: 3 4 + Вывод: 7"""
    input_arr = input().split()
    operation_dicts = {'+':lambda t, v: t+v,
                        '-':lambda t, v: v-t,
                        '*':lambda t, v: t*v,
                        '/':lambda t, v: v//t}
    for i in input_arr:
        if i.lstrip('-').isnumeric():
            stack_digits.push(int(i))
        else:
            temp1 = stack_digits.pop()  
            temp2 = stack_digits.pop()
            stack_digits.push(operation_dicts[i](temp1, temp2))            
    return(stack_digits.pop())

if __name__ == '__main__':
    stack_digits = Stack()
    print(calculator())
