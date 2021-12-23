t = int(input())
for i in range(1, t + 1):
    s1 = {x for x in input().split()}
    s2 = {x for x in input().split()}
    result = s1.intersection(s2)
    print(f'Test {i}:')
    if len(result) > 0:
        print(f'{result}')
    else:
        print('{}')
