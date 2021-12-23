from net.braniumacademy.ex_chapter5.lesson52.exercises1.utils \
    import create_fraction, display_fractions, \
    add_list_fractions, multiply_list_fractions

option = "=============== OPTIONS ===============\n" \
         "1. Nhập vào một phân số mới dạng a/b.\n" \
         "2. Hiển thị danh sách phân số hiện có.\n" \
         "3. Rút gọn phân số.\n4. Tính tổng hai phân số.\n" \
         "5. Tính tổng các phân số có trong danh sách.\n" \
         "6. Tính hiệu hai phân số.\n7. Tính tích hai phân số.\n" \
         "8. Tính thương hai phân số.\n" \
         "9. Tính tích các phân số trong danh sách.\n" \
         "0. Thoát chương trình.\nBạn chọn? "
m_fractions = []
while True:
    choice = int(input(option))
    match choice:
        case 0:
            print("==> Chương trình kết thúc <==")
            break
        case 1:
            f = create_fraction()
            if f is not None:
                m_fractions.append(f)
        case 2:
            print("== Các phân số có trong danh sách ==")
            display_fractions(m_fractions)
        case 3:
            f = create_fraction()
            if f is not None:
                f.simplify()
                print(f"Phân số sau khi rút gọn: {f}")
        case 4:
            f1 = create_fraction()
            f2 = create_fraction()
            if f1 is not None and f2 is not None:
                fsum = f1.add(f2)
                fsum.simplify()
                print(f"{f1} + {f2} = {fsum}")
        case 5:
            fsum = add_list_fractions(m_fractions)
            print(f"Tổng các phân số trong danh sách: {fsum}")
        case 6:
            f1 = create_fraction()
            f2 = create_fraction()
            if f1 is not None and f2 is not None:
                fdif = f1.sub(f2)
                fdif.simplify()
                print(f"{f1} - {f2} = {fdif}")
        case 7:
            f1 = create_fraction()
            f2 = create_fraction()
            if f1 is not None and f2 is not None:
                fprod = f1.mul(f2)
                fprod.simplify()
                print(f"{f1} - {f2} = {fprod}")
        case 8:
            f1 = create_fraction()
            f2 = create_fraction()
            if f1 is not None and f2 is not None:
                fquot = f1.div(f2)
                fquot.simplify()
                print(f"{f1} - {f2} = {fquot}")
        case 9:
            fprod = multiply_list_fractions(m_fractions)
            print(f"Tích các phân số trong danh sách: {fprod}")
        case _:
            print("Sai tùy chọn, vui lòng kiểm tra lại")
