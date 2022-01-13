def get_gpa():
    try:
        input_gpa = input('Nhập điểm TB ở hệ 4: ')
        gpa = float(input_gpa)
        if gpa < 0 or gpa > 4.0:
            raise ValueError('Điểm TB không hợp lệ.')
        else:
            return gpa
    except ValueError as e:
        print(e)
        raise RuntimeError('Không phân loại được sinh viên.') from e


def get_scholarship(g):
    return g >= 3.2


if __name__ == '__main__':
    try:
        student_gpa = get_gpa()
        result = "Có" if get_scholarship(student_gpa) else "Không"
        print(f'Sinh viên {result} đạt học bổng.')
    except RuntimeError as ex:
        print(ex)
