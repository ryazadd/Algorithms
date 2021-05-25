# описываем узел в списке:
class Node:  
    def __init__(self, value, next_item=None):  
        self.value = value  
        self.next_item = next_item


# выписываем весь список задач:
def print_vertex(node) -> None:
    while node:
        print(node.value)
        node = node.next_item

def get_node_by_index(node, index):
        while index:
                node = node.next_item
                index -= 1
        return node

def insert_node(head, index, value):
        if index == 0:
            return head.next_item
        previous_node = get_node_by_index(head, index-1)
        new_node.next = previous_node.next_item 
        previous_node.next = new_node
        return head 

def delete_node(head, index):
        if index == 0:
            return  head.next_item 
        previous_node = get_node_by_index(head, index-1)
        current_node = get_node_by_index(head, index)
        previous_node.next_item = current_node.next_item 
        return head         


def find_value(node, value):
    index = 0
    while node:        
        if node.value==value:
            return index
        node = node.next_item
        index +=1
    return -1


class DoubleConnectedNode:  
    def __init__(self, value, next=None, prev=None):  
        self.value = value  
        self.next = next  
        self.prev = prev

def naobor(node):
    while node:
        node.prev, node.next = node.next, node.prev
        head = node
        node = node.prev
    return head

class StackMaxEffective:
    
    def __init__(self):
        self.items = []
        self.max_items = []

    def push(self, item):
        if len(self.items) == 0:
            self.max_items.append(item)
        self.items.append(item)
        if item>self.max_items[-1]:
            self.max_items.append(item)
        else:
            self.max_items.append(self.max_items[-1])


    def pop(self):
        if len(self.items) >0:
            self.items.pop()
            return self.max_items.pop()
        print('error')

    def get_max(self):
        if  len(self.items) >0:
            return self.max_items[-1]
        return None

# n = int(input())
# st = StackMaxEffective()

# for i in range(0,n):
#     str_ = input()
#     if str_== 'get_max':
#         print(st.get_max())
#     elif str_=='pop':
#         st.pop()
#     else:
#         st.push(int(str_[4:]))

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
        print(stack.items)
        if in_str[j]=='(' or in_str[j]=='{' or in_str[j]=='[':
            stack.push(in_str[j])
        else:
            if len(stack.items)> 0:
                if ((in_str[j]=='}' and stack.items[-1]=='{' ) or  
                    (in_str[j] == ')' and stack.items[-1]=='(') or 
                    (in_str[j] == ']' and stack.items[-1] == '[')):
                        stack.pop()
                else:
                    break
            else:
                stack.push(in_str[j])
                break
    if len(stack.items)==0:
        print(True)
    else:
        print(False)
          
# is_correct_bracket_seq(input())

class MyQueueSized:
    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0 
       
    def is_empty(self):
        return self.size == 0
  
    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
        else:
            print('error')

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x 
    
    def peek(self):
        if not self.is_empty():
            print(self.queue[self.head])
        else:
            print(None)

# n = int(input())
# st = MyQueueSized(int(input()))

# for i in range(0,n):
#     str_ = input()
#     if str_== 'peek':
#         st.peek()
#     elif str_=='pop':
#         print(st.pop())
#     elif str_== 'size':
#         print(st.size)
#     else:
#         st.push(int(str_[4:]))


class Node:
    def __init__(self, value=None, next_item=None):
        self.value = value
        self.next_item = next_item

class Queue:
    def __init__(self):
        self.head = None

    def get(self):
        if self.head:
            print(self.head.value)
            self.head = self.head.next_item
        else:
            print('error')

    def put(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        item = self.head
        while item.next_item:
            item = item.next_item
        item.next_item = new_node

    def size(self):
        size = 0
        if self.head:
            item = self.head
            while item:
                item = item.next_item
                size += 1
        print(size)


n = int(input())
queue = Queue()

for i in range(0,n):
    str_ = input()
    if str_=='get':
        queue.get()
    elif str_== 'size':
        queue.size()
    else:
        queue.put(int(str_[4:]))
