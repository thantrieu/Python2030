def factorial(n):
    """Hàm tính n! đệ quy"""
    if n == 1 or n == 0:
        return 1
    return n * factorial(n - 1)


def factorial_loop(n):
    """Hàm tính n! sử dụng vòng lặp"""
    result = 1
    for x in range(1, n + 1, 1):
        result *= x
    return result


value = 50
print(f"Recursion {value}! = {factorial(value)}")
print(f"Loop {value}! = {factorial_loop(value)}")
