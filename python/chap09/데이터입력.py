##
#	온도 변환 프로그램을 GUI 기반으로 구현한다. 
#
from tkinter import *
import pickle

# 이벤트 처리 함수를 정의한다. 

forms = []
def process():
    ofile = open("user.dat", "ab")
    uinfo = {}
    uinfo["이름"] = forms[0].get()
    uinfo["직업"] = forms[1].get()
    uinfo["나이"] = forms[2].get()
    pickle.dump(uinfo, ofile)
    ofile.close()
    
def load():
    ifile = open("user.dat", "rb")
    uinfo = pickle.load(ifile)
    print(uinfo)
    
def printUser():
    pass
    
def reset():
    e1.delete(0, END)
    e2.delete(0, END)
    
window  = Tk()

Label(window , text="이름").grid(row=0, column=0)
Label(window, text="직업").grid(row=1, column=0)
Label(window, text="나이").grid(row=2, column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(window, text="파일에 저장", command=process).grid(row=3, column=0)
Button(window, text="다시 입력", command=reset).grid(row=3, column=1)
Button(window, text="파일 내용 출력", command=load).grid(row=3, column=0)
window.mainloop()