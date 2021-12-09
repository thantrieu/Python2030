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


def precedentce(op):
    """This function return the precidence of operators"""
    match op:
        case '+' | '-':
            return 1
        case '*' | '/' | '//':
            return 2
        case '^' | '**':
            return 3
        case _:
            return 0


def add_space(data):
    """This function add space before and after operators"""
    data = data.replace('^', ' ^ ')
    data = data.replace('(', ' ( ')
    data = data.replace(')', ' ) ')
    data = data.replace('+', ' + ')
    data = data.replace('-', ' - ')
    data = data.replace('*', ' * ')
    data = data.replace('/', ' / ')
    return data


def infix_to_postfix(data):
    """This function convert infix to postfix expression"""
    elements = data.split()
    result = []
    stack = []
    for e in elements:
        if precedentce(e) > 0:  # e làn toán tử
            while not is_empty(stack) and precedentce(e) <= precedentce(peek(stack)):
                result.append(peek(stack))
                pop(stack)
            push(stack, e)
        elif e == ')':  # e là ngoặc đóng
            op = pop(stack)
            while op != '(':
                result.append(op)
                op = pop(stack)
        elif e == '(':  # e là dấu ngoặc mở (
            push(stack, e)
        else:  # e là toán hạng, thêm vào kết quả
            result.append(e)
    # pop cac phan tu con lai cua stack
    while not is_empty(stack):
        op = pop(stack)
        if op != '(':
            result.append(op)
    return result  # trả về kết quả


def print_result(r):
    """This function print result of postfix expression"""
    for e in r:
        print(f'{e} ', end='')
    print()


t = int(input())
for i in range(1, t + 1):
    expression = input()
    expression = add_space(expression)
    print_result(infix_to_postfix(expression))
