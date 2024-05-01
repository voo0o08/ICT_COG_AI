from tkinter import*

from math import*

 

def ten():

    entry.insert(END, 10)

    

def hund():

    entry.insert(END, 100)

    

def plus():

    entry.insert(END, "+")

    

def res():

    result =eval(entry.get())

    entry.delete(0, END)

    entry.insert(END, str(result))

    

    

    

window =Tk()

entry = Entry(window)

entry.grid(row = 0)

 

 

 

 

e1= Button(window,text = "10",command=ten)

e2= Button(window,text = "100",command=hund)

e3= Button(window,text = "+",command =plus)

e4 =Button(window,text = "=",command =res)

 

e1.grid(row =1,column=0)

e2.grid(row =1,column=1)

e3.grid(row =2,column=0)

e4.grid(row =2,column=1)

 

window.mainloop()