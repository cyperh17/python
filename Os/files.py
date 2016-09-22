import os

file_path = 'C:\test.txt'

#LBYL
# if os.access(file_path, os.R_OK): #Race Condition because we are openning file in nex few second
#     with open(file_path) as f:
#         print(f.read())
# else:
#     print('File is inaccecible')

#EAFP
# try:
#     f = open(file_path) #no Race Condition
# except IOError as e:
#     print('File is inaccecible')
# else:
#     with f:
#         print(f.read())