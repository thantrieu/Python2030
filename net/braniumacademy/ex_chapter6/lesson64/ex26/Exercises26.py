def draw_triangle(height):
    triangle = []
    for i in range(1, height + 1):
        triangle.append([])
        for j in range(1, 2 * height):
            if j == h - i + 1 or i == h or j == h + i - 1:
                triangle[i - 1].append(' 1 ')
            else:
                triangle[i - 1].append('   ')
    return triangle


def writer_triangle(mwriter, matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            mwriter.write(f'{e}')
        mwriter.write('\n')


with open('input26.txt') as reader, open('output26.txt', 'w') as writer:
    data = reader.readline()
    while True:
        if data == '':
            break
        h = int(data)
        if h <= 0:
            writer.write('ERROR\n')
        else:
            result = draw_triangle(h)
            writer_triangle(writer, result)
        data = reader.readline()
