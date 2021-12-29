def read_matrix(mrow):
    """Hàm đọc vào ma trận từ bàn phím"""
    matrix = []
    for i in range(mrow):
        matrix.append([int(x) for x in input().split()])
    return matrix


def show_matrix(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    print(f'{len(matrix)} {len(matrix[0])}')
    for x in matrix:
        for e in x:
            print(f'{e} ', end='')
        print()
    print()


def transposition(matrix):
    """Hàm chuyển ma A thành ma trận chuyển vị của A."""
    mrow = len(matrix)
    mcol = len(matrix[0])
    result = []
    for i in range(mcol):
        result.append([])
        for j in range(mrow):
            result[i].append(matrix[j][i])
    return result


row_str, col_str = input().split()
row = int(row_str)
col = int(col_str)
if row <= 0 or col <= 0:
    print('ERROR')
else:
    matrix_integer = read_matrix(row)
    show_matrix(matrix_integer)
    trans_matrix = transposition(matrix_integer)
    show_matrix(trans_matrix)
