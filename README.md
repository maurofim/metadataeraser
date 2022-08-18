# metadataeraser

***********************
Coded by maurofim
mauro.fim92@gmail.com
***********************

Automates the use of 'mat2' with python, to work with the files in a directory specify by the user;
it erases all metadata of the files and generates a txt file (cleaned.txt) with the information that
was cleaned (using 'exiftool'). It generates a copy of the directory tree in case there are subdirectories
and puts the cleaned files in their respective directory; the files that couldn't be cleaned are copied
and the information of their location and metadata would be in a separate txt file(not_cleaned.txt).
Works only on linux yet...
