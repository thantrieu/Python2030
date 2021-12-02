# Tính tổng từ k đến n
# k = int(input("Enter integer number k: "))
# n = int(input("Enter integer number n > k: "))
# sum = 0
# for x in range(k, n + 1, 1):
#     sum += x
# print(f"Sum from {k} to {n}: {sum}")

# # Hiển thị các kí tự trong một chuỗi input
# full_name = input("Enter your full name: ")
# print("Spell your name: ")
# for x in full_name:
#     if x.isalpha():
#         print(f"'{x}'")
# else:
#     print("All done!")
#
# Vẽ hình chữ nhật rỗng bằng dấu *
width = int(input("Enter rectangle's width: "))
height = int(input("Enter rectangle's width: "))
for i in range(1, width + 1, 1):
    for j in range(1, height + 1, 1):
        if i == 1 or i == width or j == 1 or j == height:
            print(" * ", end="")
        else:
            print("   ", end="")
    print()
