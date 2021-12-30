def count_divisible_k(array, k):
    """This function count elements in list divisible by k"""
    count = 0
    for e in array:
        if e % k == 0:
            count += 1
    return count


with open('input10.txt') as reader, open('output10.txt', 'w') as writer:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n_str, k_str = reader.readline().split()
        n = int(n_str)
        k_value = int(k_str)
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            writer.write(f"Test {i}:\nN INVALID\n")
        elif k_value == 0:
            writer.write(f"Test {i}:\nK INVALID\n")
        else:
            writer.write(f"Test {i}:\n{count_divisible_k(arr, k_value)}\n")
