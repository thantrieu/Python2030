def draw_rect(row, col):
    """Hàm vẽ và trả về hình chữ nhật đặc bằng các dấu *"""
    rect = []
    for x in range(row):
        rect.append([])
        for y in range(col):
            rect[x].append(' * ')
    return rect


def show_rect(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    for x in matrix:
        for e in x:
            print(f'{e}', end='')
        print()
    print()


row_str, col_str = input().split()
row = int(row_str)
col = int(col_str)
if row <= 0 or col <= 0:
    print('ERROR')
else:
    rectangle = draw_rect(row, col)
    show_rect(rectangle)
