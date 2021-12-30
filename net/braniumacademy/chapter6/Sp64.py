input_file = 'STUDENT.DAT'
output_file = 'OUTPUT.DAT'

with open(input_file) as reader, open(output_file, 'w') as writer:
    line = reader.readline()
    while line != '':
        writer.write(line)
        line = reader.readline()

output_file = 'output.txt'
names = ['Hoa', 'Mai', 'Linh', 'Nam', 'Phong', 'Khanh']
with open(output_file, 'w') as writer:
    writer.writelines(names)
