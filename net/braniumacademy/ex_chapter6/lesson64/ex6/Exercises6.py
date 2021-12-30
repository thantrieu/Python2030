def is_reversible(m):
    """This function check whether or not n is reversible number"""
    if m < 0:
        m *= -1
    x = m
    r = 0
    while m > 0:
        r = r * 10 + m % 10
        m //= 10
    return r == x


def listed_reverse_numbers(mwriter, array):
    """This function listed all reverse numbers in list"""
    for index in range(0, len(array)):
        if is_reversible(arr[index]):
            mwriter.write(f"{arr[index]} ")
    mwriter.write('\n')


with open('input6.txt') as reader, open('output6.txt', 'w') as writer:
        t = int(reader.readline())
        for i in range(1, t + 1):
            n = int(reader.readline())
            arr = [int(x) for x in reader.readline().split()]
            if n <= 0:
                writer.write(f"Test {i}:\nN INVALID\n")
            else:
                writer.write(f"Test {i}:\n")
                listed_reverse_numbers(writer, arr)
