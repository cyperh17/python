import os

dir_path = 'D:/test'
os.chdir(dir_path)

for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)

    #renaming file here
    #''.strip() #trim
    #''.zfill(2) #2 digits wide
    #os.rename(f, '') #renames file