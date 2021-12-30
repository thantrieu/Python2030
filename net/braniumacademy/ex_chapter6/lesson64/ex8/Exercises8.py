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


with open('input8.txt') as reader, open('output8.txt', 'w') as writer:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            writer.write(f"Test {i}:\nN INVALID\n")
        else:
            min2 = find_min2(arr)
            max2 = find_max2(arr)
            if min2 == max2:
                writer.write(f"Test {i}:\nNOT AVAILABLE\n")
            else:
                writer.write(f"Test {i}:\n{min2} {max2}\n")
