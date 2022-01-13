# print('Hello World!')  # Lỗi thừa chữ f trong lệnh print()
# while True:
#     print('OK, I am inevitable')  # Lỗi thiếu dấu : sau while


try:
    integer_number = int('Hahaha')
    print(integer_number)
except TypeError:
    print('Giá trị đối số không hợp lệ.')
print('Someting new...')
