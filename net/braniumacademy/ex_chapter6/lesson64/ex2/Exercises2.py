def avg_elements(array):
    """This function calculate average value of elements in list"""
    s = 0
    for x in array:
        s += x
    return s / len(array)


with open('input2.txt') as reader, open('output2.txt', 'w') as writer:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            writer.write(f"Test {i}:\nN INVALID\n")
        else:
            writer.write(f"Test {i}:\n{avg_elements(arr)}\n")
