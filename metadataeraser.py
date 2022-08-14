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

#create directories and move their respective files into them, .clean. >> /clean and .txt >> /clean_info
os.mkdir(path + '/cleaned')
os.mkdir(path + '/cleaned_info')
os.system('mv clean.txt' + ' ' + path + '/cleaned_info')
os.system('mv not_clean.txt' + ' ' + path + '/cleaned_info')
end = '^.*\.cleaned\..*$'
for file in os.listdir(path):
    if re.match(end, file):
        os.system('mv ' + '"' + file + '"' + ' ' + path + '/cleaned')
