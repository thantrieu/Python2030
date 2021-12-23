def max_len(data):
    """This function return max length of elements in list data"""
    value = 0
    for e in data:
        if len(e) > value:
            value = len(e)
    return value


def find_max_element(data):
    """This function find and print max elements in data"""
    data.sort()
    max_size = max_len(data)
    for e in data:
        if len(e) == max_size:
            print(e)


t = int(input())
for i in range(1, t + 1):
    s1 = {x for x in input().split()}
    s2 = {x for x in input().split()}
    result = s1.intersection(s2)
    print(f'Test {i}:')
    if len(result) > 0:
        find_max_element(list(result))
    else:
        print('None')
