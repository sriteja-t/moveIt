import os
import shutil
import platform
from sys import platform
 
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
if os.path.isdir(destination_path):
     print('Directory exists.')
else:
    os.mkdir(destination_path)
    print('Directory created.')
file_type = int(input('''Select file type from the given options:
                         0  Skip
                         1  Images 
                         2  Apps 
                         3  Documents (all formats)
                         4  PDF
                         5  Custom  
                         '''))
if file_type == 1:
    a = ('.jpg', '.png', '.jpeg', '.hief')
elif file_type == 2:
    a = ('.exe', '.msi')
elif file_type == 3:
    a = ('.pdf', '.doc', 'docx', '.pptx', '.xlsx', '.csv', '.ppt')
elif file_type == 4:
    a = ('.pdf')
elif file_type == 5:
    a = tuple(input("Enter File Type/Types seperated by space: ").split())
#add custom options also.
print(a)
limit = float(input("Enter the minimum file size in MB : "))
f_size = limit * 1000000
 
files = os.listdir(source_path)
index = 0
for item in files: 
    if platform != "win32":
        src = source_path + "/" + item
        dst = destination_path + "/" + item
    else:
        src = source_path + "\\" + item
        dst = destination_path + "\\" + item
    if os.path.isfile(src):
        size = (os.path.getsize(src))
        if size > f_size:
            if file_type == 0:  
                index = index + 1
                shutil.move(src, dst)
                print(index, size, item)
            elif item.endswith(a):  
                index = index + 1 
                shutil.move(src, dst)
                print(index, size, item)