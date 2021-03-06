"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = list()

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        return self.storage.pop()



class Stack:
    def __init__(self, value = None, next_node = None):
        self.size = 0
        # the value at this 
        self.value = value
        self.next_node = next_node

    def __len__(self):
        return len(self.storage)

    def push(self, value):
        return self.storage.append(value)

    def pop(self):
        return self.storage.pop()
