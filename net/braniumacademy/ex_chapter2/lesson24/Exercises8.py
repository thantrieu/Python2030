a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)
if a <= 0 or b <= 0:
    print("INVALID")
else:
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a == 0 and b == 1 or b == 0 and a == 1:
        print("YES")
    else:
        print("NO")
