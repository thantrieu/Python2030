import math

path = r"C:\Users\trieu\PycharmProjects\Example\input.txt"
output_path = r"C:\Users\trieu\PycharmProjects\Example\output.txt"
file = open(path)
output_file = open(output_path, "w")

t = int(file.readline())
for i in range(1, t + 1):
    n = int(file.readline())
    output_file.write(f"Test {i}: ")
    if n <= 1:
        output_file.write("NO")
    else:
        s = 1  # tổng ước nhỏ hơn n
        bound = int(math.sqrt(n))
        for x in range(2, bound + 1):
            if n % x == 0:  # nếu x là ước của n
                s += x
                if n // x != x:
                    s += n // x
        if s == n:
            output_file.write("YES")
        else:
            output_file.write("NO")
    output_file.write("\n")
output_file.close()
file.close()
