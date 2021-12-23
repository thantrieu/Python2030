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


def find_max2(array):
    """This function find and return second max value in list"""
    max_value = find_max(array)
    second = max_value
    for x in array:
        if x != max_value:
            second = x
            break
    for x in array:
        if x > second and x != max_value:
            second = x
    return second


def find_min2(array):
    """This function find and return second min value in list"""
    min_value = find_min(array)
    second = min_value
    for x in array:
        if x != min_value:
            second = x
            break
    for x in array:
        if x < second and x != min_value:
            second = x
    return second


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n <= 0:
        print(f"Test {i}:\nN INVALID")
    else:
        min2 = find_min2(arr)
        max2 = find_max2(arr)
        if min2 == max2:
            print("NOT AVAILABLE")
        else:
            print(f"Test {i}:\n{min2} {max2}")
