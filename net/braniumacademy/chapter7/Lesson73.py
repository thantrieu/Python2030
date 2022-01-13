# try:
#     age = int(input('Nhập tuổi của bạn(0-150): '))
#     if age < 0 or age > 150:
#         raise ValueError('Tuổi bạn nhập không hợp lệ!')
#     else:
#         print(f'Tuổi của bạn là {age}')
# except ValueError as e:
#     print(e)


# def contains_invalid_character(name):
#     for c in name:
#         if not c.isalpha() and not c == ' ':
#             return True
#     return False
#
#
# try:
#     full_name = input('Họ và tên người gửi: ')
#     if len(full_name) < 2 or len(full_name) > 30 or \
#             contains_invalid_character(full_name):
#         raise ValueError('Họ và tên không hợp lệ.')
#     else:
#         print(f'Xin chào {full_name}!')
# except ValueError as e:
#     raise RuntimeError('Không xác định được người gửi hàng.') from e

try:
    gpa_str = input('Nhập điểm TB học kỳ: ')
    gpa = float(gpa_str)
except ValueError as e:
    raise RuntimeError('Không phân loại được sinh viên này.') from e
