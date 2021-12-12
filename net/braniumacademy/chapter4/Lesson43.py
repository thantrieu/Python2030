# Vẽ và lưu hình chữ nhật đặc bằng dấu * vào list lồng nhau
width = int(input("Nhập chiều rộng: "))
height = int(input("Nhập chiều cao: "))
rect = []
# Cách 1:
for row in range(height):
    rect.append([])
    for col in range(width):
        rect[row].append(' * ')

# Cách 2:
# for row in range(height):
#     rect.append([' * ' for x in range(width)])

# Hiển thị kết quả ra màn hình:
for row in rect:
    for e in row:
        print(f'{e}', end='')
    print()

# Nhập dữ liệu ma trận vào từ bàn phím và lưu vào list lồng nhau
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
matrix = []
# Cách 1:
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(int(input(f'matrix[{i}][{j}] = ')))

# Cách 2:
# for i in range(m):
#     matrix.append([int(x) for x in input(f"Các phần tử của hàng thứ {i}: ").split()])

for row in matrix:
    for e in row:
        print(f'{e} ', end='')
    print()
