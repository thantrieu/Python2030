def create_spiral_matrix(a, row_start, row_end, col_start, col_end, counter):
    """This function create a spiral matrix and return it
     # B1: khởi tạo các biến row_start-chỉ số hàng đầu, row_end-chỉ số hàng cuối,
     # col_start-cột đầu, col_end-cột cuối.
     # B2: Lặp chừng nào tất cả các cạnh cấu thành ma trận xoắn ốc được duyệt:
     # B2.1: in ra hàng đầu tiên trong vùng đang xét của ma trận, tăng row_start lên 1.
     # B2.2: in ra cột cuối cùng trong vùng đang xét của ma trận, giảm col_end đi 1.
     # B2.3: in ra hàng cuối cùng trong vùng đang xét của ma trận, giảm row_end đi 1.
     # B2.4: in ra cột đầu tiên trong vùng đang xét của ma trận, tăng col_start lên 1.
    """
    if row_start >= row_end or col_start >= col_end:
        return  # điểm dừng
    # gán giá trị cho hàng đầu trong số các hàng còn lại
    for index in range(col_start, col_end):  # c
        a[row_start][index] = counter
        counter += 1
    row_start += 1  # chuyển đến hàng kế tiếp ở lần duyệt tới
    # gán giá trị cho cột cuối trong số các cột còn lại
    for index in range(row_start, row_end):
        a[index][col_end - 1] = counter
        counter += 1
    col_end -= 1  # chuyển tới cột liền trước ở lần duyệt tới
    # gán giá trị cho hàng cuối trong các hàng còn lại
    if row_start < row_end:
        for index in range(col_end - 1, col_start - 1, -1):
            a[row_end - 1][index] = counter
            counter += 1
        row_end -= 1  # chuyển tới hàng liền trước ở lần duyệt tới
    # gán giá trị cho cột đầu trong số các cột còn lại
    if col_start < col_end:
        for index in range(row_end - 1, row_start - 1, -1):
            a[index][col_start] = counter
            counter += 1
        col_start += 1  # chuyển đến cột kế tiếp ở lần duyệt tới
    create_spiral_matrix(a, row_start, row_end, col_start, col_end, counter)


def show_matrix(matrix, row, col):
    for i_index in range(0, row):
        for j_index in range(0, col):
            print("{0:5}".format(matrix[i_index][j_index]), end="")
        print("\n")
    print()


t = int(input())
for x in range(1, t + 1):
    row_str, col_str = input().split()
    m_row = int(row_str)
    m_col = int(col_str)
    arr = []  # Tạo list rỗng
    for i in range(0, m_row):  # tạo list chứa m_row hàng, mỗi hàng là 1 list
        arr.append([])
        for j in range(0, m_col):  # tạo list[i] chứa m_col cột, các phần tử ban đầu bằng 0
            arr[i].append(0)
    # các giá trị khởi tạo
    value = 1
    start_r = 0
    start_c = 0
    # tạo ma trận xoắn ốc
    create_spiral_matrix(arr, start_r, m_row, start_c, m_col, value)
    # hiển thị kết quả
    print(f"Test {x}: ")
    show_matrix(arr, m_row, m_col)
