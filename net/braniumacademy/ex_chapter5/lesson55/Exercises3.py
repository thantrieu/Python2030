class Matrix:
    def __init__(self, row=0, col=0, data=None):
        if data is None:
            data = list()
        self.row = row
        self.col = col
        self.data = data

    def __add__(self, other):
        if self.row == other.row and self.col == other.row:
            data = []
            for i in range(self.row):
                data.append([])
                for j in range(self.col):
                    data[i].append(self.data[i][j] + other.data[i][j])
            return Matrix(self.row, self.col, data)
        else:
            print('Không cộng được do hai ma trận không cùng cấp.')
            return None

    def __sub__(self, other):
        if self.row == other.row and self.col == other.row:
            data = []
            for i in range(self.row):
                data.append([])
                for j in range(self.col):
                    data[i].append(self.data[i][j] - other.data[i][j])
            return Matrix(self.row, self.col, data)
        else:
            print('Không trừ được do hai ma trận không cùng cấp.')
            return None

    def __mul__(self, other):
        if self.col == other.row:
            data = []
            for i in range(self.row):
                data.append([])
                for x in range(other.col):  # khởi tạo giá trị phần tử ma trận kết quả
                    data[i].append(0)
                for j in range(other.col):
                    for k in range(self.col):
                        data[i][j] += (self.data[i][k] * other.data[k][j])
            return Matrix(self.row, self.col, data)
        else:
            print('Không nhân được do hai ma trận không khả tích.')
            return None

    def __eq__(self, other):
        if self.row != other.row or self.col != other.col:
            return False
        for i in range(self.row):
            for j in range(self.col):
                if self.data[i][j] != other.data[i][j]:
                    return False
        return True

    def __ne__(self, other):
        if self.__eq__(other):
            return False
        return True

    def __str__(self):
        matrix = f'[row={self.row}, col={self.col}]\n'
        for row in self.data:
            for element in row:
                matrix += f'{element:<5}'
            matrix += '\n'
        return matrix


def create_matrix(matrix):
    str1, str2 = input('Nhập vào cấp của ma trận: ').split()
    row = int(str1)
    col = int(str2)
    if row > 0 and col > 0:
        data = []
        for i in range(row):
            data.append([])
            for j in range(col):
                x = int(input(f'Nhập phần tử data[{i}][{j}]: '))
                data[i].append(x)
        matrix.row = row
        matrix.col = col
        matrix.data = data


if __name__ == '__main__':
    option = '================= TÙY CHỌN =================\n' \
             '1. Nhập vào ma trận 1.\n' \
             '2. Nhập vào ma trận 2.\n' \
             '3. Tính tổng hai ma trận.\n' \
             '4. Tính hiệu hai ma trận.\n' \
             '5. Tính tích hai ma trận.\n' \
             '6. So sánh hai ma trận bằng nhau.\n' \
             '7. So sánh hai ma trận không bằng nhau.\n' \
             '8. Thoát chương trình.\n' \
             'Xin mời chọn: '
    matrix1 = Matrix()
    matrix2 = Matrix()
    while True:
        choice = int(input(option))
        match choice:
            case 1:
                print('Nhập vào ma trận thứ nhất: ')
                create_matrix(matrix1)
                print(matrix1)
            case 2:
                print('Nhập vào ma trận thứ hai: ')
                create_matrix(matrix2)
                print(matrix2)
            case 3:
                matrix_sum = matrix1 + matrix2
                print(matrix_sum)
            case 4:
                matrix_dif = matrix1 - matrix2
                print(matrix_dif)
            case 5:
                matrix_product = matrix1 * matrix2
                print(matrix_product)
            case 6:
                print(f'Hai ma trận bằng nhau? {matrix1 == matrix2}')
            case 7:
                print(f'Hai ma trận khác nhau? {matrix1 != matrix2}')
            case 8:
                print('==> Chương trình kết thúc. <==')
            case _:
                print('==> Sai chức năng. Vui lòng chọn lại. <==')
