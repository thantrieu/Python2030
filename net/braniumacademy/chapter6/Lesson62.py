import os
import shutil

path1 = 'net/branium/newfile.txt'
path2 = 'net/branium/newfile.pdf'
print(os.path.exists(path1))
print(os.path.exists(path2))

for x in os.listdir('.'):
    if os.path.isfile(x):
        print(x)

# path = 'net'
# shutil.rmtree(path)

# path = 'myfile4.txt'
# os.remove(path)

src = 'Lesson61.py'
dst = 'net/branium/output2.txt'
shutil.copy2(src, dst)

old_name = 'newfile.txt'
new_name = 'net/branium/newfile.txt'
os.renames(old_name, new_name)


file_name = 'myfile.txt'
mode = 'x'
open(file_name, mode)
