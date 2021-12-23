a_str, b_str = input("Nhập hai số nguyên a, b: \n").split()
a = int(a_str)
b = int(b_str)
option = "============ MENU ============\n" \
         "1. Cộng hai số.\n2. Trừ a cho b.\n3. Nhân a với b.\n" \
         "4. Chia a cho b.\n5. Chia lấy dư a cho b.\n6. Tính a^b, b >= 0.\n" \
         "0. Thoát.\nXin mời chọn: "
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("Cảm ơn quý vị đã sử dụng dịch vụ!")
            break
        case 1:
            print(f"{a} + {b} = {a + b}")
        case 2:
            print(f"{a} - {b} = {a - b}")
        case 3:
            print(f"{a} * {b} = {a * b}")
        case 4:
            if b == 0:
                print("ERROR")
            else:
                print(f"{a} / {b} = {a / b}")
        case 5:
            if b == 0:
                print("ERROR")
            else:
                print(f"{a} % {b} = {a % b}")
        case 6:
            print(f"{a} ^ {b} = {a ** b}")
        case _:
            print("Sai chức năng. Mời nhập lại!")
