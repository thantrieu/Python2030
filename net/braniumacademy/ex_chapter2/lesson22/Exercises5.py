day_str, month_str = input().split()
day = int(day_str)
month = int(month_str)

match month:
    case 1:
        if 1 <= day <= 19:
            print("Ma Kết")
        elif 20 <= day <= 31:
            print("Bảo Bình")
        else:
            print("INVALID DAY")
    case 2:
        if 1 <= day <= 18:
            print("Bảo Bình")
        elif 19 <= day <= 29:
            print("Song Ngư")
        else:
            print("INVALID DAY")
    case 3:
        if 1 <= day <= 20:
            print("Song Ngư")
        elif 21 <= day <= 31:
            print("Bạch Dương")
        else:
            print("INVALID DAY")
    case 4:
        if 1 <= day <= 20:
            print("Bạch Dương")
        elif 21 <= day <= 30:
            print("Kim Ngưu")
        else:
            print("INVALID DAY")
    case 5:
        if 1 <= day <= 20:
            print("Kim Ngưu")
        elif 21 <= day <= 31:
            print("Song Tử")
        else:
            print("INVALID DAY")
    case 6:
        if 1 <= day <= 21:
            print("Song Tử")
        elif 22 <= day <= 30:
            print("Cự Giải")
        else:
            print("INVALID DAY")
    case 7:
        if 1 <= day <= 22:
            print("Cự Giải")
        elif 23 <= day <= 31:
            print("Sư Tử")
        else:
            print("INVALID DAY")
    case 8:
        if 1 <= day <= 22:
            print("Sư Tử")
        elif 23 <= day <= 31:
            print("Xử Nữ")
        else:
            print("INVALID DAY")
    case 9:
        if 1 <= day <= 22:
            print("Xử Nữ")
        elif 23 <= day <= 30:
            print("Thiên Bình")
        else:
            print("INVALID DAY")
    case 10:
        if 1 <= day <= 23:
            print("Thiên Bình")
        elif 24 <= day <= 31:
            print("Bọ Cạp")
        else:
            print("INVALID DAY")
    case 11:
        if 1 <= day <= 22:
            print("Bọ Cạp")
        elif 23 <= day <= 30:
            print("Nhân Mã")
        else:
            print("INVALID DAY")
    case 12:
        if 1 <= day <= 21:
            print("Nhân Mã")
        elif 22 <= day <= 31:
            print("Ma Kết")
        else:
            print("INVALID DAY")
    case _:
        print("INVALID_MONTH")
