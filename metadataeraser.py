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

#create clean.txt and add all the metadata into it
#then erase metadata
for file in os.listdir(path):
    os.system('exiftool ' + '"' + file + '"' + ' >> clean.txt')
    cleaning_command = subprocess.Popen(['mat2', '"', file, '"'], stdout = subprocess.PIPE)
    output = str(cleaning_command.communicate())
    if output == '':
        os.system('CLEANED >> clean.txt')
    else:
        os.system(output + ' >> clean.txt')
    os.system('echo -------------------------------------------- >> clean.txt')

#create directory clean and move cleaned files into it
os.mkdir(path + '/clean')
os.system('mv clean.txt ' + path + '/clean')
end = '^.*cleaned.*$'
for file in os.listdir(path):
    if re.match(end, file):
        os.system('mv ' + '"' + file + '"' + ' ' + path + '/clean')
