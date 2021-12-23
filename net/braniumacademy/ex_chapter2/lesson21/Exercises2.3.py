# Kiểm tra tương quan hai số a, b
a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)
if a == b:
    print("EQUAL")
else:
    x = a - b
    if x < 0:
        x *= -1
    print(f"DIFFERENT {x}")
