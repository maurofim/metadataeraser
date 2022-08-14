#!/usr/bin/env python3
#exiftool needed
#mat2 needed

import re
import os
import subprocess
#specify directory location
path = str(input('enter path directory: '))

#changing working directory
os.chdir(path)

#create clean.txt and not_clean.txt, then add all the metadata into it
#then erase metadata
for file in os.listdir(path):
    cleaning_command = subprocess.Popen(['mat2', file], stdout = subprocess.PIPE)
    output = cleaning_command.communicate()[0]
    if output == b'':
        os.system('echo CLEANED >> clean.txt')
        os.system('exiftool ' + '"' + file + '"' + ' >> clean.txt')
        os.system('echo -------------------------------------------- >> clean.txt')
    else:
        os.system('echo ' + str(output) + ' >> not_clean.txt')
        os.system('exiftool ' + '"' + file + '"' + ' >> not_clean.txt')
        os.system('echo -------------------------------------------- >> not_clean.txt')

#create path to the directory before
r_path = '\/[\w]*$'
final_dir = re.search(r_path, path)
final_dir_len = len(final_dir.group())
path_len = len(path)
new_path_len = path_len - final_dir_len
new_path = path[0:new_path_len]

#create directories and move their respective files into them, .clean. >> /clean and .txt >> /clean_info
os.mkdir(new_path + '/' + final_dir.group() + '.cleaned')
os.mkdir(new_path + '/' + final_dir.group() + '.cleaned_info')
os.system('mv clean.txt' + ' ' + new_path + '/' + final_dir.group() + '.cleaned_info')
os.system('mv not_clean.txt' + ' ' + new_path + '/' + final_dir.group() + '.cleaned_info')
r_file = '^.*\.cleaned\..*$'
for file in os.listdir(path):
    if re.match(r_file, file):
        os.system('mv ' + '"' + file + '"' + ' ' + new_path + '/' + final_dir.group() + '.cleaned')
