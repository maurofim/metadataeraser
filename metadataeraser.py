#!/usr/bin/env python3
#exiftool needed
#mat2 needed

import re
import os
import shutil
import subprocess

#create path to the parent directory
def get_parent_dir(file_path):
    r_path = '\/[\w ]*$'
    current_file = re.search(r_path, file_path).group()
    parent_dir_path = file_path.replace(current_file,'')
    return (parent_dir_path, current_file)

#create cleaned directories
def cleaned_dirs(path, dirs, root, subdirs):
    r_path = '\/[\w ]*'
    for dir in dirs, subdirs:
        dir_path_end = root.replace(get_parent_dir(path)[0],'')
        dir_list = re.findall(r_path, dir_path_end)
        cleaned_path = ''
        for name in dir_list:
            name = name + '.cleaned'
            cleaned_path += name
        if os.path.exists(get_parent_dir(path)[0] + cleaned_path):
            pass
        else:
            os.mkdir(get_parent_dir(path)[0] + cleaned_path)

#find cleaned dir for file.cleaned
def path_cleaned_dir(origin_file, root, path):
    r_path = '\/[\w ]*'
    parent_path = get_parent_dir(path)[0]
    final_path = root.replace(parent_path, '')
    dir_list = re.findall(r_path, final_path)
    cleaned_path = ''
    for name in dir_list:
        name = name + '.cleaned'
        cleaned_path +=  name
    final_cleaned_path = parent_path + cleaned_path + '/' + origin_file
    return final_cleaned_path

#creating cleaned files and txt files
#moving cleaned files and txt files to their respective dir
def cleaned_files(root, files, path, dirs):
    txt_path = get_parent_dir(path)[0]
    for file in files:
        os.chdir(root)
        #erase metadata
        cleaning_command = subprocess.Popen(['mat2', file], stdout = subprocess.PIPE)
        output = cleaning_command.communicate()[0]
        os.system('exiftool ' + '"' + file + '"' + ' >> cleaned_file.txt')
        shutil.move('cleaned_file.txt', txt_path)
        os.chdir(txt_path)
        #check if the file is supported by mat2
        if output == b'':
            #create cleaned.txt add metadata
            os.system('echo CLEANED >> cleaned.txt')
            #adding "" for files with white spaces, this way linux terminal can read them
            os.system('cleaned_file.txt >> cleaned.txt')
            os.system('rm cleaned_file.txt')
            os.system('echo -------------------------------------------- >> cleaned.txt')
            #move cleaned file to respective cleaned directory
            shutil.move((root + '/' +file + '.cleaned'), path_cleaned_dir(file, root, path))
        else:
            #create not_cleaned.txt add metadata
            os.system('echo ' + str(output) + ' >> not_cleaned.txt')
            os.system('echo location: ' + str(path_cleaned_dir(file, root, path)) + ' >> not_cleaned.txt')
            os.system('cleaned_file.txt >> not_cleaned.txt')
            os.system('rm cleaned_file.txt')
            os.system('echo -------------------------------------------- >> not_cleaned.txt')
            #move copy of file to respective cleaned directory
            shutil.copy((root + '/' + file), path_cleaned_dir(file, root, path))

def main():
    #specify directory location
    path = str(input('enter path directory: '))
    for root, dirs, subdirs in os.walk(path):
        cleaned_dirs(path, dirs, root, subdirs)
    for root, dirs, files in os.walk(path):
        cleaned_files(path, files, root, dirs)

main()
