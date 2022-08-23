mark = input("Nhập vào một giá trị a-f: ")
match mark:
    case 'a' | 'A':
        print("Giỏi")
    case 'b' | 'B':
        print("Khá")
    case 'c' | 'C':
        print("Trung bình")
    case 'd' | 'D':
        print("Yếu")
    case 'f' | 'F':
        print("Liệt")
    case _:
        print("INVALID")
