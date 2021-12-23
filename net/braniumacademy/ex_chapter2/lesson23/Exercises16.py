m_str, n_str = input().split()
m = int(m_str)
n = int(n_str)
# draw rect from number:
for i in range(1, m + 1):
    for j in range(1, n + 1):
        print(f"{j} ", end="")
    print()
