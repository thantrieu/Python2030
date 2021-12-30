def read_matrix(mreader, mrow):
    """Hàm đọc vào ma trận từ bàn phím"""
    matrix = []
    for index in range(mrow):
        matrix.append([int(x) for x in mreader.readline().split()])
    return matrix


def write_matrix(writer, matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    writer.write(f'{len(matrix)} {len(matrix[0])}\n')
    for x in matrix:
        for e in x:
            writer.write(f'{e} ')
        writer.write('\n')


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


with open('input18.txt') as reader, open('output18.txt', 'w') as writer:
    data = reader.readline()
    while True:
        if data == '':
            break
        row_str, col_str = data.split()
        row = int(row_str)
        col = int(col_str)
        if row <= 0 or col <= 0:
            writer.write('ERROR\n')
            row = abs(row)
            for i in range(row):
                reader.readline()
        else:
            matrix_integer = read_matrix(reader, row)
            write_matrix(writer, matrix_integer)
            trans_matrix = transposition(matrix_integer)
            write_matrix(writer, trans_matrix)
        data = reader.readline()
