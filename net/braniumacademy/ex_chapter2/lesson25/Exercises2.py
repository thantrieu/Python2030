import math

t = int(input())
for i in range(1, t + 1):
    a_str, b_str, k_str = input().split()
    a = int(a_str)
    b = int(b_str)
    k = int(k_str)
    if a < 0 or b < 0 or a > b or k <= 0:
        print("NOT AVAILABLE")
    else:
        count = 0  # đếm số giá trị đã in ra
        for x in range(a, b + 1):
            is_prime = True  # giả sử ban đầu n là số nguyên tố
            bound = int(math.sqrt(x))
            # kiểm tra xem n có phải nguyên tố không
            for y in range(2, bound + 1):
                if x % y == 0:  # nếu n chia hết cho x-> n không nguyên tố
                    is_prime = False  # gán lại giá trị cho biến đánh dấu
                    break  # kết thúc việc kiểm tra
            if count < k and is_prime:
                print(f"{x} ", end="")
                count += 1
            elif count >= k:
                break
        print()
