# Kiểm tra ba số a b c có tạo thành tam giác vuông hay không
a_str, b_str, c_str = input().split()
a = float(a_str)
b = float(b_str)
c = float(c_str)
if (a ** 2 + b ** 2) == c ** 2 or (a ** 2 + c ** 2) == b ** 2 \
        or a ** 2 == (b ** 2 + c ** 2):
    print("YES")
else:
    print("NO")
