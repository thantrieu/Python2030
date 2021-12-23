import math

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print(f"Test {i}: ", end="")
    if n <= 0:
        print("INVALID")
    else:
        count = 0
        bound = int(math.sqrt(n))
        for x in range(1, bound + 1):
            if n % x == 0:  # nếu x là ước của n
                if x != (n // x):  # lúc này x và n//x là ước của n
                    count += 2
                else:  # do x và n//x là 1 nên chỉ tính là 1 ước. ví dụ 100/10 = 10
                    count += 1  # tăng biến đếm lên 1 đơn vị
        print(count)  # in ra dòng trống
