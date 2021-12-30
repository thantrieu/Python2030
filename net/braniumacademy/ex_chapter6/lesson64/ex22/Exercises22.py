def draw_rect(mrow, mcol):
    """Hàm vẽ và trả về hình chữ nhật rỗng bằng các dấu *"""
    rect = []
    for x in range(mrow):
        rect.append([])
        for y in range(mcol):
            if x == 0 or x == mrow - 1 or y == 0 or y == mcol - 1:
                rect[x].append(' * ')
            else:
                rect[x].append('   ')
    return rect


def write_rect(mwriter, matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            mwriter.write(f'{e}')
        mwriter.write('\n')


with open('input22.txt') as reader, open('output22.txt', 'w') as writer:
    data = reader.readline()
    while True:
        if data == '':
            break
        row_str, col_str = data.split()
        row = int(row_str)
        col = int(col_str)
        if row <= 0 or col <= 0:
            writer.write('ERROR\n')
        else:
            rectangle = draw_rect(row, col)
            write_rect(writer, rectangle)
        data = reader.readline()
