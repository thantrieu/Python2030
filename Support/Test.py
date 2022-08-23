def update():
    s = 0
    for index in range(0, n):
        s = s + a[index] * x[index]
    if s >= c:
        b.append(s)  # cập nhật kết quả


def process(index):
    # j chạy từ 0 đến 1
    for j in range(0, 2):
        x[index] = j
        if index == n - 1:
            update()
        else:
            process(index + 1)


if __name__ == '__main__':
    x = [0 for i in range(1000)]  # khởi tạo list với 1000 phần tử mang giá trị 0
    b = []  # tạo một list rỗng
    n = int(input("Nhap n = "))  # nhập vào giá trị n - số phần tử của list
    c = int(input('Nhap c = '))  # nhập vào giá trị c
    a = [float(number) for number in input().split()]  # nhập các phần tử của list a[]
    process(0)  # đệ quy tìm kết quả
    b.sort()  # sắp xếp kết quả
    result = list(dict.fromkeys(b))  # lọc lấy các phần tử duy nhất
    for element in result:  # liệt kê ra màn hình
        print(f'{element} ')
