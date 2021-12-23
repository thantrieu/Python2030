def is_symmetry(array):
    """This function check whether or not array is symmetry"""
    size = len(array)
    for index in range(0, int(size / 2)):
        if array[index] != array[size - 1 - index]:
            return False
    return True


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if n <= 0:
        print(f"Test {i}:\nN INVALID")
    else:
        print(f"Test {i}:", end="")
        if is_symmetry(arr):
            print("YES")
        else:
            print("NO")
