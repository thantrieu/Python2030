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


def is_operator(op):
    """This function check whether or not op is operator"""
    if op == '+' or op == '-' or op == '*' or op == '/' or \
            op == '//' or op == '^' or op == '**':
        return True
    return False


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


def calculate(a, b, op):
    """This function return result a op b"""
    match op:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case '^':
            return a ** b
        case _:
            return 0


def calculator(postfix_exp):
    stack = []
    elements = postfix_exp.split()
    for e in elements:
        if is_operator(e):
            b = float(pop(stack))
            a = float(pop(stack))
            result = calculate(a, b, e)
            push(stack, result)
        else:
            push(stack, e)
    return float(pop(stack))


def print_result(r):
    """This function print result of postfix expression"""
    for e in r:
        print(f'{e} ', end='')
    print()


t = int(input())
for i in range(1, t + 1):
    expression = input()
    expression = add_space(expression)
    print(f"{calculator(expression)}")
