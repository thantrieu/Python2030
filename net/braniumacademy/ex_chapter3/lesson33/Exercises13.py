def print_spiral_form(a, row_start, row_stop, col_start, col_stop):
    if row_start >= row_stop or col_start >= col_stop:
        return
    # gán giá trị cho hàng đầu trong số các hàng còn lại
    for i in range(col_start, col_stop):
        print(f"{a[row_start][i]} ", end="")
    row_start += 1
    # gán giá trị cho cột cuối trong số các cột còn lại
    for i in range(row_start, row_stop):
        print(f"{a[i][col_stop - 1]} ", end="")
    col_stop -= 1
    # gán giá trị cho hàng cuối trong các hàng còn lại
    if row_start < row_stop:
        for i in range(col_stop - 1, col_start - 1, -1):
            print(f"{a[row_stop - 1][i]} ", end="")
        row_stop -= 1
    # gán giá trị cho cột đầu trong số các cột còn lại
    if col_start < col_stop:
        for i in range(row_stop - 1, row_start - 1, -1):
            print(f"{a[i][col_start]} ", end="")
        col_start += 1

    # gọi đệ quy
    print_spiral_form(a, row_start, row_stop, col_start, col_stop)


t = int(input())
for x in range(1, t + 1):
    row_str, col_str = input("Nhập số hàng, số cột: ").split()
    m_row = int(row_str)
    m_col = int(col_str)
    arr = []  # Tạo list rỗng
    for index in range(0, m_row):  # tạo list chứa m_row hàng, mỗi hàng là 1 list
        arr.append([])
        for j in range(0, m_col):
            value = int(input(f"Phần tử hàng {index + 1} cột {j + 1}: "))
            arr[index].append(value)
    # hiển thị kết quả
    print(f"Test {x}: ")
    print_spiral_form(arr, 0, m_row, 0, m_col)
