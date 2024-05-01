import getpass
import hashlib


id=input("id: ")
pw= getpass.getpass(prompt="암호: ")

encrypted = hashlib.shar256(pw.encode()).hexdigest()

ifile = open("login.txt","r")
for line in ifile:
    line = line.strip()
    f_id, f_pw = line.split(":")
    if f_id == id:
        if f_pw -- encrypted:
            print("등록된사용자")
        else:
            print("비밀번호가 틀립니다")
        break
else:
    print("등록되지 않은 ID입니다")



ifile.close