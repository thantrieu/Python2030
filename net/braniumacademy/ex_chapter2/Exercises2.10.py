# Đổi điểm số sang điểm chữ
mark = float(input())
level = "INVALID"
if 0.0 <= mark <= 10.0:
    if mark >= 9.0:
        level = "A"
    elif mark >= 7.0:
        level = "B"
    elif mark >= 5.0:
        level = "C"
    elif mark >= 4.0:
        level = "C"
    else:
        level = "F"
print(level)
