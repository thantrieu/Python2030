# Tìm giá trị lớn nhất trong 3 số
a_str, b_str, c_str = input().split()
a = int(a_str)
b = int(b_str)
c = int(c_str)

if a == b and b == c:
    print("NO RESULT")
else:
    max_value = a
    if b > max_value:
        max_value = b
    if c > max_value:
        max_value = c
    print(max_value)
