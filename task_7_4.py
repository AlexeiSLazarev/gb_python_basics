
import os
from os import walk

dir_name = os.getcwd()
list_of_files = []
for r, d, f in os.walk(dir_name):
    for file in f:
        list_of_files.append(os.path.join(r, file))

import glob

files_with_size = [ (file_path, os.stat(file_path).st_size) 
                    for file_path in list_of_files ]

fs = {10:0, 100:0, 1000:0, 10000:0}
for f, s in files_with_size:
    if s <= 10: fs[10] += 1
    elif 10 < s <= 100: fs[100] += 1
    elif 100 < s <= 1000: fs[1000] += 1
    elif 1000 < s <= 10000: fs[1000] += 1

print(fs)
