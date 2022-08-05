#!/usr/bin/env python3
#mat2 needed

import re
import subprocess
import os

#Specify dir location
path_of_the_directory = 'C:/'

with open("metadata.txt", mode ="w") as f:
    for files in os.listdir(path_of_the_directory):
        f.write(os.system('exiftool' + str(files))\n)
        f.write('--------------------------------------------------')
        os.system('mat2 ' + str(files))

os.mkdir('path_of_the_directory/clean')
end = re.search(cleaned\.\w\w\w)
for files in os.listdir(path_of_the_directory):
    if files.endswith(end)
        os.system('mv' + str(files) + 'clean')
