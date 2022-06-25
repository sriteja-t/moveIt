import os
import shutil

print('''\n\n
███╗░░░███╗░█████╗░██╗░░░██╗███████╗██╗████████╗
████╗░████║██╔══██╗██║░░░██║██╔════╝██║╚══██╔══╝
██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░██║░░░██║░░░
██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░██║░░░██║░░░
██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗██║░░░██║░░░
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░░╚═╝░░░\n\n\n''')
source_path = input(str("Enter the path of the directory to scan : "))
# print(source_path)
destination_path = input(str("Enter the path of the directory to move the files : "))
# print(destination_path)

limit = int(input("Enter the minimum file size in MB : "))
f_size = limit*1000000
# print(limit)
# print(f_size)

files = os.listdir(source_path)

for item in files: 
    src = source_path + "\\" + item
    dst = destination_path + "\\" + item
    if os.path.isfile(src):
        size = (os.path.getsize(src)) 
        if size > f_size:  
            shutil.move(src, dst)
            print(size, item)