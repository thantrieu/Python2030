# Giải phương trình bậc nhất ax + b = 0
a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)

if a == 0 and b == 0:
    print("COUNTERLESS SOLUTION")
elif a == 0 and b != 0:
    print("NO SOLUTION")
else:
    print(-b / a)
