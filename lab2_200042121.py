#! /bin/python3

import sys


def password_validator(password,filename):
    if(not password.isascii()):
        raise Exception(f"{sys.argv[0][2:]}: Password should contain only ascii characters, or in other words invalid string as first argument")
    if(len(password)>5):
        raise Exception(f"{sys.argv[0][2:]}:Password Length exceeds maximum of 5 but here length is {len(password)}")
    if(len(filename)>20):
        raise Exception(f"{sys.argv[0][2:]}:File name length exceeds maximum of 20 but here the length is {len(filename)}")
    if('/' in filename):
        raise Exception(f"{sys.argv[0][2:]}:File name cannot contain /")
    filehandlerRead=open('top-100k-password-list.txt','r')
    filelines=filehandlerRead.readlines()
    filehandlerRead.close()
    filehandlerWrite=open(filename,'w')
    endlen=-len(password)
    for i in filelines:
        query=i[:-1]
        if(len(password)<=len(query) and query[endlen:]==password):
            filehandlerWrite.write(i)
    filehandlerWrite.close()






if __name__=="__main__":
    try:
        if(len(sys.argv)<=2):
            raise Exception(f"{sys.argv[0][2:]}: Filename must be present")
        password_validator(sys.argv[1],sys.argv[2])
    except Exception as e:
        print(e)

