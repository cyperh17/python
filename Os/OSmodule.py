#1
# import os, glob

# os.chdir('C:/')

# for file in glob.glob('*.*'):
#     print(file)

import os
from datetime import datetime

#print(dir(os))

#print(os.getcwd()) #current working directory

#os.chdir('c:\Users\cyperh\Desktop') #changing directory, sets the new cwd

#print(os.listdir()) #prints all files in dir

#Making Dirs
#os.mkdir('') #create dir
#os.makedirs('') #creating all subdirectories in a path

#Removing Dirs
#os.rmdir('') #remove dir
#os.removedirs('') #remove all dirs in path

#File renaming
#os.rename('from', 'to')

#os.chdir(os.getcwd() + '\Os')
#print(os.stat('OSmodule.py').st_size) #filesize
#mod_time = os.stat('OSmodule.py').st_mtime #modification time
#print(datetime.fromtimestamp(mod_time))


#Directory Tree
#os.chdir(os.getcwd())

# for dirpath, dirnames, filenames in os.walk(os.getcwd()):
#     print('Current Path: ', dirpath)
#     print('Directories: ', dirnames)
#     print('Files: ', filenames)
#     print()


#Enviroment
#os.chdir(os.getcwd())
#print(os.environ.get('PATH')) #prints path env variable


#os.path module
# print(os.path.join('A', 'B')) #joining paths

# with open('', 'w') as f:
#     print(f)


#
print(os.path.basename('/temp/test.txt')) #gets file name from path
print(os.path.dirname('/temp/test.txt')) #gets dir name from path
print(os.path.split('/temp/test.txt')) #gets dir and file name from path

print(os.path.exists('C:/')) #checks if file exists

print(os.path.isdir('C:/')) #checks if this is a dir
print(os.path.isfile('C:/')) #checks if this is a file

print(os.path.splitext('C:/text.txt')) #return tuple with file ext separated

print(dir(os.path))