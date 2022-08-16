#!/usr/bin/env python3
#exiftool needed
#mat2 needed

import re
import os
import shutil
import subprocess

#create path to the parent directory
def get_parent_dir(file_path):
    r_path = '\/[\w]*$'
    current_file = re.search(r_path, file_path).group()
    parent_dir_path = current_file.replace(current_file,'')
    return (parent_dir_path, current_file)

#create cleaned directories
def cleaned_dirs(path, dirs, root):
    os.mkdir(path + '.cleaned')
    os.mkdir(path + '.cleaned_info')
    for dir in dirs:
        dir_path_end = root.replace(get_parent_dir(path)[0],'')
        r_directories = '\/[\w ]*'
        dir_list = re.findall(r_directories, dir_path_end)
        cleaned_path = ''
        for name in dir_list:
            name = name + '.cleaned'
            cleaned_path += name
        os.mkdir(get_parent_dir(path)[0] + cleaned_path)

#find cleaned dir for file.cleaned
def path_cleaned_dir(origin_file):
    origin_file_path = os.path.abspath(origin_file)
    parent_dir= get_parent_dir(get_parent_dir(origin_file_path)[0])[1]
    cleaned_path = os.path.abspath(parent_dir+'.cleaned')
    return cleaned_path

def cleaned_files(root, files, path):
    txt_path = os.path.abspath(get_parent_dir(path)[1] + 'cleaned_info')
    for file in files:
    #erase metadata
        os.chdir(root)
        cleaning_command = subprocess.Popen(['mat2', file], stdout = subprocess.PIPE)
        output = cleaning_command.communicate()[0]
        os.chdir(txt_path)
    #check if the file is supported by mat2
        if output == b'':
            os.system('echo CLEANED >> clean.txt')
    #create clean.txt add metadata
    #adding "" for files with white spaces, this way linux terminal can read them
            os.system('exiftool ' + '"' + file + '"' + ' >> clean.txt')
            os.system('echo -------------------------------------------- >> clean.txt')
    #move cleaned file to respective cleaned directory
            shutil.move(os.path.abspath(file + '.cleaned'), path_cleaned_dir(file))
        else:
    #create not_clean.txt, then add metadata
            os.system('echo ' + str(output) + ' >> not_clean.txt')
            os.system('echo location: ' + str(path_cleaned_dir(file)) + ' >> not_clean.txt')
            os.system('exiftool ' + '"' + file + '"' + ' >> not_clean.txt')
            os.system('echo -------------------------------------------- >> not_clean.txt')
    #move copy of file to respective cleaned directory
            shutil.copy(os.path.abspath(file), path_cleaned_dir(file))

def main():
#specify directory location
    path = str(input('enter path directory: '))
#changing working directory
    for root, dirs, files in os.walk(path):
        cleaned_dirs(path, dirs, root)
        cleaned_files(path, files, root)

main()
