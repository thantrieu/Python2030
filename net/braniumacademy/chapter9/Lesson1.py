import re

gpa_string = input('Nhập điểm TB ở hệ 4 dạng #.## ví dụ 3.25: ').strip()
pattern = r'^(([0-3].[0-9]{2})|4.00)$'
matcher = re.match(pattern, gpa_string)
if matcher:
    print(f'Điểm của sinh viên hợp lệ: {gpa_string}')
else:
    print(f'Điểm của sinh viên không hợp lệ: {gpa_string}')

# birth_date = input('Nhập ngày sinh dạng 20/03/2000: ').strip()
# pattern = r'^((0[1-9])|([12][0-9])|(3[01]))/((0[1-9])|(1[0-2]))/\d{4}$'
# matcher = re.match(pattern, birth_date)
# if matcher:
#     print('Ngày sinh hợp lệ!')
# else:
#     print('Ngày sinh không hợp lệ!')

# string = input('Nhập vào chuỗi kí tự bất kỳ: ')
# pattern = r'[\s\t,.?]+'
# words = re.split(pattern, string)
#
# for word in words:
#     print(word)
