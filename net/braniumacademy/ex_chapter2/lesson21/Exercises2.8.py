# Kiểm tra ba số a b c có tạo thành ba cạnh tam giác không
a_str, b_str, c_str = input().split()
a = float(a_str)
b = float(b_str)
c = float(c_str)
if a + b > c and b + c > a and c + a > b:
    print("YES")
else:
    print("NO")
