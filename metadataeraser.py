#!/usr/bin/env python3
#exiftool needed
#mat2 needed
"""Cleans all metadata in a specified directory using mat2 and retrieves metadata with exiftool"""

import re
import os
import shutil
import subprocess

#specify directory location
PATH = str(input('enter path directory: '))
#create path to the parent directory
class Data():
    """Storing most used data to a class variable"""
    path = PATH
    current_dir = re.search('[/][A-za-z0-9 -_]*$', path).group()
    parent_dir = path.replace(current_dir,'')

def cleaned_dirs(root):
    """create cleaned directories"""
    r_path = '[/][A-za-z0-9 -_]*'
    dir_path_end = root.replace(Data.parent_dir, '')
    dir_list = re.findall(r_path, dir_path_end)
    cleaned_path = ''
    for name in dir_list:
        name = name + '.cleaned'
        cleaned_path += name
    if os.path.exists(Data.parent_dir + cleaned_path):
        pass
    else:
        os.mkdir(Data.parent_dir + cleaned_path)

def path_cleaned_dir(origin_file, root):
    """find cleaned dir for file.cleaned"""
    r_path = '[/][A-za-z0-9 -_]*'
    final_path = root.replace(Data.parent_dir, '')
    dir_list = re.findall(r_path, final_path)
    cleaned_path = ''
    for name in dir_list:
        name = name + '.cleaned'
        cleaned_path +=  name
    final_cleaned_path = Data.parent_dir + cleaned_path + '/' + origin_file
    return final_cleaned_path

def cleaned_file(file):
    """find cleaned file name"""
    dot = file.index('.')
    name1 = file[:dot]
    name2 = file[dot:]
    cleaned = name1 + '.cleaned' + name2
    return cleaned

def cleaned_files(root, files):
    """creates and moves cleaned files to their respective dir;
    also creates txts files and append info to them"""
    for file in files:
        os.chdir(root)
        #gather metadata
        cleaning_command = subprocess.Popen(['exiftool', file], stdout = subprocess.PIPE)
        metadata = cleaning_command.communicate()[0]
        #erase metadata
        cleaning_command = subprocess.Popen(['mat2', file], stdout = subprocess.PIPE)
        output = cleaning_command.communicate()[0]
        os.chdir(Data.parent_dir)
        #check if the file is supported by mat2
        if output == b'':
            #create cleaned.txt add metadata
            os.system('echo CLEANED >> cleaned.txt')
            #adding "" for files with white spaces, this way linux terminal can read them
            os.system('echo ' + str(metadata) + ' >> cleaned.txt')
            os.system('echo -------------------------------------------- >> cleaned.txt')
            #move cleaned file to respective cleaned directory
            shutil.move((root + '/' + cleaned_file(file)),
                        path_cleaned_dir(cleaned_file(file), root))
        else:
            #create not_cleaned.txt add metadata
            os.system('echo ' + str(output) + ' >> not_cleaned.txt')
            os.system('echo ' + str(metadata) + ' >> not_cleaned.txt')
            os.system('echo location.cleaned: ' + str(path_cleaned_dir(file, root))
                      + ' >> not_cleaned.txt')
            os.system('echo -------------------------------------------- >> not_cleaned.txt')
            #move copy of file to respective cleaned directory
            shutil.copy((root + '/' + file), path_cleaned_dir(file, root))
def main():
    """master function"""
    for root in os.walk(Data.path):
        cleaned_dirs(root[0])
    for root in os.walk(Data.path):
        cleaned_files(root[0], root[2])

main()
