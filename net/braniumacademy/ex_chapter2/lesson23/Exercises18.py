m_str, n_str = input().split()
m = int(m_str)
n = int(n_str)
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if i == 1 or i == m or j == 1 or j == n:
            print(" * ", end="")
        else:
            print("   ", end="")
    print()
