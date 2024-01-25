def findPassword(enter): #finds password in file top-100k-password-list.txt
    if(len(enter)>5):
        raise Exception("The string cannot be greater than maximum length")
    if(len(enter)==0):
        raise Exception("Please enter a string")
    found=False
    try:
        fileReader=open("top-100k-password-list.txt","r")
        lines=fileReader.readlines()
        for i in lines:
            if enter in i:
                print(i)
                found=True
        if(not found):
            print(f"No password contains {enter}")
    except FileNotFoundError:
        print("File URL is incorrect")


if __name__ == '__main__' :
    s=str(input("Enter String: "))
    try:
        findString(s)
    except Exception as e:
        print(str(e))
