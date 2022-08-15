#!/usr/bin/env python3
#exiftool needed
#mat2 needed

import re
import os
import subprocess

#create path to the parent directory
def get_parent_dir(path_dir):
    r_path = '\/[\w]*$'
    final_dir = re.search(r_path, path_dir).group()
    final_dir_len = len(final_dir)
    path_len = len(path_dir)
    new_path_len = path_len - final_dir_len
    new_path = path[0:new_path_len]
    return (new_path, final_dir)

#create cleaned directories
def cleaned_dirs(dir):
    os.mkdir(get_parent_dir(path)[0] + get_parent_dir(path)[1] + '.cleaned')
    os.mkdir(get_parent_dir(path)[0] + get_parent_dir(path)[1] + '.cleaned_info')
    for subdir, dirs in os.walk(dir):
        for dir in dirs, subdir:
            dir_path = os.path.abspath(dir)
            os.mkdir(get_parent_dir(path)[0] + '/' + get_parent_dir(path)[1] + '.cleaned')

#find cleaned dir for file.cleaned
def path_cleaned_dir(origin_file):



#create clean.txt and not_clean.txt, then add all the metadata into it
#then erase metadata
def main():
#specify directory location
    path = str(input('enter path directory: '))
#changing working directory
    os.chdir(path)
    cleaned_dirs(path)
    for subdir, dirs, files in os.walk(path):
        for file in files:
            cleaning_command = subprocess.Popen(['mat2', file], stdout = subprocess.PIPE)
            output = cleaning_command.communicate()[0]
#check if the file is supported by mat2
            if output == b'':
                os.system('echo CLEANED >> clean.txt')
#adding "" for files with white spaces, this way linux terminal can read them
                os.system('exiftool ' + '"' + file + '"' + ' >> clean.txt')
                os.system('echo -------------------------------------------- >> clean.txt')
                os.system('mv ' + '"' + file + '.cleaned' + '"' + ' ' + path_cleaned_dir(file))
#move file to respective cleaned directory

            else:
                os.system('echo ' + str(output) + ' >> not_clean.txt')
                os.system('exiftool ' + '"' + file + '"' + ' >> not_clean.txt')
                os.system('echo -------------------------------------------- >> not_clean.txt')

#Move .txt >> /clean_info
    os.system('mv clean.txt' + ' ' + get_parent_dir(path)[0] + '/' + get_parent_dir(path)[1] + '.cleaned_info')
    os.system('mv not_clean.txt' + ' ' + get_parent_dir(path)[0] + '/' + get_parent_dir(path)[1] + '.cleaned_info')

main()
