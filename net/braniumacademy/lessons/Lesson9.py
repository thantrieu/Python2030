# Đọc vào string str
# Đọc vào số nguyên int
# Đọc vào số thực float

full_name = input("Nhập họ và tên của bạn rồi nhấn phím Enter: ")
print(f"Xin chào '{full_name}'!")
address = input("Bạn ở đâu vậy? ")
print(f"Bạn {full_name} đến từ {address} này các bạn ơi!")
inputText = input("Bạn bao nhiêu tuổi? ")
age = int(inputText)
print(f"Ồ bạn {full_name} {age} tuổi và đến từ {address}.")
inputText = input("Điểm Trung bình môn kì trước của bạn là bao nhiêu? ")
gpa = float(inputText)
print(f"Wao! Điểm của bạn {full_name} là {gpa} đó.")
