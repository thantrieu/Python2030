def tower_of_hanoi(n, from_rod, to_rod, tmp_rod):
    """Hàm giải bài toán tháp Hà Nội. Các bước thực hiện:
     * B1: Nếu n == 1, chuyển n từ cọc A sang cọc C. Kết thúc.
     * B2: gọi đệ quy, chuyển n-1 đĩa từ cọc A sang cọc B.
     * B3: chuyển đĩa dưới cùng sang cọc C.
     * B4: chuyển n-1 đĩa từ cọc B sang cọc C.
     * Sau khi chuyển, đọc ngược giá trị tại cột C từ dưới lên
     * với điều kiện giá trị đọc trước nhỏ hơn giá trị đọc sau
     * sẽ được kết quả xét từ trên xuống(1-n).
    """
    if n == 1:
        print(f"Chuyển {n} từ cọc {from_rod} đến cọc {to_rod}")
        return
    tower_of_hanoi(n - 1, from_rod, tmp_rod, to_rod)
    print(f"Chuyển {n} từ cọc {from_rod} đến cọc {to_rod}")
    tower_of_hanoi(n - 1, tmp_rod, to_rod, from_rod)


m = int(input("Nhập n: "))
tower_of_hanoi(m, 'A', 'C', 'B')
