# Tìm tập từ xuất hiện trong cả hai chuỗi s1, s2
s1 = {x for x in input('Nhập tập từ thứ 1: ').split()}
s2 = {x for x in input('Nhập tập từ thứ 2: ').split()}
result = s1.intersection(s2)
print(f'Tập từ chung: {result}')
