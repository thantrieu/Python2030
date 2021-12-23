t = int(input())
for i in range(1, t + 1):
    a_str, b_str = input().split()
    a = int(a_str)
    b = int(b_str)
    print(f"Test {i}: {min(a, b)} {max(a, b)}")
