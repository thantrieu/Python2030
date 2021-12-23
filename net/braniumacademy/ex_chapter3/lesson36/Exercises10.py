def count_divisible_k(array, k):
    """This function count elements in list divisible by k"""
    count = 0
    for e in array:
        if e % k == 0:
            count += 1
    return count


t = int(input())
for i in range(1, t + 1):
    n_str, k_str = input().split()
    n = int(n_str)
    k_value = int(k_str)
    arr = [int(x) for x in input().split()]
    if n <= 0:
        print(f"Test {i}:\nN INVALID")
    elif k_value == 0:
        print(f"Test {i}:\nK INVALID")
    else:
        print(f"Test {i}:\n{count_divisible_k(arr, k_value)}")
