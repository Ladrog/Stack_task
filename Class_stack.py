

class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def get_push(self, item):
        self.items.append(item)

    def pop_the_top(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("удаление из пустого стека")

    def peek_up(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("вызов из пустого стека")

    def get_size(self):
        return len(self.items)


# stack = Stack()
# stack.get_push(3)
# stack.get_push(2)
# stack.get_push(1)
# print(stack.is_empty())
# print(stack.get_size())
# print(stack.peek_up())
# stack.pop_the_top()
# stack.pop_the_top()
# stack.pop_the_top()
# print(stack.is_empty())
