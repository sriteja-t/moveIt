import os
from pathlib import Path
import shutil
source_path = str(Path.home() / "Downloads")
destination_path = str(Path.home()/ "Documents")

files = os.listdir(source_path)

for item in files: 
    src = source_path + "\\" + item
    dst = destination_path + "\\" + item
    if os.path.isfile(src):
        size = (os.path.getsize(src)) 
        if size > 524288000:   #500MB    
            shutil.move(src, dst)
            print(size, item)