import os, os.path
import getpass
import sys

#needed setup
find = 1

user = getpass.getuser()

print '''GRID COMMAND
V.1

user set to: ''' +str(user)

path = os.getcwd()

dir_found = (os.path.isdir(path))

        
while True:
    if find == 'check dir':
        dir_found = (os.path.isdir(path))
        if dir_found == False:
            print 'could not find directory at: ' +str(path)
            find = 2
            check = 0

        if dir_found == True:
            print 'found: ' +str(path)
            find = 1
            check = 0

    if find == 'check file':
        dir_found = (os.path.isfile(path))
        if dir_found == False:
            print 'could not find file at: ' +str(path)
            find = 2
            check = 0

        if dir_found == True:
            print 'found: ' +str(path)
            os.startfile(path) 
            find = 1
            check = 0        

    if find == 1:
        find = raw_input('')
        if find == 'cd':
            find_path = raw_input('cd to: ')
            
            path = path +str(find_path)
            find = 'check dir'
            
        if find == 'of':
            find_file = raw_input('file: ')
            path = path +str(find_file)
            find = 'check file'
            
        if find == 'ls':
            print os.listdir(path)
            find = 1

        if find == 'reset':
            path = os.getcwd()
            find = 1

        if find == 'reset to c:':
            path = 'C:'
            find = 'check dir'

        if find == 'reset to cwd':
            path = os.getcwd()
            find = 'check dir'
            
        if find == 'exit':
            sys.exit()
            
            

    if find == 2:
        path = os.getcwd()
        find = 1



