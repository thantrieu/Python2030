def avg_elements(array):
    """This function calculate average value of elements in list"""
    s = 0
    for x in array:
        s += x
    return s / len(array)


with open('input2.txt') as reader:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            print(f"Test {i}:\nN INVALID")
        else:
            print(f"Test {i}:\n{avg_elements(arr)}")
