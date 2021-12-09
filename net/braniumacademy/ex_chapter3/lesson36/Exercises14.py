def print_list(my_list):
    """This function print all elements in the list"""
    for x in my_list:
        print(f"{x} ", end="")
    print()


t = int(input())
for i in range(1, t + 1):
    arr = [x for x in input().split()]
    arr.sort(reverse=False)  # sort elements in list asc
    print_list(arr)
