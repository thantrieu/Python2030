import os
import shutil

path = 'Learn Python 3.x'
try:
    shutil.rmtree(path)
except FileNotFoundError as e:
    print(e)


# src = 'new folder'
# dst = "destination/src"
# shutil.copytree(src, dst)



# old_dir = 'Learn Python'
# new_dir = 'Learn Python 3.x'
# old_dir = 'Test/level1/level2/level3'
# new_dir = 'new folder/child folder/lesson 6.1x'
# os.renames(old_dir, new_dir)



# # path = 'Learn Python'
# # path = 'D:/Test/level1/level2/level3'
# path = 'Test/level1/level2/level3'
# try:
#     os.makedirs(path)
# except FileExistsError as e:
#     print(e)
