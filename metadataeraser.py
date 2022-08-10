#!/usr/bin/env python3
#mat2 needed

import re
import subprocess
import os

#specify directory location
path_directory = str(input('enter path directory: '))

#create clean.txt and add all the metadata into it
#then erase metadata
for file in os.listdir(path_directory):
    os.system('exiftool ' + str(file) + ' >>' + path_directory +' clean.txt')
    os.system('echo -------------------------------------------- >> clean.txt')
    os.system('mat2 ' + str(file))

#create directory clean and move clened files into it
os.mkdir(path_directory + '/clean')
os.system('mv clean.txt' + path_directory + '/clean')
end = re.search('cleaned\.\w\w\w$')
for files in os.listdir(path_directory):
    if files.endswith(end):
        os.system('mv ' + str(files) + ' clean')
