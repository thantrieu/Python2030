def read_matrix(mreader, mrow):
    """Hàm đọc vào ma trận từ bàn phím"""
    matrix = []
    for i in range(mrow):
        matrix.append([int(x) for x in mreader.readline().split()])
    return matrix


def show_matrix(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    print(f'{len(matrix)} {len(matrix[0])}')
    for x in matrix:
        for e in x:
            print(f'{e} ', end='')
        print()
    print()


def add_two_matrix(input_matrix1, input_matrix2):
    """Hàm chuyển ma A thành ma trận chuyển vị của A."""
    mrow = len(input_matrix1)
    mcol = len(input_matrix1[0])
    result = []
    for i in range(mrow):
        result.append([])
        for j in range(mcol):
            result[i].append(input_matrix1[i][j] + input_matrix2[i][j])
    return result


with open('input19.txt') as reader:
    data = reader.readline()
    while True:
        if data == '':
            break
        row_str, col_str, row_str2, col_str2 = data.split()
        row = int(row_str)
        row2 = int(row_str2)
        col = int(col_str)
        col2 = int(col_str2)
        matrix1 = read_matrix(reader, row)
        matrix2 = read_matrix(reader, row2)
        if row != row2 or col != col2:
            print('INVALID ACTION')
        else:
            matrix_sum = add_two_matrix(matrix1, matrix2)
            show_matrix(matrix_sum)
        data = reader.readline()
