import shutil

path = 'destination'
shutil.rmtree(path, ignore_errors=True)







# src = 'new folder'
# dst = 'destination/src'
# shutil.copytree(src, dst)



#
# old_dir = 'net'
# new_dir = 'new folder1/child folder/lesson 6.1x'
# os.renames(old_dir, new_dir)

# path = 'net/branium/learn python/lesson 6.1'
# os.makedirs(path)

#
# dir_name = 'Learn Python'
# try:
#     os.mkdir(dir_name)
# except FileExistsError as e:
#     print(e)
