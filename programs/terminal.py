import time
loginCreds = input('Enter Access Key:\n')
f = open('programs/access.key')
AccessKey = f.read()
f.close()
if loginCreds == AccessKey:
    researchFiles = 'programs/research/w'
    menu1 = input('A)dd Research\nD)elete Research\nE)dit Research\n')
    if menu1 == 'A':
        print('Connecting...')
        createFile = input('Create File?(Y/N)')
        if createFile == 'Y':
            fileCreateName = input('File Name?')
            f = open(researchFiles + fileCreateName + '.txt', 'x')
            f = open(researchFiles + fileCreateName + '.txt', 'a')
            toAdd = input('What to add?')
            seconds = time.time()
            local_time = time.ctime(seconds)
        elif createFile == 'N':
            f = open(researchFiles + fileCreateName + '.txt', 'a')
            toAdd = input('What to add?')
            seconds = time.time()
            local_time = time.ctime(seconds)
            
            f.write('\n' + local_time + '\n' + toAdd)


    elif menu1 == 'D':
        print('Connecting...')
        fileDeleteName = input('File name?')
        f = open(researchFiles + fileDeleteName + '.txt')
        f.delete()
        print('Deleted')
            