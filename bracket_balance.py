from Class_stack import Stack


def is_balanced(expression):
    stack = Stack()
    open_brackets = '([{'
    close_brackets = ')]}'

    for char in expression:
        if char in open_brackets:
            stack.get_push(char)
        elif char in close_brackets:
            if stack.is_empty():
                return 'Несбалансированно'
            elif open_brackets.index(stack.peek_up()) != close_brackets.index(char):
                return 'Несбалансированно'
            else:
                stack.pop_the_top()

    if stack.is_empty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


# Примеры сбалансированных последовательностей скобок
print(is_balanced("(((([{}]))))"))  # Сбалансированно
print(is_balanced("[([])((([[[]]])))]{()}"))  # Сбалансированно
print(is_balanced("{{[()]}}"))  # Сбалансированно

# Примеры несбалансированных последовательностей скобок
print(is_balanced("}{}"))  # Несбалансированно
print(is_balanced("{{[(])]}}"))  # Несбалансированно
print(is_balanced("[[{())}]"))  # Несбалансированно
