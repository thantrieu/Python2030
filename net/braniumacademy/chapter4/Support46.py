# from prime import is_prime, F0, F1  # Import hàm, f0, f1

from prime import is_prime as check_prime_number

print(f'{2} is prime number? {check_prime_number(2)}')
print(f'{3} is prime number? {check_prime_number(3)}')
print(f'{6} is prime number? {check_prime_number(6)}')
# Kết quả:
# 2 is prime number? True
# 3 is prime number? True
# 6 is prime number? False

# Sau khi import tên hàm cụ thể,
# ta sử dụng trực tiếp tên hàm không cần qua tên modul
# print(f'F0 = {F0}')
# print(f'F1 = {F1}')
# Kết quả:
# 2 is prime number? True
# 3 is prime number? True
# 6 is prime number? False
# F0 = 0
# F1 = 1

import prime

print(dir(prime))
# Kết quả:
# ['F0', 'F1', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__',
# '__package__', '__spec__', 'is_prime', 'math']
