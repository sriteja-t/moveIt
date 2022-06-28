import os
import shutil

print('''


███╗░░░███╗░█████╗░██╗░░░██╗███████╗██╗████████╗
████╗░████║██╔══██╗██║░░░██║██╔════╝██║╚══██╔══╝
██╔████╔██║██║░░██║╚██╗░██╔╝█████╗░░██║░░░██║░░░
██║╚██╔╝██║██║░░██║░╚████╔╝░██╔══╝░░██║░░░██║░░░
██║░╚═╝░██║╚█████╔╝░░╚██╔╝░░███████╗██║░░░██║░░░
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░░╚═╝░░░


''')

source_path = input(str("Enter the path of the directory to scan : "))
destination_path = input(str("Enter the path of the directory to move the files : "))
file_type = input("Enter the file extension you want to scan in the directory or 0 to scan all files : ")
limit = float(input("Enter the minimum file size in MB : "))
f_size = limit * 1000000

files = os.listdir(source_path)
index = 0
for item in files: 
    src = source_path + "\\" + item
    dst = destination_path + "\\" + item
    if os.path.isfile(src):
        size = (os.path.getsize(src))
        if size > f_size:
            if file_type == "0":  
                index = index + 1
                shutil.move(src, dst)
                print(index, size, item)
            elif item.endswith(file_type):  
                index = index + 1 
                shutil.move(src, dst)
                print(index, size, item)
