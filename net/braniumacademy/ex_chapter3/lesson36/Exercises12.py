def print_list(my_list):
    """This function print all elements in the list"""
    for x in my_list:
        print(f"{x} ", end="")
    print()


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    arr.sort()  # sort elements in list asc
    print_list(arr)
