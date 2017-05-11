import crypt
def testpass(cryptPass):
    salt=cryptPass[0:2]#分片，即提取前两位

    dictFile=open('dictionary.txt','r')
    for word in dictFile.readlines():
        word=word.strip('\n')
        cryptWord=crypt.crypt(word,salt)#将字典中的密码加密为哈希值
        if (cryptWord==cryptPass):
            print("[+] Found PassWord:"+word+"\n")
            return
    print("[-] Passwword Not Found.\n")
    return
def main():
    passFile=open('passwords.txt')
    for line  in passFile.readlines():
        if ":" in line:
            user =line.split(':')[0]
            cryptPass=line.split(':')[1].strip(' ')
            print("[*] Cracking PassWord For :" +user)
            testpass(cryptPass)



if __name__ == '__main__':
    main()