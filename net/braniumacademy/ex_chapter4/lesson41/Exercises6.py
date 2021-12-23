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


def merge(s1, s2):
    """This function merge data of 2 stack into 1 stack in ascending order"""
    rstack = []  # Stack kết quả đảo ngược
    while not is_empty(s1) and not is_empty(s2):  # TH cả hai stack chưa rỗng
        if peek(s1) > peek(s2):  # Lấy phần tử đầu stack nào lớn hơn
            push(rstack, pop(s1))  # Đẩy vào stack đảo ngược
        else:
            push(rstack, pop(s2))
    while not is_empty(s1):  # Lấy các phần tử còn lại của stack s1
        push(rstack, pop(s1))
    while not is_empty(s2):  # Lấy các phần tử còn lại của stack s2
        push(rstack, pop(s2))
    stack = []  # Stack kết quả
    while not is_empty(rstack):  # Lấy các phần tử trong stack đảo ngược
        push(stack, pop(rstack))  # Đẩy vào stack đích
    return stack


def show_result(r):
    """This function show element in stack in ascending order"""
    for e in r:
        print(f'{e} ', end='')
    print()


# Main code run the test
t = int(input())
for i in range(1, t + 1):
    stack1 = [int(x) for x in input().split()]
    stack2 = [int(x) for x in input().split()]
    result = merge(stack1, stack2)  # Trộn hai stack lại thành 1 stack sắp xếp tăng dần
    print(f'Test {i}: ')
    show_result(result)
