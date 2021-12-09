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


t = int(input())
for i in range(1, t + 1):
    words = input().split()
    stack = []
    for x in words:
        push(stack, x)
    while not is_empty(stack):
        print(f"{pop(stack)} ", end="")
    print()
