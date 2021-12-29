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


with open('input7.txt') as reader:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            print(f"Test {i}:\nN INVALID")
        else:
            print(f"Test {i}:\n{find_min(arr)} {find_max(arr)}")
