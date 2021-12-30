def read_matrix(mreader, mrow):
    """Hàm đọc vào ma trận từ bàn phím"""
    matrix = []
    for index in range(mrow):
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


def transposition(matrix):
    """Hàm chuyển ma A thành ma trận chuyển vị của A."""
    mrow = len(matrix)
    mcol = len(matrix[0])
    result = []
    for index in range(mcol):
        result.append([])
        for j in range(mrow):
            result[index].append(matrix[j][index])
    return result


with open('input18.txt') as reader:
    data = reader.readline()
    while True:
        if data == '':
            break
        row_str, col_str = data.split()
        row = int(row_str)
        col = int(col_str)
        if row <= 0 or col <= 0:
            print('ERROR')
            row = abs(row)
            for i in range(row):
                reader.readline()
        else:
            matrix_integer = read_matrix(reader, row)
            show_matrix(matrix_integer)
            trans_matrix = transposition(matrix_integer)
            show_matrix(trans_matrix)
        data = reader.readline()
