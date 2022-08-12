#!/usr/bin/env python3
#mat2 needed

import re
import os
#specify directory location
path = str(input('enter path directory: '))

#changing working directory
os.chdir(path)

#create clean.txt and add all the metadata into it
#then erase metadata
for file in os.listdir(path):
    os.system('exiftool ' + file + ' >> clean.txt')
    os.system('echo -------------------------------------------- >> clean.txt')
    os.system('mat2 ' + file)

#create directory clean and move cleaned files into it
os.mkdir(path + '/clean')
os.system('mv clean.txt ' + path + '/clean')
end = '\.cleaned\..*$'
for file in os.listdir(path):
    if re.search(file, end):
        os.system('mv ' + file + ' clean')
