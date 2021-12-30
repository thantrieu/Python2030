path = 'input.txt'

# Hiển thị 4 dòng đầu trong file input21.txt
with open(path, 'r', encoding='UTF-8') as reader:
    lines = reader.readlines()
    print(lines[:4])  # In ra 4 phần tử đầu tiên trong list

# Đọc cả file với readlines()
with open(path, 'r', encoding='UTF-8') as reader:
    lines = reader.readlines()
    for line in lines:
        print(line.strip())

# Đọc 4 dòng đầu trong file input21.txt
with open(path, 'r', encoding='UTF-8') as reader:
    for i in range(4):
        print(reader.readline().strip())

# Đọc cả file với readline()
with open(path, 'r', encoding='UTF-8') as reader:
    line = reader.readline().strip()
    while line != '':
        print(line)
        line = reader.readline().strip()

# Đọc cả file không dùng readline()
with open(path, 'r', encoding='UTF-8') as reader:
    for line in reader:
        print(line.strip())

# Đọc dòng đầu và dòng cuối trong file
with open(path, 'r', encoding='UTF-8') as reader:
    print(reader.readline().strip())
    for last_line in reader:
        pass
    print(last_line.strip())

with open(path, 'r', encoding='UTF-8') as reader:
    print(reader.read())

try:
    reader = open(path, 'r', encoding='UTF-8')
    print(reader.read())
    reader.close()
except FileNotFoundError as e:
    print(e)
