t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if n < 0:
        n *= -1
    m = n
    reverse = 0
    while m > 0:
        reverse = reverse * 10 + m % 10
        m //= 10
    if reverse == n:  # giá trị sau khi đảo ngược bằng giá trị n
        print(f"Test {i}: YES")
    else:
        print(f"Test {i}: NO")
