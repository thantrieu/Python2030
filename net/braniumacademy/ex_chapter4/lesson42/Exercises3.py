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
    """This function return the number of element in queue"""
    return len(m_queue)


def merge(que1, que2):
    """Hàm trộn các phần tử vào hàng đợi theo thứ tự tăng dần."""
    other = deque()
    while not is_empty(que1) and not is_empty(que2):
        if front(que1) <= front(que2):
            push(other, pop(que1))
        else:
            push(other, pop(que2))
    while not is_empty(que1):
        push(other, pop(que1))
    while not is_empty(que2):
        push(other, pop(que2))
    return other


def print_result(q):
    """Hàm hiển thị các phần tử của hàng đợi."""
    for x in q:
        print(f'{x} ', end='')
    print()


t = int(input())
for i in range(1, t + 1):
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    q1 = deque(l1)
    # for x in l1:
    #     push(q1, x)
    q2 = deque(l2)
    # for y in l2:
    #     push(q2, y)
    result = merge(q1, q2)
    print_result(result)
    del result
