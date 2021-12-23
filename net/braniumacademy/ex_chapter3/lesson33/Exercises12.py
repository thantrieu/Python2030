def create_spiral_matrix(a, row_prev, row_next, col_prev, col_next, counter, bound, row):
    """This function create a spiral matrix and return it"""
    if counter >= bound:
        return
    for index in range(col_prev + 1, col_next + 1):
        if row_prev >= 0 and index < row:
            a[row_prev][index] = counter
            counter += 1
    col_prev -= 1
    if col_next < row:
        for index in range(row_prev + 1, row_next + 1):
            if index < row:
                a[index][col_next] = counter
                counter += 1
    row_prev -= 1
    if row_next < row:
        for index in range(col_next - 1, col_prev - 1, -1):
            if index >= 0:
                a[row_next][index] = counter
                counter += 1
    col_next += 1
    if col_prev >= 0:
        for index in range(row_next - 1, row_prev - 1, -1):
            if index >= 0:
                a[index][col_prev] = counter
                counter += 1
    row_next += 1
    create_spiral_matrix(a, row_prev, row_next, col_prev, col_next, counter, bound, row)


def show_matrix(matrix, row, col):
    for i_index in range(0, row):
        for j_index in range(0, col):
            print("{0:5}".format(matrix[i_index][j_index]), end="")
        print("\n")
    print()


t = int(input())
for x in range(1, t + 1):
    m_row = int(input())
    m_col = m_row
    arr = []  # Tạo list rỗng
    for i in range(0, m_row):  # tạo list chứa m_row hàng, mỗi hàng là 1 list
        arr.append([])
        for j in range(0, m_col):  # tạo list[i] chứa m_col cột, các phần tử ban đầu bằng 0
            arr[i].append(0)
    # các giá trị khởi tạo
    center_row_index = (m_row - 1) // 2
    center_col_index = (m_col - 1) // 2
    next_row = center_row_index + 1
    next_col = center_col_index + 1
    prev_row = center_row_index
    prev_col = center_col_index
    value = 1
    arr[center_col_index][center_row_index] = value
    value += 1
    upper_bound = m_row * m_col

    # tạo ma trận xoắn ốc
    create_spiral_matrix(arr, prev_row, next_row,
                         prev_col, next_col, value, upper_bound, m_row)
    # hiển thị kết quả
    print(f"Test {x}: ")
    show_matrix(arr, m_row, m_col)
