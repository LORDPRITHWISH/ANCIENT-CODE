from tkinter import *
import time 

print(str)
# x=input("enter ir \t")
# l=x.split()
# print("output is",l)
global i
i=0



g=Tk()
l2=Label(g,text='prithwish',font=("Arial Black",20))
l2.pack(side="top")
print(l2['text'])
l2['text']="sampa"


c=0
def incri():
    global i
    t = time.localtime(time.time())
    l['text']=time.asctime(t)
    print(i)
    g.update()
    i+=10
    b.place(x=i,y=250)
# 
# if(i>200):
#     return
# g.after(1000,incri(i))
    

t = time.localtime(time.time())
g.geometry("750x500")
b=Button(g,text="prithwish",command=lambda:incri())
# c=Button(g,text="prithwish",background="red",width=20)

bt=Button(g,text="SAMPA",font=("Chiller",40),background="green")
bt.place(x=400,y=300)
b.place(x=0,y=230)
l=Label(g,text=time.asctime(t),font=("Arial Black",20))
l.pack(side="top")
 
g.mainloop()