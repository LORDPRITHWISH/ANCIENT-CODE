from tkinter import *
from time import *
w=Tk()
# w.geometry("1600x1000")
w.geometry("1000x400")
w.title("numbers")
l=Label(w,text='',font=("Goudy Stout",30))
l.pack(side="top",padx=20,pady=20)
c=""
for i in range (100):
    c+=str(i)+" "
    l['text']=c
    w.update()
    sleep(.1)

w.mainloop()
