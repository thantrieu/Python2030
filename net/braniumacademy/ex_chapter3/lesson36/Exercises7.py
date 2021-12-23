def find_min(array):
    """This function return minimum value in list"""
    value = arr[0]
    for x in array:
        if x < value:
            value = x
    return value


def find_max(array):
    """This function return maximum value in list"""
    value = arr[0]
    for x in array:
        if x > value:
            value = x
    return value


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n <= 0:
        print(f"Test {i}:\nN INVALID")
    else:
        print(f"Test {i}:\n{find_min(arr)} {find_max(arr)}")
