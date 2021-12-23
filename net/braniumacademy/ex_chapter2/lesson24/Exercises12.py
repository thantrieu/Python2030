option = "Nhập tháng 1-12.\nNhập 0 để thoát:\n"
while True:
    month = int(input(option))
    match month:
        case 0:
            print("Cảm ơn quý vị đã sử dụng dịch vụ!")
            break
        case 1:
            result = "January"
        case 2:
            result = "February"
        case 3:
            result = "March"
        case 4:
            result = "April"
        case 5:
            result = "May"
        case 6:
            result = "Jun"
        case 7:
            result = "July"
        case 8:
            result = "August"
        case 9:
            result = "September"
        case 10:
            result = "October"
        case 11:
            result = "November"
        case 12:
            result = "December"
        case _:
            result = "Giá trị không hợp lệ, vui lòng chọn lại!"
    print(result)
    print("===================================")
