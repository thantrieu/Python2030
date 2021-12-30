def count_x(array, x):
    """This function count the occurent of x in list array"""
    count = 0
    for e in array:
        if x == e:
            count += 1
    return count


with open('input9.txt') as reader, open('output9.txt', 'w') as writer:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n_str, x_str = reader.readline().split()
        n = int(n_str)
        x_value = int(x_str)
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            writer.write(f"Test {i}:\nN INVALID\n")
        else:
            writer.write(f"Test {i}:\n{count_x(arr, x_value)}\n")
