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


def add_to_queue(nums, q):
    """Hàm chèn các phần tử vào hàng đợi theo thứ tự tăng dần."""
    for x in nums:
        if is_empty(q) or x >= back(q):
            push(q, x)
        else:
            other = deque()
            while not is_empty(q) and front(q) < x:
                push(other, pop(q))
            push(other, x)
            while not is_empty(q):
                push(other, pop(q))
            while not is_empty(other):
                push(q, pop(other))


def print_result(q):
    """Hàm hiển thị các phần tử của hàng đợi."""
    for x in q:
        print(f'{x} ', end='')
    print()


queue = deque()
t = int(input())
for i in range(1, t + 1):
    numbers = [int(x) for x in input().split()]
    add_to_queue(numbers, queue)
    print_result(queue)
    queue.clear()
