#! /bin/python3
try:
    fileReader=open('top-100k-password-list.txt','r')
    lines=fileReader.readlines()
    fileWriter=open('passwords_for_dummies.txt','w')
    fileWriter
    for i in lines:
        if i[:4]=='pass':
            fileWriter.write(i)
    if(len(lines)==0):
        fileWriter.write('No password starts with pass')
except Exception as e:
    print(f"{sys.argv[0]}: "+e)

