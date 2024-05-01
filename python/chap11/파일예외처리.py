import getpass
import hashlib

while True:
    id=input("id: ")
    p1= getpass.getpass(prompt="암호등록")
    p2= getpass.getpass(prompt="암호확인")

    if p1 != p2:
        print("두암호일치x 다시입력")
        continue
    else:
        break


encrypted = hashlib.sha256(p1.encode).hexdigest()

ofile = open("login.txt","a")
print(f"{id}:{encrypted}",file=ofile)
ofile.close