def read_matrix(mrow, mcol, mreader):
    """Hàm đọc vào ma trận từ bàn phím"""
    arr = [int(x) for x in mreader.readline().split()]
    matrix = []
    for i in range(mrow):
        matrix.append([])
        for j in range(mcol):
            matrix[i].append(arr[i * mcol + j])
    return matrix


def show_matrix(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            print(f'{e} ', end='')
        print()
    print()


with open('input17.txt') as reader:
    while True:
        data = reader.readline()
        if data == '':
            break
        row_str, col_str = data.split()
        row = int(row_str)
        col = int(col_str)
        if row <= 0 or col <= 0:
            reader.readline()  # đọc bỏ dòng data
            print('ERROR')
        else:
            matrix_integer = read_matrix(row, col, reader)
            print(f'{row} {col}')
            show_matrix(matrix_integer)
