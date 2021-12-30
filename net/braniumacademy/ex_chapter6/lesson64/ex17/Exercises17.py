def read_matrix(mrow, mcol, mreader):
    """Hàm đọc vào ma trận từ bàn phím"""
    arr = [int(x) for x in mreader.readline().split()]
    matrix = []
    for i in range(mrow):
        matrix.append([])
        for j in range(mcol):
            matrix[i].append(arr[i * mcol + j])
    return matrix


def write_matrix(mwriter, matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            mwriter.write(f'{e} ')
        mwriter.write('\n')


with open('input17.txt') as reader, open('output17.txt', 'w') as writer:
    while True:
        data = reader.readline()
        if data == '':
            break
        row_str, col_str = data.split()
        row = int(row_str)
        col = int(col_str)
        if row <= 0 or col <= 0:
            reader.readline()  # đọc bỏ dòng data
            writer.write('ERROR\n')
        else:
            matrix_integer = read_matrix(row, col, reader)
            writer.write(f'{row} {col}\n')
            write_matrix(writer, matrix_integer)
