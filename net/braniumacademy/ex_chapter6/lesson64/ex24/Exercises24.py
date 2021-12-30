def draw_triangle(height):
    triangle = []
    for i in range(1, height + 1):
        triangle.append([])
        for j in range(1, 2 * height):
            if height - i + 1 <= j <= height + i - 1:
                triangle[i - 1].append(' * ')
            else:
                triangle[i - 1].append('   ')
    return triangle


def show_triangle(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            print(f'{e}', end='')
        print()


with open('input24.txt') as reader:
    data = reader.readline()
    while True:
        if data == '':
            break
        h = int(data)
        if h <= 0:
            print('ERROR')
        else:
            result = draw_triangle(h)
            show_triangle(result)
        data = reader.readline()
