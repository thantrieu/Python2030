def show_result(data):
    """This function print result, the number occurrence of each word in list data"""
    unique_words = set()
    for e in words:
        if e not in unique_words:
            print(f'{e}-{words.count(e)}')


t = int(input())
for i in range(1, t + 1):
    words = [x for x in input().split()]
    print(f'Test {i}: ')
    show_result(words)
