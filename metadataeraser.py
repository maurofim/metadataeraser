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
    new_path = path_dir.replace(final_dir,'')
    return (new_path, final_dir)

#create cleaned directories
def cleaned_dirs(dir):
    os.mkdir(get_parent_dir(path)[0] + get_parent_dir(path)[1] + '.cleaned')
    os.mkdir(get_parent_dir(path)[0] + get_parent_dir(path)[1] + '.cleaned_info')
    for subdir, dirs in os.walk(dir):
        for dir in dirs, subdir:
            dir_path = os.path.abspath(dir)
            dir_path_end = origin_file_path.replace(get_parent_dir(path)[0],'')
            r_directories = '\/[\w ]*'
            dir_list = re.findall(r_directories, dir_path_end)
            for name in dir_list
                name = name + '.cleaned'
                cleaned_path += name
            os.mkdir(get_parent_dir(path)[0] + cleaned_path + dir + '.cleaned')

#find cleaned dir for file.cleaned
def path_cleaned_dir(origin_file):
    origin_file_path = os.path.abspath(origin_file)
    not_cleaned_path = origin_file_path.replace(get_parent_dir(path)[0],'')
    r_directories = '\/[\w ]*'
    dir_list = re.findall(r_directories, not_cleaned_path)
    for name in dir_list
        name = name + '.cleaned'
        cleaned_path += name
    return (get_parent_dir(path)[0] + cleaned_path)

def main():
#specify directory location
    path = str(input('enter path directory: '))
#changing working directory
    os.chdir(path)
    cleaned_dirs(path)
    for subdir, dirs, files in os.walk(path):
        for file in files:
#erase metadata
            cleaning_command = subprocess.Popen(['mat2', file], stdout = subprocess.PIPE)
            output = cleaning_command.communicate()[0]
#check if the file is supported by mat2
            if output == b'':
                os.system('echo CLEANED >> clean.txt')
#create clean.txt add metadata
#adding "" for files with white spaces, this way linux terminal can read them
                os.system('exiftool ' + '"' + file + '"' + ' >> clean.txt')
                os.system('echo -------------------------------------------- >> clean.txt')
#move cleaned file to respective cleaned directory
                os.system('mv ' + '"' + file + '.cleaned' + '"' + ' ' + path_cleaned_dir(file))
            else:
#create not_clean.txt, then add metadata
                os.system('echo ' + str(output) + ' >> not_clean.txt')
                os.system('exiftool ' + '"' + file + '"' + ' >> not_clean.txt')
                os.system('echo -------------------------------------------- >> not_clean.txt')
#move copy of file to respective cleaned directory
                os.system('cp ' + '"' + file + '.cleaned' + '"' + ' ' + path_cleaned_dir(file))
#Move .txt >> /clean_info
    os.system('mv clean.txt' + ' ' + get_parent_dir(path)[0] + '/' + get_parent_dir(path)[1] + '.cleaned_info')
    os.system('mv not_clean.txt' + ' ' + get_parent_dir(path)[0] + '/' + get_parent_dir(path)[1] + '.cleaned_info')

main()
