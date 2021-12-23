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


def add_data_to_stack(elements):
    """This function push data into stack in ascending order"""
    stack = []
    for e in elements:
        # Nếu stack rỗng hoặc phần tử đầu stack nhỏ hơn e
        if is_empty(stack) or peek(stack) <= e:
            push(stack, e)  # Push e vào stack
        else:
            stack_tmp = []  # Tạo stack phụ để chứa các phần tử trong stack đích mà lớn hơn e
            top = peek(stack)  # Lần lượt lấy từng phần tử khỏi stack đưa sang stack phụ
            while top is not None and top > e:
                push(stack_tmp, top)
                pop(stack)
                top = peek(stack)
            # Push e vào stack đích
            push(stack, e)
            # Pop các phần tử của stack_tmp và đưa sang stack đích
            while peek(stack_tmp) is not None:
                push(stack, pop(stack_tmp))
    return stack


def show_result(r):
    """This function show element in stack in ascending order"""
    for e in r:
        print(f'{e} ', end='')
    print()


# Main code run the test
t = int(input())
for i in range(1, t + 1):
    m_elements = [int(x) for x in input().split()]
    result = add_data_to_stack(m_elements)
    print(f'Test {i}: ')
    show_result(result)
