def draw_triangle(height):
    """Hàm vẽ và trả về hình tam giác đặc vuông góc trái dưới bằng các dấu *"""
    mtriangle = []
    for x in range(height):
        mtriangle.append([])
        for y in range(x + 1):
            mtriangle[x].append(' * ')
    return mtriangle


def show_triangle(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            print(f'{e}', end='')
        print()
    print()


h = int(input())
if h <= 0:
    print('ERROR')
else:
    triangle = draw_triangle(h)
    show_triangle(triangle)
