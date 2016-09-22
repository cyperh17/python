import os, glob

os.chdir('C:/')

for file in glob.glob('*.*'):
    print(file)