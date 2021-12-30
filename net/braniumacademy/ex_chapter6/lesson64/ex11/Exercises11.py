def is_symmetry(array):
    """This function check whether or not array is symmetry"""
    size = len(array)
    for index in range(0, int(size / 2)):
        if array[index] != array[size - 1 - index]:
            return False
    return True


with open('input11.txt') as reader, open('output11.txt', 'w') as writer:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            writer.write(f"Test {i}:\nN INVALID\n")
        else:
            writer.write(f"Test {i}:\n")
            if is_symmetry(arr):
                writer.write("YES\n")
            else:
                writer.write("NO\n")
