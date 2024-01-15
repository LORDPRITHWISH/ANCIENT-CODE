import random
import pyperclip
from tkinter import *

def creator(x):
    li=[]
    for _ in range(x):
        y=random.randint(10,1000)
        k['text']=str(len(li))
        win.update()
        # print(len(li))
        
        # while True :
        #     if y not in li :
        #         li.append(y)
        #         break
        li.append(y)
        
        
    return li

def do() :
    a=str(creator(5000))
    print(a)
    pyperclip.copy(a)   
    Label(win,text="  DONE  ",font=('Goudy Stout',40,'bold')).pack()
    win.update()
    
    

win=Tk()
Label(win,text="  welcome MATE  ",font=('Goudy Stout',40,'bold')).pack()
k=Label(win,text=" starting  ",font=('Goudy Stout',80,'bold'))
k.pack()
win.update()

do()

win.mainloop()
                
# [19, 53, 65, 74, 85, 4, 40, 91, 55, 3]
