def fibonacci(n):
    """This function find and return fibonacci number fn"""
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


t = int(input())
for i in range(1, t + 1):
    m = int(input())
    print(f"Test {i}: ", end="")
    if m < 0:
        print("ERROR")
    else:
        print(fibonacci(m))
