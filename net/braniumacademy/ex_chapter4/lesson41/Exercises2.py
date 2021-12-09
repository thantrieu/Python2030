def push(s, data):
    """This function add new item into stack"""
    s.append(data)


def is_empty(s):
    """This function check stack is empty or not"""
    return len(s) == 0


def pop(s):
    """This function remove and return top element of stack"""
    if is_empty(s):
        return None
    return s.pop()


def peek(s):
    """This function return top element of stack.
       Return None if stack is empty.
    """
    if is_empty(s):
        return None
    return s[len(s) - 1]


def size(s):
    """This function return stack's size"""
    return len(s)


def is_symmetry(data, s):
    """This function check whether or not data is symmetry"""
    idx = 0
    while not is_empty(s):
        if pop(s) != data[idx]:
            return False
        idx += 1
    return True


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    numbers = [int(y) for y in input().split()]
    stack = []
    size = len(numbers)
    for index in range(size // 2, size):
        push(stack, numbers[index])
    if is_symmetry(numbers, stack):
        print(f"Test {i}: YES")
    else:
        print(f"Test {i}: NO")
