def print_list(my_list):
    """This function print all elements in the list"""
    for x in my_list:
        print(f"{x} ", end="")
    print()


with open('input14.txt') as reader:
    t = int(reader.readline())
    for i in range(1, t + 1):
        arr = [x for x in reader.readline().split()]
        arr.sort(reverse=False)  # sort elements in list asc
        print_list(arr)
