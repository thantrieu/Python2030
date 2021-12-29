def print_list(my_list):
    """This function print all elements in the list"""
    for x in my_list:
        print(f"{x} ", end="")
    print()


with open('input12.txt') as reader:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        arr.sort()  # sort elements in list asc
        print(f'Test {i}:')
        print_list(arr)
