from collections import deque


def push(m_queue, data):
    """This function add new item at the end of the queue"""
    m_queue.append(data)


def is_empty(m_queue):
    """This function check queue is empty or not"""
    return len(m_queue) == 0


def pop(m_queue):
    """This function remove and return leftmost element of queue"""
    if is_empty(m_queue):
        return None
    return m_queue.popleft()


def front(m_queue):
    """This function return leftmost element of queue"""
    if is_empty(m_queue):
        return None
    return m_queue[0]


def back(m_queue):
    """This function return rightmost element of queue"""
    if is_empty(m_queue):
        return None
    return m_queue[size(m_queue) - 1]


def size(m_queue):
    return len(m_queue)


option = "====================== OPTIONS ======================\n" \
         "1. Add new item.\n2. Get leftmost element.\n" \
         "3. Get rightmost element.\n4. Pop leftmost element.\n" \
         "5. Check queue is empty.\n6. Get queue's size.\n" \
         "0. Exit.\nYour choice? "
queue = deque()
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("==> Program terminated <==")
            break
        case 1:
            value = input("Enter a name: ")
            push(queue, value)
        case 2:
            print(f"Leftmost element: {front(queue)}")
        case 3:
            print(f"Rightmost element: {back(queue)}")
        case 4:
            print(f"Removed element: {pop(queue)}")
        case 5:
            print(f"Is queue empty? {is_empty(queue)}")
        case 6:
            print(f"Queue's size: {size(queue)}")
        case _:
            print("Wrong option.Please try again!")
