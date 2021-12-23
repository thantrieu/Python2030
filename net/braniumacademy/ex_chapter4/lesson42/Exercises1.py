def push(m_queue, data):
    """This function add new item at the end of the queue"""
    m_queue.append(data)


def push_front(m_queue, data):
    """This function add new item at the front of the queue"""
    m_queue.insert(0, data)


def is_empty(m_queue):
    """This function check queue is empty or not"""
    return len(m_queue) == 0


def pop(m_queue):
    """This function remove and return leftmost element of queue"""
    if is_empty(m_queue):
        return None
    return m_queue.pop(0)


def pop_back(m_queue):
    """This function remove and return rightmost element of queue"""
    if is_empty(m_queue):
        return None
    return m_queue.pop()


def front(m_queue):
    """This function return leftmost element of queue.
       Return None if queue is empty.
    """
    if is_empty(m_queue):
        return None
    return m_queue[0]


def back(m_queue):
    """This function return rightmost element of queue.
       Return None if queue is empty.
    """
    if is_empty(m_queue):
        return None
    return m_queue[size(m_queue) - 1]


def size(m_queue):
    """This function return queue's size"""
    return len(m_queue)


def print_elements(m_queue):
    """This function print all element of queue"""
    for x in m_queue:
        print(f"{x} ", end="")
    print()


option = "=============== OPTIONS ===============\n" \
         "1. Add new item at the end queue.\n" \
         "2. Add new item at the front queue.\n" \
         "3. Get leftmost element.\n4. Get rightmost element.\n" \
         "5. Get queue's size.\n6. Check queue is empty.\n" \
         "7. Pop leftmost element\n8. Pop rightmost element.\n" \
         "9. Print queue's elements.\n" \
         "0. Exit.\nYour choice? "
queue = []
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("==> Program terminated <==")
            break
        case 1:
            value = input("Enter an element: ")
            push(queue, value)
        case 2:
            value = input("Enter an element: ")
            push_front(queue, value)
        case 3:
            print(f"Leftmost element: {front(queue)}")
        case 4:
            print(f"Rightmost element: {back(queue)}")
        case 5:
            print(f"queue's size: {size(queue)}")
        case 6:
            print(f"Queue is empty?: {is_empty(queue)}")
        case 7:
            print(f"Removed leftmost element: {pop(queue)}")
        case 8:
            print(f"Removed rightmost element: {pop_back(queue)}")
        case 9:
            print("Elements of queue: ")
            print_elements(queue)
        case _:
            print("Wrong option. Please try again!")
