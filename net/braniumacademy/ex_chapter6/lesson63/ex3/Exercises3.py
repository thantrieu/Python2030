def avg_even_index_elements(array):
    """This function calculate average value of even index elements"""
    s = 0
    count_element = 0
    for i in range(0, len(array)):
        if i % 2 == 0:
            s += array[i]
            count_element += 1
    return s / count_element


with open('input3.txt') as reader:
    t = int(reader.readline())
    for i in range(1, t + 1):
        n = int(reader.readline())
        arr = [int(x) for x in reader.readline().split()]
        if n <= 0:
            print(f"Test {i}:\nN INVALID")
        else:
            print(f"Test {i}:\n{avg_even_index_elements(arr)}")
