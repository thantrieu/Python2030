# Tìm giá trị nhỏ nhất trong 3 số
a_str, b_str, c_str = input().split()
a = int(a_str)
b = int(b_str)
c = int(c_str)

if a == b and b == c:
    print("NO RESULT")
else:
    min_value = a
    if b < min_value:
        min_value = b
    if c < min_value:
        min_value = c
    print(min_value)
