option = "Nhập ngày 1-7.\nNhập 0 để thoát:\n"
while True:
    day = int(input(option))
    match day:
        case 0:
            print("Xin chào và hẹn gặp lại!")
            break
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Frday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:
            print("Giá trị không hợp lệ, vui lòng chọn lại!")
    print("===================================")
