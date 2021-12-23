def avg_elements(array):
    """This function calculate average value of elements in list"""
    s = 0
    for x in array:
        s += x
    return s / len(array)


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n <= 0:
        print(f"Test {i}:\nN INVALID")
    else:
        print(f"Test {i}:\n{avg_elements(arr)}")
