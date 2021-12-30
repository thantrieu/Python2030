def draw_rect(edge):
    """Hàm vẽ và trả về hình chữ nhật rỗng bằng các dấu *"""
    rect = []
    for x in range(1, edge + 1):
        rect.append([])
        for y in range(1, edge + 1):
            if x == 1 or x == edge or y == 1 or y == edge or x == y or x + y == edge + 1:
                rect[x - 1].append(' * ')
            else:
                rect[x - 1].append('   ')
    return rect


def writer_rect(mwriter, matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            mwriter.write(f'{e}')
        mwriter.write('\n')


with open('input28.txt') as reader, open('output28.txt', 'w') as writer:
    data = reader.readline()
    while True:
        if data == '':
            break
        h = int(data)
        if h <= 0:
            writer.write('ERROR\n')
        else:
            rectangle = draw_rect(h)
            writer_rect(writer, rectangle)
        data = reader.readline()
