import math

n = 12
# Tạo list chứa các số chính phương
squares = [x ** 2 for x in range(n)]
print(squares)
# Kết quả: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]

# Tạo list chứa cặp giá trị khác nhau từng đôi
pairs = [(x, y) for x in [3, 4, 5] for y in [6, 3, 5] if x != y]
print(pairs)


# Kết quả: [(3, 6), (3, 5), (4, 6), (4, 3), (4, 5), (5, 6), (5, 3)]


def is_prime(n):
    """This function check whether or not n is prime number"""
    if n < 2:
        return False
    bound = int(math.sqrt(n))
    for x in range(2, bound + 1):
        if n % x == 0:
            return False
    return True


# Tạo list các số nguyên tố trong danh sách cho trước
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 0, 11, 12, 13, 14, 15]
primes = [x for x in numbers if is_prime(x)]
print(f'Prime numbers in list: {primes}')
# Kết quả: Prime numbers in list: [2, 3, 5, 7, 7, 11, 13]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in range(len(matrix)):
    for col in range(len(matrix[row])):
        print(f'{matrix[row][col]} ', end='')
    print()
# Kết quả:
# 1 2 3
# 4 5 6
# 7 8 9

# Hoặc sử dụng cú pháp rút gọn:
for row in matrix:
    for e in row:
        print(f'{e} ', end='')
    print()
# Kết quả:
# 1 2 3
# 4 5 6
# 7 8 9

friends = ['Hanh', 'Nam', 'Phong', 'Khanh', 'Trang', 'Nhung']
del friends[0]  # Xóa phần tử đầu
print(friends)
del friends[0: 3]  # Xóa các phần tử có index trong [0, 3)
print(friends)
del friends  # Xóa cả danh sách
print(friends)
# Kết quả:
# ['Nam', 'Phong', 'Khanh', 'Trang', 'Nhung']
# ['Trang', 'Nhung']
# NameError: name 'friends' is not defined
