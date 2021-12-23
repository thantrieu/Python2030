# Liệt kê n số nguyên tố đầu tiên, n > 0 nhập vào từ bàn phím.
# Số nguyên tố là số nguyên dương chỉ chia hết cho 1 và chính nó.
# Số 2, 3, 5, 7... là một số ví dụ
import math

n = int(input("Enter an integer number n > 0: "))
i = 2
count = 0
print(f"First {n} prime numbers: ")
while count < n:
    is_prime = True
    j = 2
    bound = int(math.sqrt(i))
    while j <= bound:
        if i % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        print(f"{i} ", end="")
        count += 1
    i += 1

numbers = [1, 2, 4, 8, 7, 6, 9, 8, 0]  # Ctrl Alt L == format code
print("Odd numbers from list: ")
for x in numbers:
    if x % 2 == 0:
        continue
    print(f"{x} ", end="")
