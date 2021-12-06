def push(stack, data):
    """This function add new item into stack"""
    stack.append(data)


def is_empty(stack):
    """This function check stack is empty or not"""
    return len(stack) == 0


def pop(stack):
    """This function remove and return top element of stack"""
    if is_empty(stack):
        return None
    return stack.pop()


def peek(stack):
    """This function return top element of stack.
       Return None if stack is empty.
    """
    if is_empty(stack):
        return None
    return stack[len(stack) - 1]


def size(stack):
    """This function return stack's size"""
    return len(stack)


option = "=============== OPTIONS ===============\n" \
         "1. Add new item.\n2. Get top element.\n3. Pop top element.\n" \
         "4. Check stack is empty.\n5. Get stack's size.\n" \
         "0. Exit.\nYour choice? "
stack = []
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("==> Program terminated <==")
            break
        case 1:
            value = input("Enter a name: ")
            push(stack, value)
        case 2:
            print(f"Top element: {peek(stack)}")
        case 3:
            print(f"Removed element: {pop(stack)}")
        case 4:
            print(f"Is stack empty? {is_empty(stack)}")
        case 5:
            print(f"Stack's size: {size(stack)}")
        case _:
            print("Wrong option. Please try again!")
