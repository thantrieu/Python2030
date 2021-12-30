def draw_triangle(height):
    """Hàm vẽ và trả về hình tam giác đặc vuông góc trái dưới bằng các dấu *"""
    mtriangle = []
    for x in range(height):
        mtriangle.append([])
        for y in range(x + 1):
            mtriangle[x].append(' * ')
    return mtriangle


def write_triangle(mwriter, matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            mwriter.write(f'{e}')
        mwriter.write('\n')


with open('input23.txt') as reader, open('output23.txt', 'w') as writer:
    data = reader.readline()
    while True:
        if data == '':
            break
        h = int(data)
        if h <= 0:
            writer.write('ERROR\n')
        else:
            triangle = draw_triangle(h)
            write_triangle(writer, triangle)
        data = reader.readline()
