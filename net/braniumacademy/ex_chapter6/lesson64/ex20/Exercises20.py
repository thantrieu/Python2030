def draw_plus_sign(row, col):
    rect = []
    for i in range(row):
        rect.append([])
        for j in range(col):
            if ((i == 0 or i == 8) and (4 <= j <= 8)
                    or (i == 1 or i == 2 or i == 6 or i == 7)
                    and (j == 4 or j == 8)
                    or ((i == 3 or i == 5) and (j < 5 or j > 7))
                    or (i == 4 and (j == 0 or j == 12))):
                rect[i].append("*")
            else:
                rect[i].append(" ")
    return rect


def write_rect(matrix):
    """Hàm hiển thị các phần tử trong ma trận"""
    with open('output20.txt', 'w') as writer:
        for x in matrix:
            for e in x:
                writer.write(f'{e}')
            writer.write('\n')


plus_sign = draw_plus_sign(9, 13)
write_rect(plus_sign)
