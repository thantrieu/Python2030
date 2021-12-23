a_str, b_str = input().split()
a = int(a_str)
b = int(b_str)
if a < 0 or b < 0:
    print("INVALID")
else:
    product = a * b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    print(f"{a} {product // a}")
