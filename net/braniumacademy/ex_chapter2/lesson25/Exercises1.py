import math

t = int(input())
for i in range(1, t + 1):
    n = int(input())
    if n < 2:  # mọi số nguyên < 2 không là số nguyên tố
        print("NO")
    else:
        is_prime = True  # giả sử ban đầu n là số nguyên tố
        bound = int(math.sqrt(n))
        # kiểm tra xem n có phải nguyên tố không
        for x in range(2, bound + 1):
            if n % x == 0:  # nếu n chia hết cho x-> n không nguyên tố
                is_prime = False  # gán lại giá trị cho biến đánh dấu
                break  # kết thúc việc kiểm tra
        if is_prime:
            print("YES")
        else:
            print("NO")
