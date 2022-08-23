# b1: nhập các phần tử của mảng
# b2: sắp xếp tăng dần với hàm sort()
# b3: hiển thị kết quả.

def print_list(my_list):
    """This function print all elements in the list"""
    for x in my_list:
        print(f"{x} ", end="")
    print()


def sort(my_list):
    """This function sort array elements in ascending order using bubble sort tecknic"""
    for i in range(0, len(my_list)):
        for j in range(len(my_list) - 1, i, -1):
            if my_list[j] < my_list[j - 1]:
                tmp = my_list[j]
                my_list[j] = my_list[j - 1]
                my_list[j - 1] = tmp


if __name__ == '__main__':
    arr = [int(x) for x in input('Array\'s elements: ').split()]  # chú ý kiểu float
    # nếu không thích thì gán
    # arr = [5, 3, 6, 2, 0, 1, 4, 8, 9, 7]
    print("Before sort: ", end="")
    print_list(arr)
    sort(arr)  # sort elements in list ascending order
    print("After sort: ", end="")
    print_list(arr)  # print result

# Array's elements: 1 9 5 2 0 4 6 9 7 3 0
# Before sort: 1 9 5 2 0 4 6 9 7 3 0
# After sort: 0 0 1 2 3 4 5 6 7 9 9
