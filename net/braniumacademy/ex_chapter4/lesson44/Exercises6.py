def find_max_element(data):
    """This function find and print max elements in data"""
    data.sort()
    print(data[0])


t = int(input())
for i in range(1, t + 1):
    s1 = {int(x) for x in input().split()}
    s2 = {int(x) for x in input().split()}
    result = s1.intersection(s2)
    print(f'Test {i}:')
    if len(result) > 0:
        find_max_element(list(result))
    else:
        print('None')
